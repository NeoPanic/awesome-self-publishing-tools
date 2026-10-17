# Contributing

This list only works if every entry is real and every price is honest.

## What gets in

1. The tool exists and is usable today. No "coming soon", no abandoned products.
2. It helps self-published authors or small publishers.
3. Pricing comes **from the tool's own current page**. Add the page to `price_note` wording ("per their pricing page").
4. No affiliate links, no tracking links. Link to the tool's official page or repo.
5. Owners may add their own tool. Mark it "(by the maintainer)" or "(by the author)" in the name. Same rules apply.
6. GitHub projects must be public, not archived, licensed and committed to within 12 months.

## Price labels

`free` (no cost), `freemium` (free tier plus paid), `paid` (you pay; trial allowed), `revenue-share` (platform keeps a cut of sales). If a tool fits two, pick the one that describes what a typical author pays, and explain in `price_note`.

## How to add a tool

1. Fork the repo.
2. Add one object to `data/entries.json`:
   ```json
   {
     "category": "write",
     "name": "Tool name",
     "url": "https://official.page/",
     "price": "freemium",
     "price_note": "What the free tier gives and what paid costs, from their page.",
     "description": "One plain sentence.",
     "price_checked": "YYYY-MM-DD"
   }
   ```
   Categories: `write`, `edit`, `format`, `design`, `dist`, `audio`, `research`, `market`, `direct`, `oss`.
3. Run `python scripts/build_readme.py`. Do not edit `README.md` by hand.
4. Add a line to `CHANGELOG.md` and open a pull request with the template.

## Writing style

Plain words. Say what it does. No "best" or "powerful". If something is unverified, say so or leave it out.

## Keeping it fresh

A weekly GitHub Action checks links and opens an issue for dead pages and prices not re-checked in 120 days. Fix these by re-reading the page and updating `price_note` and `price_checked`.
