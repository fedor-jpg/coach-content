"""Validate the authored scenario catalogue and render read-only skill references."""

import hashlib
import json
from setup_library import function_review


def require(condition, message):
    if not condition:
        raise ValueError(f"Scenarios: {message}")


def read_scenarios(references, coverage, observation):
    data = json.loads((references / "scenarios.json").read_text())
    require(data["schema_version"] == 1 and data["profile"] == observation["profile"] == "normal-mcp", "unsupported schema/profile")
    require(data["lifecycle"]["runtime_accepted"] == 0, "capability is not runtime acceptance")
    families = data["families"]
    require(len({family["id"] for family in families}) == len(families), "duplicate family")
    variants = [variant for family in families for variant in family["variants"]]
    require(len({variant["id"] for variant in variants}) == len(variants), "duplicate variant")
    sources = [source for variant in variants for source in variant["source_ids"]]
    expected = {row["source_id"] for row in coverage["records"]}
    require(len(sources) == 60 and len(set(sources)) == 60 and set(sources) == expected, "each of 60 sources needs exactly one primary variant")
    require(set(data["source_fingerprints"]) == expected, "source fingerprint membership mismatch")
    for fingerprint in data["source_fingerprints"].values():
        require(len(fingerprint) == 64 and all(letter in "0123456789abcdef" for letter in fingerprint), "invalid source fingerprint")
    capabilities = observation["capabilities"]
    for family in families:
        require(family["goal"] and family["title"] and family["fit"] and family["variants"], "empty family")
        for variant in family["variants"]:
            identity = variant["id"]
            for field in ("entry", "name", "mandatory_conditions", "outcome", "consent", "external_completion", "deduplication"):
                require(variant[field], f"{identity}: missing {field}")
            require("route" not in variant, f"{identity}: requirements are not a sequential route")
            require(variant["runtime_status"] == "not_tested" and variant["lifecycle_ref"] == data["lifecycle"]["id"], f"{identity}: invalid lifecycle")
            require(variant["requirements"] and set(variant["requirements"]) <= set(capabilities), f"{identity}: unknown capability")
            require(set(variant["source_notes"]) == set(variant["source_ids"]), f"{identity}: lost per-source difference")
            function_review(variant, observation)
            assessment = variant["assessment"]
            require(assessment["status"] in data["status_labels"] and assessment["reason"], f"{identity}: missing classification ground")
            require(isinstance(assessment["missing_source_behavior"], list), f"{identity}: invalid source gaps")
            require((assessment["status"] == "insufficient_data") == bool(assessment["missing_source_behavior"]), f"{identity}: data gap is not a tool gap or client input")
            unsupported = [key for key in variant["requirements"] if capabilities[key]["state"] != "documented"]
            if assessment["status"] == "supported":
                require(not unsupported and not assessment["replacement"], f"{identity}: unsupported requirement cannot be green")
            if assessment["status"] == "unavailable":
                require(unsupported, f"{identity}: unavailable needs a concrete absent requirement")
            replacement = assessment["replacement"]
            if assessment["status"] == "replacement":
                require(replacement, f"{identity}: replacement must name changed result")
            if replacement:
                require(replacement["changes"] and replacement["result"] and replacement["requires_consent"] is True, f"{identity}: replacement requires consent")
    continuations = data["continuations"]
    require(continuations["common_instructions"], "missing continuation boundaries")
    require(set(continuations["sources"]) <= expected, "unknown continuation source")
    for source, contexts in continuations["sources"].items():
        require(contexts and len({item["template"] for item in contexts}) == len(contexts), f"{source}: duplicate continuation")
        for context in contexts:
            require(context["template"] in continuations["templates"] and context["scope"] and context["source_title"], f"{source}: invalid continuation")
            template = continuations["templates"][context["template"]]
            require(all(template[field] for field in ("title", "provider", "inputs", "instructions")), "incomplete continuation template")
    require(all(item.get("summary") and "summary_ru" not in item for item in capabilities.values()), "missing English capability summary")
    return data


def continuation_prompts(data):
    variants = {source: (family, variant) for family in data["families"] for variant in family["variants"] for source in variant["source_ids"]}
    output = {}
    for source, contexts in data["continuations"]["sources"].items():
        family, variant = variants[source]
        output[source] = []
        for context in contexts:
            template = data["continuations"]["templates"][context["template"]]
            lines = [f"Help me prepare: {template['title']}.", f"Selected source: {source} - {context['source_title']}.",
                     f"Goal: {family['goal']}", f"Variant: {variant['name']}", f"Scope: {context['scope']}",
                     f"Source entry: {variant['entry']}", "Source requirements: " + "; ".join(variant["mandatory_conditions"]),
                     "Source timing: " + ("; ".join(variant["timing"]) or "No exact timer captured."),
                     "Source outcome: " + variant["outcome"]]
            excerpt = context["source_excerpt"]
            if excerpt:
                lines += [f"Captured text ({excerpt['node_id']}, not approved campaign copy):", excerpt["text"]]
            functional = variant["setup"]["function_review"]
            lines += ["Current setup decision: " + functional["status"] + ". " + functional["reason"], "Primary Chatfuel result: " + functional["primary_result"]]
            if functional["status"] != "adaptation_draft_requires_consent":
                lines += ["Selected Chatfuel setup is disabled. This external planning prompt does not bypass its missing capability or source evidence."]
            lines += [template["provider"], "Ask me for: " + "; ".join(template["inputs"]) + "."]
            steps = template["instructions"] + data["continuations"]["common_instructions"]
            lines += [f"{index}. {text}" for index, text in enumerate(steps, 1)]
            if template["citations"]:
                lines += ["Official guidance checked 2026-11-02:"] + [f"{item['title']}: {item['url']}" for item in template["citations"]]
            output[source].append({"id": context["template"], "title": template["title"], "scope": context["scope"],
                                   "inputs": template["inputs"], "citations": template["citations"], "prompt": "\n".join(lines)})
    return output


