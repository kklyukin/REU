# Placeholders still to fill in

Already filled: program dates (May 17 – July 31, 2027), cohort year, application
opens/deadline, decision date, graduation cutoff, NSF award number (2548283),
project coordinator, and the pre-program Q&A date.

Two remain. Find them with:

```bash
grep -rn --include='*.html' -E '\[\[[A-Z ]+\]\]' .
```

| Token | Appears in | What to put there |
|---|---|---|
| `[[ETAP LINK]]` | `apply.html` | The program's ETAP opportunity URL. **This one is an `href`** — replace the whole attribute value, not just the visible text. |
| `[[PROGRAM EMAIL]]` | every page (footer) + `contact.html`, `faq.html` | A shared alias such as `remmmedies@auburn.edu`. Use a shared mailbox, not a personal address — this outlives any one person's role. |

Both render in an orange dashed box on the page, so they cannot go live unnoticed.

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
