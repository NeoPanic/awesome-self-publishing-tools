#!/usr/bin/env python3
"""Build README.md from data/entries.json and data/meta.json."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
meta = json.loads((root / "data/meta.json").read_text(encoding="utf-8"))
entries = json.loads((root / "data/entries.json").read_text(encoding="utf-8"))
out = [meta["header"].rstrip(), "", "## Contents\n"]
for c in meta["categories"]:
    out.append(f"- [{c['title']}](#{c['anchor']})")
out += ["- [How to choose](#how-to-choose)", "- [Contributing](#contributing)", ""]
for c in meta["categories"]:
    out += [f"## {c['title']}\n", c["blurb"] + "\n"]
    for e in sorted([e for e in entries if e["category"] == c["id"]], key=lambda e: e["name"].lower()):
        out.append(f"- [{e['name']}]({e['url']}) `{e['price']}` - {e['description']} **Price:** {e['price_note']}")
    out.append("")
out.append(meta["footer"].rstrip())
(root / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("built", len(entries), "entries")
