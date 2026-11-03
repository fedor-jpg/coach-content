"""Generate portable setup references and audit captured graphs. Never call a connector."""

import hashlib
import json
import re
from copy import deepcopy
from datetime import date


def stable(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else stable(value).encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError("Setup library: " + message)


COMMENT_SCOPE_FIELDS = ("post_ids", "keywords", "match_mode")
FUNCTION_STATUSES = {"adaptation_draft_requires_consent", "waiting_for_chatfuel", "source_incomplete_reference_only"}


def function_review(variant, observation):
    review = variant["setup"]["function_review"]
    require(review["status"] in FUNCTION_STATUSES and review["reason"] and review["primary_result"], "missing functional decision: " + variant["id"])
    require(review["source_requirements"] == variant["mandatory_conditions"] and review["source_timing"] == variant["timing"], "stale functional review")
    require(set(review["blocking_dependencies"]) <= set(observation["capabilities"]), "unknown functional dependency")
    available = review["status"] == "adaptation_draft_requires_consent"
    require(bool(variant["setup"]["bindings"]) == available, "blocked variant cannot expose setup bindings")
    require(not available or not review["blocking_dependencies"], "essential unsupported function cannot be an active draft")
    if review["status"] == "waiting_for_chatfuel":
        require(review["blocking_dependencies"], "waiting needs a concrete dependency")
    return review


def validate_comment_staging(approved, readback):
    """Local rehearsal of complete projected scope values, not a tool or ownership check."""
    require(readback.get("readback_complete") is True and readback.get("enabled") is False, "complete OFF readback required")
    for key in COMMENT_SCOPE_FIELDS:
        require(key in approved and key in readback, "missing scope readback: " + key)
        expected, actual = approved[key], readback[key]
        if key in {"post_ids", "keywords"}:
            require(isinstance(expected, list) and isinstance(actual, list), "incomplete scope list: " + key)
            require(all(isinstance(value, str) and value for value in expected + actual), "invalid scope value: " + key)
            require(len(expected) == len(set(expected)) and len(actual) == len(set(actual)), "duplicate scope value: " + key)
            require(set(expected) == set(actual), "scope mismatch: " + key)
        else:
            require(isinstance(expected, str) and expected and expected == actual, "scope mismatch: " + key)
    return True


def leaves(value, prefix=""):
    if isinstance(value, dict) and value:
        for key, child in value.items():
            yield from leaves(child, prefix + "/" + key.replace("~", "~0").replace("/", "~1"))
    elif isinstance(value, list) and value:
        for index, child in enumerate(value):
            yield from leaves(child, f"{prefix}/{index}")
    else:
        yield prefix, value


def field_values(value, prefix="", phase="captured"):
    result = []
    if isinstance(value, dict):
        phase = value.get("phase", phase)
        if "value" in value or "checked" in value:
            fields = {key: value[key] for key in ("name", "label", "type", "value", "value_state", "checked", "options", "options_exact", "validation", "validation_exact") if key in value}
            result.append({"path": prefix, "phase": phase, "fields": fields})
        for key, child in value.items():
            if key not in {"evidence", "identity", "node_match", "scope_history"}:
                result.extend(field_values(child, f"{prefix}/{key}", phase))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            result.extend(field_values(child, f"{prefix}/{index}", phase))
    return result


def validate_operation(operation, observation, scope, resolved=False):
    contract = observation["normal_tool_contract"]
    require(operation["tool"] == "update_automation_setting", "preparation only contains explicit-setting drafts")
    settings = operation["settings"]
    require(len(settings) == 1, "one setting per call")
    name, values = next(iter(settings.items()))
    require(name in contract["settings"], f"unknown setting {name}")
    schema = contract["settings"][name]
    require(set(values) <= set(schema["fields"]), f"unknown field in {name}")
    mode = next(iter(schema["fields"]))
    require(mode in values, f"missing mode in {name}")
    if values.get(mode) == "ExactText":
        require("exactTextReply" in values, f"missing fixed copy in {name}")
    if values.get(mode) == "UsingAI":
        require("messagePrompt" in values, f"missing AI copy in {name}")
    for key, value in values.items():
        definition = schema["fields"][key]
        placeholder = isinstance(value, str) and value.startswith("$resolved.")
        require(not (resolved and placeholder), f"unresolved {key}")
        if placeholder:
            continue
        if isinstance(definition, list):
            require(value in definition, f"invalid enum {name}.{key}")
        elif definition == "nonempty_text":
            require(isinstance(value, str) and value.strip(), f"empty {name}.{key}")
            require(len(value) <= schema.get("limits", {}).get(key, 5000), f"over limit {name}.{key}")
        elif definition == "boolean":
            require(isinstance(value, bool), f"invalid boolean {name}.{key}")
        elif definition == "list":
            require(isinstance(value, list), f"invalid list {name}.{key}")
            for item in value:
                require(set(item) == set(schema["item_fields"]), f"invalid list item {name}.{key}")
                require(all(isinstance(text, str) and text.strip() for text in item.values()), f"empty item {name}.{key}")
    require(not (scope == "dm_base" and name == "incomingMessages" and values.get("howToReply") == "DontReply"), "DontReply forbidden on DM")
    require(not (scope != "owned_comment" and name in {"publicReply", "privateReply"}), "reply setting requires comment scope")
    require(not (name == "publicReply" and "likeContactComment" in values), "Instagram cannot set Facebook like field")
    require(name != "bookingRules", "external URL preparation must not alter global booking autonomy")


def draft_plan(recipe, direct, observation, binding):
    if recipe:
        modes = recipe["native"]["modes"]
        inputs = [item for item in recipe["inputs"] if item["type"] != "ids"]
        messages = {item["id"]: item["text"] for item in recipe["messages"]}
        instruction = recipe["native"]["messages_text"]
        contact = "Optional, only after new explicit consent; never imply external subscription." if set(modes) & {"E", "T"} else "No contact capture." 
        branches = deepcopy(recipe["route"])
    else:
        modes = direct["modes"]
        inputs = [{"name": name, "type": "url" if name.endswith("_url") else "text", "requirement": "required", "description": "Supply the business value and approve its use in this selected draft."} for name in direct["inputs"]]
        messages = {"initial": direct["initial"], "public": "{public_text}" if "C" in modes else "", "refusal": "{refusal_text}" if "D" in modes else "", "handoff": "{handoff_text}" if "H" in modes else ""}
        messages.update(direct.get("messages", {}))
        instruction, contact, branches = direct["instruction"], direct["contact_requirement"], deepcopy(direct.get("branches"))
    scope = binding["target"]
    if scope == "dm_base":
        modes = [mode for mode in modes if mode not in {"C", "N", "P"}]
        if "D" not in modes:
            modes.append("D")
        messages["public"] = ""
        messages["placement"] = "DM {keyword}." if any(item["name"] == "keyword" for item in inputs) else ""
        if not messages.get("refusal"):
            messages["refusal"] = "Understood. I will not continue this campaign."
    instruction += "\n" + binding.get("instruction", "")
    if "Q" in modes:
        instruction += "\nAfter new affirmative consent ask {question_one}, wait for its actual answer, then {question_two}; wait for a distinct answer. Apply {qualification_policy}. If appropriate and {next_step}=booking_link, give {booking_url}, without qualification-only handoff. If {next_step}=handoff or unclear, use the team. If inappropriate, explain politely without a booking claim. Omit booking_url when handoff is selected."
    if "E" in modes and recipe:
        instruction += "\nExplain {contact_purpose}, obtain new explicit consent, then request an optional email. Refusal does not revoke delivered value. Never reuse historical email or consent."
    if "T" in modes and recipe:
        instruction += "\nExplain {contact_purpose}, obtain new explicit consent, then request an optional phone number with country code. No SMS subscription or call is implied."
    if "W" in modes:
        contact = "Intended saved states: fresh YES -> joined; STOP -> withdrawn before state-dependent handoff. Required contact-value readback is unavailable in normal MCP. Neither chat text nor capture settings verify membership or withdrawal."
        instruction = "Ask: Join the waitlist for {launch_name}, for {launch_purpose}? {consent_text} Intended attribute: {membership_attribute}. Fresh YES requests joined; STOP requests withdrawn and ends this campaign. Preserve unset or existing state otherwise; never reuse old consent. Normal MCP has no contact-attribute-value reader. Do not claim saved membership or withdrawal from chat text or capture configuration. Any confirmation or handoff requiring the saved value stays blocked; drafting copy and capture settings remains possible."
        messages["continuation"] = instruction
        for step in branches["steps"]:
            if step["id"] in {"joined", "withdrawn", "handoff"}:
                step["action"] = "Intended branch only; saved-state proof unavailable through normal MCP. " + step["action"]
    if recipe and recipe["id"] == "inro-6049":
        instruction += "\nAsk {question_one}, wait for a real answer, then {question_two}; wait for its answer, then give {registration_url}. No survey-completion or access claim."
    if recipe and recipe["id"] == "inro-4484":
        instruction += "\nOffer two mutually exclusive choices: {option_one} -> {option_one_url}; {option_two} -> {option_two_url}. Ask {preference_question}, wait, and give only the selected destination. Never run both branches in sequence."
    if recipe and recipe["id"] == "inro-6085":
        instruction += "\nApproved facts: {known_facts}. Handoff criteria: {handoff_conditions}."
    if recipe and recipe["id"] == "inro-6082":
        messages["public"] = "{thanks_text}"
    if recipe and not set(recipe["native"]["modes"]) & {"D"} and scope == "dm_base":
        branches = None
    if branches:
        branches["steps"][0]["action"] = binding["entry"]
    copy_names = {"campaign", "language", "keyword", "question_one", "question_two", "email_request", "phone_request", "preference_question"}
    inputs = [{**item, "provided_by": "resolved_by_assistant" if item["name"] == "membership_attribute" else "drafted_by_assistant_for_approval" if item["name"] in copy_names or item["name"].endswith(("_text", "_prompt")) else "business_fact_if_missing"} for item in inputs]
    names = {item["name"] for item in inputs}
    operations = []
    def add(name, values):
        operation = {"tool": "update_automation_setting", "target": scope, "settings": {name: values}}
        validate_operation(operation, observation, scope)
        operations.append(operation)
    if scope == "owned_comment":
        add("publicReply", {"publicReplyHowToReply": "DontReply"} if "N" in modes else {"publicReplyHowToReply": "ExactText", "exactTextReply": messages["public"] or "{public_text}"})
        add("privateReply", {"privateReplyHowToReply": "DontReply"} if "P" in modes else {"privateReplyHowToReply": "ExactText", "exactTextReply": messages["initial"]})
    if "D" in modes:
        entry = binding["entry"]
        prompt = f"Campaign {{campaign}}. Language: {{language}}. Entry: {entry}. First message: {messages['initial']}\n{instruction}\nHandle refusal before keyword matching. "
        if messages.get("refusal"):
            prompt += f"On refusal: {messages['refusal']} End this campaign. "
        prompt += "Use only new answers and consent from this run. Same-run repeats must not restart intake or duplicate capture. Do not send after silence or an external click. Preserve unrelated support."
        prompt += "\nApproved reply texts by branch (choose only the applicable branch; never send these as a sequence):\n" + "\n".join(f"{key}: {value}" for key, value in messages.items() if value and key not in {"initial", "public", "placement"})
        if scope == "owned_comment":
            prompt += " The one private comment reply has already sent the opener. Wait for the person's actual linked reply; do not resend the opener or send a second unsolicited DM. Continue only within the permitted messaging window."
        add("incomingMessages", {"howToReply": "UsingAI", "messagePrompt": prompt})
        if scope == "owned_comment":
            add("whenAIReplies", {"option": "Always"})
    else:
        require(scope == "owned_comment", "silent one-shot must be comment-scoped")
        add("incomingMessages", {"howToReply": "DontReply"})
    if scope == "owned_comment":
        add("followUps", {"howToSend": "DontSend"})
    additions = {}
    if "H" in modes:
        additions["switchToHuman"] = {"switchingConditions": "Campaign {campaign}: the person requests the team or facts are unresolved." + (" After both actual answers, hand off for next_step=handoff; never for qualification alone when next_step=booking_link." if "Q" in modes else ""), "messagePrompt": messages["handoff"]}
        if "W" in modes:
            additions["switchToHuman"]["switchingConditions"] += " Any handoff requiring saved joined/withdrawn state is blocked without actual value proof; normal MCP cannot supply that readback. Do not infer it from chat text."
        add("switchToHuman", {"howToSwitch": "SwitchToTeammates", "rules": "$resolved.safe_handoff_rules"})
    if set(modes) & {"E", "T", "W"}:
        detail = contact if not recipe else ("Save joined/withdrawn only on explicit current-run YES/STOP for this campaign; never reuse old consent." if "W" in modes else "Save a new optional consented " + ("phone" if "T" in modes else "email") + " for the approved purpose; no external subscription.")
        purpose = "{contact_purpose}" if "contact_purpose" in names else "{sms_purpose}" if "sms_purpose" in names else "the approved campaign purpose"
        additions["collectContactInfo"] = [{"attribute": "$resolved.verified_" + field + "_attribute", "description": "Campaign {campaign}; " + field + " for " + purpose + ": " + detail} for field in direct["contact_fields"]] if direct and direct.get("contact_fields") else {"attribute": "$resolved.verified_attribute", "description": "Campaign {campaign}: " + detail}
        add("collectContactInfo", {"howToCollect": "CollectInfo", "captures": "$resolved.safe_captures"})
    placeholders = set(re.findall(r"\{([a-z_]+)\}", stable([operations, additions, messages, instruction])))
    require(placeholders <= names, f"undeclared draft inputs: {placeholders - names}")
    payload = stable([operations, additions])
    require(all("{" + name + "}" in payload for name in binding["output_bindings"]), "selected outcome missing from concrete setting drafts")
    require(scope in binding["allowed_targets"], "selected entry contradicts binding")
    if branches:
        ids = {step["id"] for step in branches["steps"]}
        require(len(ids) == len(branches["steps"]), "duplicate draft step")
        require(all(edge["from"] in ids and edge["to"] in ids for edge in branches["transitions"]), "broken draft branch")
        require(all(set(step["message_ids"]) <= set(messages) for step in branches["steps"]), "missing draft copy")
        reachable = {branches["steps"][0]["id"]}
        while True:
            expanded = reachable | {edge["to"] for edge in branches["transitions"] if edge["from"] in reachable}
            if expanded == reachable:
                break
            reachable = expanded
        require(reachable == ids, f"unreachable draft steps: {sorted(ids - reachable)}")
    readback = observation["normal_tool_contract"]["readback_boundaries"]["contact_attribute_values"]
    gates = ["Preserve current whenAIReplies and followUps values, including inheritance, on the shared DM base. If its schedule or active follow-ups conflict with the proposed behavior, hold affected configuration or obtain separate approval for the exact base-wide change. No schedule/follow-up write is a default draft operation."] if scope == "dm_base" else ["Before staging an owned OFF custom, complete readback must equal approved posts, keywords and match mode. Reply-setting updates cannot change filters. A mismatch blocks staging; setup_comment_replies needs separate immediate-enabled approval."]
    if set(modes) & {"E", "T", "W"}:
        gates.append(readback["claim"])
    if "W" in modes:
        gates.append("Missing mandatory saved-state proof blocks membership/withdrawal confirmation and any dependent handoff, not copy or setting preparation.")
    return {"origin": "existing_described_analogue" if recipe else "authored_source_adaptation", "analogue_id": recipe["id"] if recipe else None,
            "selection": binding,
            "preserve_settings": ["whenAIReplies", "followUps"] if scope == "dm_base" else [],
            "entry_readback_fields": list(COMMENT_SCOPE_FIELDS) if scope == "owned_comment" else [],
            "preparation_gates": gates,
            "missing_readback": ["contact_attribute_values"] if set(modes) & {"E", "T", "W"} and not readback["available"] else [],
            "target": scope, "business_inputs": inputs, "messages": messages, "instruction": instruction,
            "intended_branches": branches, "contact_requirement": contact, "operations": operations, "list_additions": additions,
            "stop": {"tool": "set_automation_enabled", "enabled": False, "scope": scope, "gate": "Only the owned custom or exclusive unchanged DM base; never All or foreign/shared work."},
            "write_permission": "none", "runtime_status": "not_tested"}


def source_audit(source, variant, rules, observation):
    nodes = []
    for step in source["graph"]["steps"]:
        rule = rules[step["sourceType"]]
        capabilities = list(rule["capabilities"])
        if step["sourceType"] == "trigger":
            capabilities += [key for key in variant["requirements"] if key in {"comment", "dm-ai", "story", "live", "ad", "ref-link"}]
        if step["content"]["buttons"] or step["content"]["gallery"] or step["content"]["media"]:
            capabilities.append("buttons")
        if step["sourceType"] in {"condition", "contact_filter_condition"} and re.search(r"follow", step["content"]["text"] + step["content"]["preview"], re.I):
            capabilities.append("follower")
        if step["sourceType"] in {"actions", "condition"} and "score" in variant["requirements"]:
            capabilities.append("score")
        capabilities = sorted(set(capabilities))
        absent = [key for key in capabilities if observation["capabilities"][key]["state"] != "documented"]
        nodes.append({"id": step["id"], "source_type": step["sourceType"], "content": step["content"],
                      "capabilities": capabilities, "disposition": "requires_change_or_external_dependency" if absent else "documented_primitive_not_graph_equivalence",
                      "candidate_tool": "update_automation_setting" if rule["settings"] else None, "candidate_settings": rule["settings"],
                      "business_inputs": rule["business_inputs"], "reason": rule["explanation"], "unsupported": absent,
                      "known_fields": field_values(step["settings"]), "settings_pointer": f"/graph/steps/{len(nodes)}/settings",
                      "settings_sha256": sha(step["settings"]), "settings_leaf_count": len(list(leaves(step["settings"])))})
    return {"source_id": source["id"], "source_file": f"source-records/{source['id']}.json", "source_title": source["source"]["title"],
            "start": source["graph"]["start"], "nodes": nodes, "transitions": source["graph"]["transitions"],
            "transition_disposition": "Captured conditions and targets only; deterministic transitions cannot be imported through ordinary MCP.",
            "setup_screens": source["setup"], "global_fields": field_values(source["source"]["document"]),
            "source_settings_sha256": sha(source["source"]["document"]), "source_leaf_count": len(list(leaves(source["source"]["document"]))),
            "source_status": "Captured values preserved; unknowns and inspection variants are not defaults or requirements for an approved simpler adaptation."}


def verify_binding(packet, references, as_of=None):
    for name, expected in packet["bindings"].items():
        require(hashlib.sha256((references / name).read_bytes()).hexdigest() == expected, f"stale binding: {name}")
    observation = json.loads((references / "capability-observation.json").read_text())
    require((as_of or date.today()).isoformat() <= observation["normal_tool_contract"]["review_after"], "capability review expired; preparation may be discussed but no current-tool readiness claim")
    return True


def render(packet, policy, observation):
    variant = packet["variant"]
    review = packet["function_review"]
    lines = [f"# {variant['name']}", "", f"Setup {packet['revision']} | {variant['id']} | {packet['preparation_status']} | runtime not tested", "",
             "## Business Result", packet["goal"], packet["fit"], "Source entry: " + variant["entry"], "Source outcome: " + variant["outcome"],
             "Source requirements: " + "; ".join(variant["mandatory_conditions"]), "Source timing: " + ("; ".join(variant["timing"]) or "No exact timer captured."),
             "", "## Functional Availability", review["status"], review["reason"], "Primary result: " + review["primary_result"]]
    lines += ["Retained/replaced: " + text for text in review["retained"]]
    lines += ["Not retained: " + text for text in review["omitted"]]
    lines += ["Limitation: " + text for text in review["limitations"]]
    lines += ["Source fidelity and adaptation readiness are separate. Do not bypass a mandatory original gate by selecting an old analogue silently.",
              "", "## Shared Setup Procedure", "Read [setup-policy.md](../setup-policy.md) for read/prepare/approve/configure/readback/edit/return/stop. It takes precedence over old native-policy and GraphQL instructions. No writes or tests are authorized here.", "", "## Selected Preparation"]
    if not packet["plans"]:
        lines += ["SETUP DISABLED. Originals below are reference only. Do not generate setting payloads or fall back to historical recipes. A different ordinary-DM scenario is not this scenario. Stop at the named capability or source-evidence dependency."]
    lines += [f"- {key}: {observation['capabilities'][key]['summary']}" for key in packet["mandatory_dependencies"]]
    lines += [f"- Missing source behavior: {text}" for text in variant["assessment"]["missing_source_behavior"]]
    for plan in packet["plans"]:
        lines += [f"### {plan['selection']['label']}", "Choose this entry only; do not configure all alternatives. " + plan['selection']['entry'], "Entry change: " + plan['selection']['entry_change'], "Output: " + plan['selection']['output'], "Target: " + plan["target"],
                  "Ask only for missing business facts:"]
        lines += [f"- {item['name']}: {item['description']} ({item['requirement']})" for item in plan["business_inputs"] if item["provided_by"] == "business_fact_if_missing"]
        lines += ["Assistant-derived, not questionnaire fields: " + ", ".join(item["name"] for item in plan["business_inputs"] if item["provided_by"] != "business_fact_if_missing") + ". Propose naming, entry words and complete copy; infer language. Resolve technical attributes/IDs from tools and hold unresolved writes. Ask approval of the completed draft."]
        lines += ["#### Preparation Gates", *["- " + gate for gate in plan["preparation_gates"]]]
        lines += ["#### Copy and Conversation Instructions"]
        lines += [f"{key}: {value}" for key, value in plan["messages"].items() if value]
        lines += [plan["instruction"], "Contact rule: " + (plan["contact_requirement"] or "No contact capture in this plan.")]
        if plan["intended_branches"]:
            lines += ["#### Intended Alternative Branches (Instructions, Not Imported Flow)"]
            for step in plan["intended_branches"]["steps"]:
                lines += [f"- {step['id']}: {step['action']}"]
                lines += [f"  - If {edge['condition']} -> {edge['to']}" for edge in plan["intended_branches"]["transitions"] if edge["from"] == step["id"]]
        lines += ["#### Exact Setting Drafts", "Not tool calls. Add resolved botID/automationID and privacy-safe context only after all gates; one setting per call.", "```json", json.dumps(plan["operations"], ensure_ascii=False, indent=2), "```"]
        if plan["list_additions"]:
            lines += ["Candidate additions; never send as a replacement for an unread existing list:", "```json", json.dumps(plan["list_additions"], ensure_ascii=False, indent=2), "```"]
    lines += ["", "## Complete Captured Topology", "Nodes below are not an ordered conversation. Follow only the listed outgoing edges. Empty exits remain unknown. Field phases distinguish defaults, inspection variants and current clone state."]
    for source in packet["sources"]:
        lines += [f"### {source['source_id']}: {source['source_title']}", f"Full captured settings/provenance: [selected source JSON](../{source['source_file']}). Start: {source['start'] or 'no captured graph'}."]
        if not source["nodes"]:
            lines += ["No runtime graph captured. Setup fields are evidence, not invented messages:"]
            unique = {stable([item["phase"], item["fields"]]): item for item in source["global_fields"]}
            lines += [f"- {item['phase']}: {stable(item['fields'])}" for item in unique.values()]
        for node in source["nodes"]:
            lines += [f"#### {node['id']} ({node['source_type']})", node["reason"], "Business input: " + "; ".join(node["business_inputs"]),
                      "Setting candidate: " + (f"{node['candidate_tool']}: {', '.join(node['candidate_settings'])}" if node["candidate_tool"] else "No direct normal-MCP setting"),
                      "Disposition: " + node["disposition"] + "; dependencies: " + ", ".join(node["capabilities"]),
                      "Captured text (not approved outbound copy):", "```text", node["content"]["text"], "```"]
            for name in ("buttons", "media", "gallery"):
                if node["content"][name]:
                    lines += [f"Captured {name}: {stable(node['content'][name])}"]
            unique = {stable([item["phase"], item["fields"]]): item for item in node["known_fields"]}
            lines += [f"- Field ({item['phase']}): {stable(item['fields'])}" for item in unique.values()]
            outgoing = [edge for edge in source["transitions"] if edge["from"] == node["id"]]
            lines += [f"- Edge {edge['id']}: {edge['from']} -> {edge['to']} | condition/label: {json.dumps(edge['label'], ensure_ascii=False)}" for edge in outgoing]
            if not outgoing:
                lines += ["- No captured outgoing edge; do not infer completion."]
        lines += ["All source settings, including non-field controls and inspection metadata, remain in the linked JSON. No unknown value is filled by an adaptation."]
    for source, prompts in packet["continuations"].items():
        for item in prompts:
            lines += [f"## External Continuation: {source} / {item['title']}", item["scope"], "```text", item["prompt"], "```"]
    lines += ["## Binding And Evidence", f"Profile: normal-mcp; observation {observation['observed_at']}, revision {observation['normal_tool_contract']['revision']}. Recheck after {observation['normal_tool_contract']['review_after']} and before every write.",
              "This is deterministic local authoring/rehearsal evidence, not an independent chat, connector test, delivery or live acceptance.",
              f"Structured audit: [setup record]({variant['id']}.json). Source changes and capability changes invalidate generated references; they never change live campaigns."]
    return "\n".join(lines) + "\n"


def setup_outputs(references, data, recipes, coverage, observation, prompts):
    index = json.loads((references / "setup-source-index.json").read_text())
    by_source = {}
    require(len(index["records"]) == 60, "source manifest must contain60")
    for item in index["records"]:
        source = json.loads((references / item["file"]).read_text())
        require(source["id"] == item["id"] and sha(source["source"]["document"]) == item["source_sha256"] == data["source_fingerprints"][source["id"]], "source values changed")
        require(sha(source["graph"]) == item["graph_sha256"], "captured topology/settings changed")
        require(len(source["graph"]["steps"]) == item["steps"] and len(source["graph"]["transitions"]) == item["edges"], "source count drift")
        by_source[source["id"]] = source
    policy = (references / "setup-policy.md").read_text()
    recipes = {recipe["id"]: recipe for recipe in recipes}
    result, records = {}, []
    for family in data["families"]:
        for variant in family["variants"]:
            authored = variant["setup"]
            functional = function_review(variant, observation)
            require(authored["write_permission"] == "none" and authored["runtime_status"] == "not_tested", "unqualified write/runtime claim")
            require("bindings" in authored, "variant lacks reviewed entry/output binding: " + variant["id"])
            review = authored["binding_review"]
            require(review["source_entry"] == variant["entry"] and review["source_outcome"] == variant["outcome"] and review["mandatory_conditions"] == variant["mandatory_conditions"], "stale binding review: " + variant["id"])
            require(review["plan_count"] == len(authored["bindings"]), "unreviewed entry alternative")
            for binding in authored["bindings"]:
                require(binding["approval_required"] and binding["source_requirements"] == variant["mandatory_conditions"], "missing mandatory source gates")
            plans = [draft_plan(recipes.get(binding.get("analogue_id")), binding.get("draft"), observation, binding) for binding in authored["bindings"]]
            sources = [source_audit(by_source[key], variant, data["setup"]["node_rules"], observation) for key in variant["source_ids"]]
            for example in functional["examples"]:
                require(example["source_id"] in variant["source_ids"], "example belongs to another variant")
                step = next((node for node in by_source[example["source_id"]]["graph"]["steps"] if node["id"] == example["node_id"]), None)
                require(step and example["source_text"] == step["content"]["text"], "invented original example text")
            dependencies = [key for key in variant["requirements"] if observation["capabilities"][key]["state"] != "documented"]
            names = ["scenarios.json", "capability-observation.json", "setup-policy.md", "setup-source-index.json", "source-coverage.json"] + [source["source_file"] for source in sources] + [f"described-recipes/{key}.json" for key in authored["analogue_ids"]]
            packet = {"schema_version": 1, "revision": data["setup"]["revision"], "variant": variant, "goal": family["goal"], "fit": family["fit"],
                      "preparation_status": functional["status"], "function_review": functional, "runtime_accepted": False,
                      "mandatory_dependencies": dependencies, "sources": sources, "plans": plans,
                      "continuations": {source: prompts.get(source, []) for source in variant["source_ids"]},
                      "bindings": {name: hashlib.sha256((references / name).read_bytes()).hexdigest() for name in names}}
            stem = "setup-details/" + variant["id"]
            result[stem + ".json"] = json.dumps(packet, ensure_ascii=False, indent=2) + "\n"
            result[stem + ".md"] = render(packet, policy, observation)
            records.append({"id": variant["id"], "name": variant["name"], "file": stem + ".md", "audit_file": stem + ".json", "source_ids": variant["source_ids"],
                            "status": packet["preparation_status"], "function_review": functional, "mandatory_dependencies": dependencies, "source_gaps": variant["assessment"]["missing_source_behavior"],
                            "steps": sum(len(source["nodes"]) for source in sources), "edges": sum(len(source["transitions"]) for source in sources),
                            "md_sha256": hashlib.sha256(result[stem + ".md"].encode()).hexdigest(), "json_sha256": hashlib.sha256(result[stem + ".json"].encode()).hexdigest()})
    metadata = {"schema_version": 1, "revision": data["setup"]["revision"], "scenario_version": data["version"], "capability_revision": observation["normal_tool_contract"]["revision"],
                "runtime_accepted": 0, "bindings": {name: hashlib.sha256((references / name).read_bytes()).hexdigest() for name in ["scenarios.json", "capability-observation.json", "setup-policy.md", "setup-source-index.json"]}, "variants": records}
    result["setup-index.json"] = json.dumps(metadata, ensure_ascii=False, indent=2) + "\n"
    lines = ["# Variant Setup Index", "", "57 selected setup references;60 originals. Read setup-policy.md and only the selected setup-details/<variant>.md. Never load all source graphs.",
             "Local preparation only. Every original has unsupported, changed or unknown requirements; no full-path or installed readiness is claimed.", ""]
    for family in data["families"]:
        lines += ["## " + family["title"]]
        for variant in family["variants"]:
            record = next(item for item in records if item["id"] == variant["id"])
            lines += [f"- [{variant['name']}]({record['file']}) | {', '.join(variant['source_ids'])} | {record['status']}"]
    result["setup-index.md"] = "\n".join(lines) + "\n"
    return result
