# Placeholders still to fill in

Already filled: program dates (May 17 – July 23, 2027), cohort year, application
opens/deadline, decision date, graduation cutoff, NSF award number (2548283),
project coordinator, the information-session date, and its Qualtrics sign-up link.

One remains. Find it with:

```bash
grep -rn --include='*.html' -E '\[\[[A-Z ]+\]\]' .
```

| Token | Appears in | What to put there |
|---|---|---|
| `[[ETAP LINK]]` | `apply.html` | The program's ETAP opportunity URL. **This one is an `href`** — replace the whole attribute value, not just the visible text. |

It renders in an orange dashed box on the page, so it cannot go live unnoticed.

Contact addresses are listed on the Contact page rather than in a single program alias.

## Making the check a hard failure

`.github/workflows/check-placeholders.yml` (not yet uploaded to GitHub) scans
every push for leftover tokens. It currently warns rather than failing. Once the
last two are filled, change `exit 0` to `exit 1` in that file.

## If you regenerate with the build script

`tools/build_site.py` rewrites all eight `.html` files from the page content
defined inside it. If you edit the `.html` files by hand and later run the
script, **your hand edits are overwritten.** Pick one workflow:

- **Edit the HTML directly** (simplest for small text changes) — and don't run
  the script again, or
- **Edit `tools/build_site.py`** and re-run it, so the shared header, nav and
  footer stay identical across pages.
