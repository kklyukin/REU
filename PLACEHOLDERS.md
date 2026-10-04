# Placeholders — all filled in

No `[[TOKEN]]` placeholders remain. Verify any time with:

```bash
grep -rn --include='*.html' -E '\[\[[A-Z ]+\]\]' .
```

A match means something unfinished reached a page; it renders in an orange
dashed box, so it is also visible to the eye.

## Values in use

| What | Value |
|---|---|
| Applications open | October 1, 2026 |
| Information session | Friday, January 15, 2027 |
| Information session sign-up | https://auburn.qualtrics.com/jfe/form/SV_bDFC5hI9jSDScSy |
| Application deadline | February 8, 2027 |
| Decisions announced | Mid-March 2027 |
| Program dates | May 17 – July 23, 2027 |
| Graduation cutoff | Must not receive a bachelor's degree before August 2027 |
| NSF award number | 2548283 |
| ETAP | https://etap.nsf.gov/search |

Contact addresses live on the Contact page rather than in a single program
alias. Kuroda and Brown are listed; Klyukin and Miliordos still show only their
departments.

## Worth revisiting

- **ETAP link** points at the general ETAP search page. Once the REMMMEDIES
  opportunity is posted, swap in its direct URL so applicants are not left
  searching a list.
- **Program dates** disagree with the recruiting flyer, which says
  May 10 – July 24, 2027. The site's dates are exactly ten working weeks; the
  flyer's span eleven while the flyer also says "10-week experience."
- **"Mentors from two departments"** on the Home page and Research lede is not
  true of three of the eight projects (1, 5 and 7 pair mentors within one
  department). "Different research groups" would be accurate for all eight.

## Regenerating

`tools/build_site.py` rewrites all eight `.html` files from the page content
defined inside it. Hand edits to the `.html` files are overwritten when it runs,
so pick one workflow:

- **Edit the HTML directly** — and don't run the script again, or
- **Edit `tools/build_site.py`** and re-run it, so the shared header, nav and
  footer stay identical across pages.

The second is better for anything structural. The script needs only the Python
standard library:

```bash
python3 tools/build_site.py
```

It prints any remaining placeholders when it finishes.