def scenario_outputs(references, coverage, observation):
    data = read_scenarios(references, coverage, observation)
    mapping = {row["source_id"]: row for row in coverage["records"]}
    labels = data["status_labels"]
    variants = [variant for family in data["families"] for variant in family["variants"]]
    prompts = continuation_prompts(data)
    sha = lambda name: hashlib.sha256((references / name).read_bytes()).hexdigest()
    index = {"schema_version": 1, "profile": data["profile"], "version": data["version"],
             "scenarios_sha256": sha("scenarios.json"), "capability_sha256": sha("capability-observation.json"),
             "coverage_sha256": sha("source-coverage.json"), "family_count": len(data["families"]),
             "variant_count": len(variants), "source_count": 60, "continuation_prompts": prompts,
             "families": [{"id": family["id"], "file": f"scenario-details/{family['id']}.md"} for family in data["families"]]}
    compact = ["# Funnel library", "", f"{len(data['families'])} business goals, {len(variants)} variants, 60 sources. Ordinary Chatfuel MCP.",
               "Capability observation: " + observation["observed_at"] + ". Launch untested; accepted full paths: 0.",
               "A documented operation does not prove full-path readiness. Adaptations need owner approval.",
               "Read setup-index.md, setup-policy.md and the selected setup-details/<variant>.md. The functional gate controls preparation; older native recipes cannot bypass it.",
               "Do not run a local helper or load all 60 graphs. A missing analogue does not prove a missing tool.",
               "External continuation prompts are generated verbatim in the selected detail file and scenario-index.json. They prepare drafts, not installed integrations.", ""]
    result = {"scenario-index.json": json.dumps(index, ensure_ascii=False, indent=2) + "\n"}
    for family in data["families"]:
        compact += [f"## [{family['title']}](scenario-details/{family['id']}.md)"]
        detail = [f"# {family['title']}", family["goal"], family["fit"], "", data["lifecycle"]["summary"], *data["lifecycle"]["gates"], "",
                  "Profile: ordinary Chatfuel MCP. Documentation observation: " + observation["observed_at"] + ". Not an account test."]
        for variant in family["variants"]:
            assessment = variant["assessment"]
            functional = variant["setup"]["function_review"]
            status = functional["status"]
            compact += [f"- {variant['name']}: {status}."]
            detail += ["", f"## {variant['name']}", status, "Entry: " + variant["entry"], "Outcome: " + variant["outcome"],
                       "Requirements: " + "; ".join(variant["mandatory_conditions"]),
                       "Timing: " + ("; ".join(variant["timing"]) or "No separate exact timer captured."),
                       "Consent: " + variant["consent"], variant["external_completion"], functional["reason"], "Primary result: " + functional["primary_result"],
                       "Retained: " + "; ".join(functional["retained"]), "Omitted: " + "; ".join(functional["omitted"]), "Limitations: " + "; ".join(functional["limitations"])]
            if status != "adaptation_draft_requires_consent":
                detail += ["Setup disabled. Source and older analogue links below are references only, not fallback setup instructions."]
            detail += ["Missing source facts: " + ("; ".join(assessment["missing_source_behavior"]) or "None blocking this assessment."),
                       "Client inputs: " + ", ".join(variant["client_inputs"]), "### Capability evidence"]
            for capability in variant["requirements"]:
                item = observation["capabilities"][capability]
                detail += [f"- {capability}: {item['state']}; {item['basis']}; {', '.join(item['tools'])}; {', '.join(item['fields'])}. {item['claim']}"]
            detail += ["### Sources and described analogues", variant["deduplication"]]
            for source in variant["source_ids"]:
                recipe = mapping[source]["recipe_id"]
                link = f"[Described analogue {recipe}](../native-recipes/{recipe}.md)" if recipe else "No authored analogue; this does not establish tool availability."
                detail += [f"- {source}: {variant['source_notes'][source]} {link}"]
                for prompt in prompts.get(source, []):
                    detail += [f"### {prompt['title']} - {source}", prompt["scope"], "```text", prompt["prompt"], "```"]
        result[f"scenario-details/{family['id']}.md"] = "\n".join(detail) + "\n"
    result["scenario-index.md"] = "\n".join(compact) + "\n"
    return result
