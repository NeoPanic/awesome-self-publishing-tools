#!/usr/bin/env python3
"""Report dead links and stale price checks. Always exits 0; the workflow opens an issue if there are findings."""
import json, pathlib, urllib.request, urllib.error, datetime
root = pathlib.Path(__file__).resolve().parent.parent
entries = json.loads((root / "data/entries.json").read_text(encoding="utf-8"))
today = datetime.date.today()
problems = []
for e in entries:
    try:
        req = urllib.request.Request(e["url"], headers={"User-Agent": "Mozilla/5.0 (list-link-check)"})
        urllib.request.urlopen(req, timeout=30)
    except urllib.error.HTTPError as ex:
        if ex.code not in (401, 403, 429):  # these usually mean bot protection, not a dead page
            problems.append(f"- {e['name']}: {e['url']} returned HTTP {ex.code}")
    except Exception as ex:
        problems.append(f"- {e['name']}: {e['url']} failed ({type(ex).__name__})")
    age = (today - datetime.date.fromisoformat(e["price_checked"])).days
    if age > 120:
        problems.append(f"- {e['name']}: price last checked {e['price_checked']} ({age} days ago), please re-verify")
print("Findings:\n\n" + "\n".join(problems) if problems else "All links OK and prices recently checked.")
