# REMMMEDIES REU — program website

Static website for the **Research Experience in Multiscale Modeling of Matter
Embracing Disciplines in Engineering and Sciences (REMMMEDIES)** NSF REU Site,
hosted by the Center for Multiscale Modeling of Materials and Molecules (CM4)
at Auburn University.

Plain HTML and CSS. No framework, no build step in CI, no dependencies — GitHub
Pages serves the committed files directly. You can open `index.html` in a
browser locally and it works.

---

## Publishing it (about five minutes, no terminal required)

**1. Create the organization** (skip if it exists).
On github.com: your profile menu → *Your organizations* → *New organization* →
*Free*. Name it something durable like `cm4-auburn` — it becomes part of the
URL. Add Kuroda and Miliordos as owners so the site survives any one person's
account.

**2. Create the repository.**
In the organization: *New repository*. Name it `remmmedies-reu`, set it
**Public** (GitHub Pages needs public on the free plan), and do **not** add a
README, .gitignore, or license — this folder already has what it needs.

**3. Upload these files.**
On the empty repository page, click *uploading an existing file*. Drag in the
**contents** of this folder — every file and folder shown below, not the folder
itself. Commit to `main`.

> One gotcha: the browser upload silently skips dotfiles in some cases. After
> uploading, confirm that `.nojekyll` is listed in the repo. If it is missing,
> use *Add file → Create new file*, name it `.nojekyll`, leave it empty, commit.
> Without it GitHub may ignore files and folders beginning with an underscore.

**4. Turn on Pages.**
Repository *Settings* → *Pages* → **Source: Deploy from a branch** →
Branch `main`, folder `/ (root)` → *Save*. Wait a minute or two, then reload;
GitHub shows the live URL at the top of that page. It will be:

```
https://<org-name>.github.io/remmmedies-reu/
```

**5. Fill in the placeholders.**
See [`PLACEHOLDERS.md`](PLACEHOLDERS.md). Every unfinished value renders in an
orange dashed box on the page, so nothing can slip through unnoticed. Edit the
files right in GitHub's web editor (press `.` in the repo to open a full editor
in the browser) and commit — Pages redeploys automatically in under a minute.

---

## A custom domain (optional, recommended)

`cm4-auburn.github.io/remmmedies-reu` works, but a real hostname reads better
on a flyer and keeps working if you ever move hosts.

1. Ask Auburn IT for a CNAME record pointing e.g. `reu.cm4.auburn.edu` at
   `<org-name>.github.io`.
2. Add a file named `CNAME` at the repo root containing only the hostname:
   ```
   reu.cm4.auburn.edu
   ```
3. Settings → Pages → *Custom domain* → enter the same hostname → *Save*, then
   tick **Enforce HTTPS** once the certificate is issued (a few minutes).

A custom domain also makes `404.html` and root-relative links behave exactly as
they would on any normal site.

---

## What's in here

```
index.html          Home — hero, the pitch, at-a-glance figures, apply CTA
program.html        Boot camp, weeks 2–9, professional development, schedule
research.html       All eight research projects with mentors and methods
mentors.html        Program leadership and the ten faculty mentors
apply.html          Key dates, eligibility, selection criteria, how to apply
life.html           Stipend, housing, community, computing, code of conduct
faq.html            Twelve questions applicants actually ask
contact.html        Program email, leadership, info sessions, partner outreach
404.html            Self-contained not-found page
assets/css/site.css The whole design system — one file, commented
assets/img/         Favicon; put program photos here
tools/build_site.py Regenerates the eight pages from one source of truth
sitemap.xml         For search engines (update the URL after publishing)
robots.txt          Ditto
.nojekyll           Tells GitHub Pages to serve files as-is
PLACEHOLDERS.md     Every [[TOKEN]] and what belongs in it
```

## Editing content

For small text changes, edit the `.html` file directly in GitHub's web editor.

For anything structural — adding a page, changing the navigation, adding a
project — edit `tools/build_site.py` and run it, which rewrites all eight pages
so the shared header, nav, and footer stay identical:

```bash
python3 tools/build_site.py
```

It needs only the Python standard library. It also prints any remaining
placeholders when it finishes.

**Pick one workflow and stick to it.** Running the script overwrites hand edits
made to the HTML. See the note at the bottom of `PLACEHOLDERS.md`.

## Design

- **Type:** IBM Plex Serif (headings) / IBM Plex Sans (body) / IBM Plex Mono
  (data, units, labels), loaded from Google Fonts.
- **Color:** Auburn navy `#03244D` for structure, Auburn orange `#DD550C` for
  the two or three things meant to be clicked, cool neutrals everywhere else.
- **Dark mode** is supported via `prefers-color-scheme`; all colors are CSS
  custom properties defined at the top of `site.css`.
- **No JavaScript.** The FAQ uses native `<details>`; the nav is a scrollable
  strip. The site works with JS disabled and degrades gracefully on old
  browsers.

## Images

`assets/img/` currently holds only the favicon. The site reads fine without
photos, but it reads much better with them. Worth collecting:

| Where | What |
|---|---|
| Home hero | Campus, the Easley machine room, or a rendered materials visualization |
| `research.html` | One figure per project — ask each mentor, it's a two-line email |
| `mentors.html` | Headshots from the COSAM and Samuel Ginn directory pages |
| `life.html` | Campus, Toomer's Corner, Chewacla, the Jule Collins Smith Museum |

Use Auburn-owned or mentor-owned images. Give every one an `alt` attribute —
it's an accessibility requirement for a federally funded program.

## Maintenance rhythm

| When | What |
|---|---|
| Each September | Program dates, deadline, ETAP link |
| Each October | Confirm the project list with mentors |
| Each March | "Applications closed — check back in the fall" |
| Each August | Symposium photos, cohort photo, 2–3 participant quotes |

That last row matters more than any design decision. A page of last year's
students saying what they worked on will out-recruit everything else on the
site. Collect quotes and photo permissions during the final week, while
everyone is still on campus.

## After launch: where to list the site

The site is only half of recruiting. Submit it to:

- **NSF's REU Sites directory** — required, and by far the highest-traffic source
- **NSF ETAP** — the opportunity listing should link back here
- **Pathways to Science** (pathwaystoscience.org) — free, heavily used by
  students at PUIs and community colleges
- **Professional societies** — APS, ACS, MRS, SPS all maintain summer listings
- **Auburn** — COSAM, Samuel Ginn, the CM4 center page, the undergraduate
  research office
- **Partner institutions** — email advisors at the thirteen partner schools
  listed on the contact page

---

## Acknowledgment

This material is based upon work supported by the National Science Foundation
under Award No. `[[AWARD NUMBER]]`. Any opinions, findings, and conclusions or
recommendations expressed in this material are those of the author(s) and do
not necessarily reflect the views of the National Science Foundation.
