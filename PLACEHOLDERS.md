# Placeholders to fill in before you advertise the site

Every unfinished value in the site is written as `[[TOKEN]]` and rendered in an
orange dashed box, so it is impossible to miss on the page. Find them all with:

```bash
grep -rn --include='*.html' -E '\[\[[A-Z ]+\]\]' .
```

Fill them in by editing the `.html` files directly (or, if you regenerate the
site, in `tools/build_site.py` — see the note at the bottom).

| Token | Appears in | What to put there |
|---|---|---|
| `[[PROGRAM DATES]]` | `index.html`, `apply.html` | e.g. `May 24 – July 31, 2027` |
| `[[YEAR]]` | `index.html` | The cohort year, e.g. `2027` |
| `[[APPLICATION OPENS]]` | `index.html`, `apply.html` | e.g. `November 1, 2026` |
| `[[APPLICATION DEADLINE]]` | `index.html`, `apply.html` | e.g. `February 15, 2027` |
| `[[DECISION DATE]]` | `apply.html` | e.g. `Mid-March 2027` |
| `[[GRAD YEAR CUTOFF]]` | `apply.html` | e.g. `You must not receive your bachelor's degree before August 2027.` |
| `[[ETAP LINK]]` | `apply.html` | Your program's ETAP opportunity URL. **This one is an `href`** — replace the whole attribute value, not just the visible text. |
| `[[WEBINAR DATES]]` | `apply.html`, `contact.html` | Dates and Zoom links for the virtual Q&A sessions |
| `[[PROGRAM EMAIL]]` | every page (footer) + `contact.html`, `faq.html` | A shared alias such as `remmmedies@auburn.edu` — not a personal address |
| `[[COORDINATOR NAME]]` | `contact.html` | Project coordinator's name |
| `[[AWARD NUMBER]]` | every page (footer) | NSF award number, once issued |

Two more values live outside the HTML:

- `sitemap.xml` and `robots.txt` both contain `REPLACE-WITH-YOUR-SITE-URL`.
  Set these to your published URL once you know it.
- `CNAME` (create it only if you use a custom domain) should contain the bare
  hostname, e.g. `reu.cm4.auburn.edu`.

## Making the check a hard failure

`.github/workflows/check-placeholders.yml` scans every push and reports leftover
tokens. It currently warns rather than failing. Once the site is live and all
tokens are filled in, change `exit 0` to `exit 1` in that file so a placeholder
can never reach the public site again.

## If you regenerate with the build script

`tools/build_site.py` rewrites all eight `.html` files from the page content
defined inside it. If you edit the `.html` files by hand and later run the
script, **your hand edits are overwritten.** Pick one workflow:

- **Edit the HTML directly** (simplest for small text changes) — and don't run
  the script again, or
- **Edit `tools/build_site.py`** and re-run it, so the shared header, nav and
  footer stay identical across pages.

The second is better if you expect to add pages or change navigation.
