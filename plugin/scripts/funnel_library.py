#!/usr/bin/env python3
"""Validate canonical descriptions and generate native references, never runtime settings."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from scenario_library import scenario_outputs, read_scenarios, continuation_prompts
from setup_library import setup_outputs

REFERENCES = Path(__file__).resolve().parents[1] / "skills/funnels/references"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_library(references=REFERENCES):
    recipes = [load(path) for path in sorted((references / "described-recipes").glob("*.json"))]
    legacy = {path.stem: path for path in (references / "recipes").glob("*.json")}
    ids = [recipe["id"] for recipe in recipes]
    require(len(ids) == 30 and len(set(ids)) == 30 and set(ids) == set(legacy), "Expected exactly 30 canonical and legacy recipe identities")
    modes_defined = set("".join(re.findall(r"^- \*\*([CNPDQHETW/]+)\*\*", (references / "native-policy.md").read_text(), re.M)).replace("/", ""))
    observation = load(references / "capability-observation.json")
    require(observation["profile"] == "normal-mcp" and not observation["runtime_tested"] and not observation["account_checked"], "Capability observation cannot imply runtime/account acceptance")
    for recipe in recipes:
        identifier = recipe["id"]
        require(recipe["schema_version"] == 1 and recipe["version"] == "1.0.0", f"{identifier}: unsupported description schema/version")
        require(recipe["description_status"] == "described_not_accepted", f"{identifier}: descriptions are not accepted versions")
        require(recipe["reconciliation"]["legacy_sha256"] == digest(legacy[identifier].read_bytes()), f"{identifier}: stale legacy reconciliation")
        require(recipe["reconciliation"]["legacy_file"] == f"recipes/{identifier}.json", f"{identifier}: wrong legacy path")
        require(set(recipe["native"]["modes"]) <= modes_defined, f"{identifier}: unknown native policy mode")
        require(recipe["native"]["end_stop"] and "S" in recipe["native"]["end_stop"], f"{identifier}: missing stop contract")
        names = [item["name"] for item in recipe["inputs"]]
        require(len(names) == len(set(names)), f"{identifier}: duplicate input")
        require(recipe["reconciliation"]["required_input_changes"]["canonical"] == [{"name": item["name"], "requirement": item["requirement"]} for item in recipe["inputs"]], f"{identifier}: stale canonical input reconciliation")
        for item in recipe["inputs"]:
            require(item["requirement"] and item["description"] and item["type"] in {"text", "url", "ids"}, f"{identifier}: incomplete input")
        for text in [recipe["native"]["messages_text"], *(message["text"] for message in recipe["messages"])]:
            require(set(re.findall(r"\{([a-z_]+)\}", text)) <= set(names), f"{identifier}: undeclared message parameter")
        messages = {item["id"] for item in recipe["messages"]}
        require(len(messages) == len(recipe["messages"]), f"{identifier}: duplicate message")
        by_message = {item["id"]: item for item in recipe["messages"]}
        quoted = re.findall(r'"([^"\n]*)"', recipe["native"]["messages_text"])
        expected_initial = quoted[0] if quoted else ""
        if "CTA:" in recipe["native"]["messages_text"] or "Placement:" in recipe["native"]["messages_text"]:
            expected_initial = quoted[1] if len(quoted) > 1 else ""
        if identifier == "inro-4393":
            expected_initial = quoted[0]
        if identifier == "inro-comment-moderation":
            expected_initial = "{issue_prompt}"
        if identifier in {"inro-6082", "inro-6085"}:
            expected_initial = ""
        require(by_message["initial"]["text"] == expected_initial, f"{identifier}: contradictory initial template/native instruction")
        modes = set(recipe["native"]["modes"])
        if "D" in modes:
            require(by_message["continuation"]["text"] == recipe["native"]["messages_text"], f"{identifier}: contradictory continuation/native instruction")
        else:
            require(recipe["configuration"].get("continuation_reply_mode") == "DontReply", f"{identifier}: no-D mode requires DontReply")
            require("refusal_text" not in names, f"{identifier}: DontReply cannot require refusal copy")
            for name in ("refusal", "continuation", "handoff"):
                require(not by_message[name]["text"] and by_message[name]["availability"] == "not_sent", f"{identifier}: DontReply cannot send {name}")
        if recipe["native"]["difference"]:
            require(recipe["native"]["difference"] in recipe["source_differences"], f"{identifier}: contradictory source difference")
        route = recipe["route"]
        require(route["origin"] == "derived_native_instructions" and route["deterministic"] is False, f"{identifier}: route cannot claim source/runtime graph")
        nodes = {step["id"] for step in route["steps"]}
        require(len(nodes) == len(route["steps"]) and route["start"] in nodes, f"{identifier}: invalid route identity")
        for step in route["steps"]:
            require(step["provenance"]["origin"] == route["origin"] and step["action"], f"{identifier}: missing step provenance")
            require(set(step["message_ids"]) <= messages, f"{identifier}: dangling message reference")
        for edge in route["transitions"]:
            require(edge["from"] in nodes and edge["to"] in nodes and edge["condition"], f"{identifier}: dangling/empty transition")
            if "W" not in modes:
                require(not re.search(r"\b(waitlist|withdrawn)\b", edge["condition"], re.I), f"{identifier}: waitlist condition outside W mode")
        if "N" not in modes:
            entry = next(step for step in route["steps"] if step["id"] == route["start"])
            require(not re.search(r"contains-list|feedback term|for N\b", entry["action"], re.I), f"{identifier}: N-only entry outside N mode")
        if "D" not in modes:
            for step in route["steps"]:
                if step["id"] not in {route["start"], "first"}:
                    require(not step["message_ids"] and step.get("response_mode") == "silent", f"{identifier}: DontReply requires silent terminal steps")
                    require(not any(edge["from"] == step["id"] for edge in route["transitions"]), f"{identifier}: DontReply terminal cannot continue")
        reached = {route["start"]}
        while True:
            expanded = reached | {edge["to"] for edge in route["transitions"] if edge["from"] in reached}
            if reached == expanded:
                break
            reached = expanded
        require(reached == nodes, f"{identifier}: unreachable route step")
        if "Q" in recipe["native"]["modes"]:
            require({"consent", "question-one", "question-two", "qualified", "handoff"} <= nodes, f"{identifier}: incomplete qualification branches")
        if "W" in recipe["native"]["modes"]:
            require({"joined", "withdrawn"} <= nodes, f"{identifier}: incomplete membership branches")
        require(all(recipe["applicability"].get(key) for key in ("use_when", "prerequisites", "exclude_when")) and recipe["source_differences"], f"{identifier}: missing applicability/differences")
        require(all("The business requests:" not in text and "Expected outcome:" not in text for text in recipe["applicability"]["use_when"]), f"{identifier}: generic applicability")
        require(recipe["evidence"]["acceptance"]["status"] == "not_accepted", f"{identifier}: unqualified acceptance")
        require(recipe["evidence"]["canonical_version"]["status"] == "described_not_runtime_tested", f"{identifier}: canonical runtime evidence missing")
        require(all(key in recipe["lifecycle"] for key in ("checks", "return", "stop", "restart")), f"{identifier}: missing lifecycle")
    coverage = load(references / "source-coverage.json")
    records = coverage["records"]
    require(len(records) == 60 and len({row["source_id"] for row in records}) == 60, "Expected exactly 60 unique source mappings/gaps")
    require({row["source_id"] for row in records if row["source_id"].startswith("inro-")} == set(ids), "Inro coverage mismatch")
    require(sum(row["source_id"].startswith("manychat-") for row in records) == 30, "Manychat coverage mismatch")
    for row in records:
        require(row["reason"] and row["summary"] and row["differences"], f"{row['source_id']}: missing mapping rationale")
        require(row["recipe_id"] in ids if row["recipe_id"] else row["relationship"] == "explicit_gap", f"{row['source_id']}: unmapped source must be explicit gap")
        require(row["relationship"] in {"explicit_gap", "related_not_equivalent", "source_origin_not_equivalence", "business_replacement"}, "Unsupported mapping relationship")
    return recipes, coverage, observation


def recipe_section(recipe):
    native = recipe["native"]
    lines = [f"### {recipe['id']} | {recipe['title']}", f"Inputs: {native['inputs_text']}",
             f"Messages: {native['messages_text']}", f"Native: {'+'.join(native['modes'])}.",
             f"End/stop: {native['end_stop']}"]
    if native["difference"]:
        lines.append(f"Difference: {native['difference']}")
    return "\n".join(lines) + "\n"


def recipe_detail(recipe, coverage, policy):
    lines = [f"# {recipe['title']}", "", f"{recipe['id']} | v{recipe['version']} | described, not accepted.", "",
             "Read setup-policy.md and the selected setup-details/<variant>.md via setup-index.md before configuration. The historical native-policy modes below cannot bypass current variant gates. Recheck actual host tools/account before writes.", "",
             recipe_section(recipe), "## Applicability", *[f"- {text}" for text in recipe["applicability"]["use_when"]],
             "", "## Prerequisites", *[f"- {text}" for text in recipe["applicability"]["prerequisites"]],
             "", "## Exclusions", *[f"- {text}" for text in recipe["applicability"]["exclude_when"]], "", "## Inputs"]
    lines += [f"- `{item['name']}` ({item['type']}; {item['requirement']}): {item['description']}" for item in recipe["inputs"]]
    lines += ["", "## Available Templates And Instructions"]
    for message in recipe["messages"]:
        lines += [f"### {message['id']} ({message['kind']}; {message['availability']})", message["text"] or "No outgoing message supplied."]
    lines += ["", "## Intended Branches", "Derived from native instructions, not captured competitor graph or imported deterministic Flow."]
    for step in recipe["route"]["steps"]:
        lines += [f"### {step['id']}", step["action"]]
        lines += [f"- If {edge['condition']} -> {edge['to']}" for edge in recipe["route"]["transitions"] if edge["from"] == step["id"]]
    lines += ["", "## Settings And Operations", *[f"- {text}" for text in recipe["configuration"]["operations"]], recipe["configuration"]["normal_connector_gate"],
              "", "## Legacy Reconciliation", recipe["reconciliation"]["explanation"],
              f"Original goal: {recipe['reconciliation']['legacy_goal']}",
              f"Legacy status: {recipe['reconciliation']['legacy_status']}. Legacy digest: {recipe['reconciliation']['legacy_sha256']}.",
              "Legacy lists are audit evidence, not additional requirements for this analogue.",
              "", "## Lifecycle", recipe["lifecycle"]["return"], recipe["lifecycle"]["stop"], recipe["lifecycle"]["restart"],
              *[f"- Required check: {text}" for text in recipe["lifecycle"]["checks"]], "", "## Evidence"]
    lines += [f"- {key}: {json.dumps(value, ensure_ascii=False)}" for key, value in recipe["evidence"].items()]
    lines += ["", "## Selected Native Setting Instructions"]
    for letters, text in re.findall(r"^- \*\*([A-Z/]+)\*\*: (.+)$", policy, re.M):
        if set(letters.split("/")) & set(recipe["native"]["modes"]):
            lines += [f"### Mode {letters}", text]
    lines += ["", "## Related Sources", "These are mappings or losses, not runtime equivalence."]
    for row in coverage["records"]:
        if row["recipe_id"] == recipe["id"]:
            lines += [f"- {row['source_id']} ({row['relationship']}): {row['reason']}", *[f"  - {text}" for text in row["differences"]]]
    return "\n".join(lines) + "\n"


def outputs(references=REFERENCES):
    recipes, coverage, observation = read_library(references)
    index = {"schema_version": 1, "status": "described_not_accepted", "accepted_registry": "catalog.json", "source_count": len(coverage["records"]),
             "policy_sha256": digest((references / "native-policy.md").read_bytes()),
             "coverage_sha256": digest((references / "source-coverage.json").read_bytes()),
             "capability_sha256": digest((references / "capability-observation.json").read_bytes()),
             "recipes": [{"id": recipe["id"], "version": recipe["version"], "title": recipe["title"], "file": f"described-recipes/{recipe['id']}.json",
                          "native_file": f"native-recipes/{recipe['id']}.md", "sha256": digest((references / f"described-recipes/{recipe['id']}.json").read_bytes())} for recipe in recipes]}
    index_md = ["# Described Funnel Index", "", "30 business analogues; 60 sources mapped or explicitly missing. Zero accepted versions.",
                "Historical reference only. Read setup-index.md, setup-policy.md and the selected setup-details/<variant>.md first. Waiting/source-only decisions prohibit setup through these older recipes.",
                "The selected detail and viewer derive from the same described-recipes/<id>.json version.",
                "Do not run a helper, load all raw graphs or transfer user settings. Journal belongs to this conversation.",
                "No cross-chat recovery is promised. catalog.json is a separate accepted-version gate.", ""]
    index_md += [f"- [{recipe['title']}](native-recipes/{recipe['id']}.md) | {recipe['id']} | {'+'.join(recipe['native']['modes'])} | described, not accepted" for recipe in recipes]
    header = (references / "native-policy.md").read_text(encoding="utf-8").rstrip()
    result = {"described-index.json": json.dumps(index, ensure_ascii=False, indent=2) + "\n", "described-index.md": "\n".join(index_md) + "\n",
              "chatgpt-funnels.md": header + "\n\n" + "\n".join(recipe_section(recipe) for recipe in recipes)}
    result.update({f"native-recipes/{recipe['id']}.md": recipe_detail(recipe, coverage, header) for recipe in recipes})
    result.update(scenario_outputs(references, coverage, observation))
    scenarios = read_scenarios(references, coverage, observation)
    result.update(setup_outputs(references, scenarios, recipes, coverage, observation, continuation_prompts(scenarios)))
    return result


def generate(references=REFERENCES, check=False):
    expected = outputs(references)
    for name, text in expected.items():
        path = references / name
        if check:
            require(path.is_file() and path.read_text(encoding="utf-8") == text, f"Missing/stale generated reference: {name}; run funnel_library.py")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    require({path.name for path in (references / "native-recipes").glob("*.md")} == {Path(name).name for name in expected if name.startswith("native-recipes/")}, "Unexpected native recipe output")
    require({path.name for path in (references / "scenario-details").glob("*.md")} == {Path(name).name for name in expected if name.startswith("scenario-details/")}, "Unexpected scenario detail output")
    require({path.name for path in (references / "setup-details").glob("*.*")} == {Path(name).name for name in expected if name.startswith("setup-details/")}, "Unexpected setup detail output")
    return {"described_recipes": 30, "sources": 60, "generated_files": len(expected), "checked": check}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    print(json.dumps(generate(check=args.check)))
