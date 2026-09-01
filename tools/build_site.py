#!/usr/bin/env python3
"""
Build the REMMMEDIES REU static site.

Regenerates every .html file in the repository root from the page content
defined below, so the shared header, nav, and footer stay identical across
pages. Run from the repository root:

    python3 tools/build_site.py

Requires only the Python standard library. No dependencies, no node, no build
step in CI -- the committed .html files are what GitHub Pages serves.
"""

import os
import re
import sys

SITE_NAME = "REMMMEDIES"
TAGLINE = "NSF REU Site · CM4 · Auburn University"

PAGES = [
    ("index.html",    "home",     "Home",              "REMMMEDIES REU at Auburn University",
     "A paid 10-week NSF REU in computational modeling of materials and molecules at Auburn University. $6,365 stipend, housing, meals and travel. No programming experience required."),
    ("program.html",  "program",  "The Program",       "The Program",
     "Ten weeks: a week-long boot camp in simulation methods, eight weeks of mentored research at two scales, and a closing research symposium."),
    ("research.html", "research", "Research Projects", "Research Projects",
     "Eight active research projects in 2D materials, catalysis, quantum materials, dusty plasmas, molecular interactions and viral capsids."),
    ("mentors.html",  "mentors",  "Mentors",           "Mentors",
     "Faculty mentors from Physics, Chemistry, Materials Engineering, Chemical Engineering and Statistics at Auburn University."),
    ("apply.html",    "apply",    "Apply",             "Apply",
     "Eligibility, selection criteria, key dates and how to apply through NSF ETAP."),
    ("life.html",     "life",     "Life at Auburn",    "Life at Auburn",
     "Stipend, housing, meals, travel, computing resources and community life during the ten weeks."),
    ("faq.html",      "faq",      "FAQ",               "Frequently Asked Questions",
     "Answers to the questions we get most often about eligibility, experience required, matching, and the summer itself."),
    ("contact.html",  "contact",  "Contact",           "Contact",
     "How to reach the program leadership, information sessions, and partnership information for faculty and advisors."),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · REMMMEDIES REU</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} · REMMMEDIES REU">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#03244D">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;600;700&display=swap">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="mast">
  <div class="mast-inner">
    <a class="brand" href="index.html">
      <span class="mark">{site}</span>
      <span class="sub">{tagline}</span>
    </a>
    <nav class="tabs" aria-label="Main">
{nav}
    </nav>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="site">
  <div class="wrap">
    <p class="ack">This material is based upon work supported by the National Science Foundation under Award No. <span class="ph">[[AWARD NUMBER]]</span>. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.</p>
    <p>Auburn University is an equal opportunity educational institution/employer.</p>
    <p>Center for Multiscale Modeling of Materials and Molecules (CM4) · Auburn University · Auburn, AL 36849 · <span class="ph">[[PROGRAM EMAIL]]</span></p>
  </div>
</footer>
</body>
</html>
"""


def nav_html(current):
    out = []
    for fname, key, label, _t, _d in PAGES:
        cur = ' aria-current="page"' if key == current else ""
        out.append(f'      <a href="{fname}"{cur}>{label}</a>')
    return "\n".join(out)


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------

HOME = """
<div class="hero">
  <div class="hero-inner">
    <div>
      <p class="eyebrow">Summer research · Auburn University</p>
      <h1>Model matter,<br>atom to bulk.</h1>
      <p class="tag">A paid 10-week research experience in computational modeling of materials and molecules — for undergraduates who want to do this and don't have the chance at home.</p>
      <p class="factline">
        <span class="ph">[[PROGRAM DATES]]</span>
        <span>$6,365 stipend</span>
        <span>Housing + meals + travel</span>
        <span>No programming experience required</span>
      </p>
      <p class="cta-row">
        <a class="btn btn-primary" href="apply.html">Apply on NSF ETAP</a>
        <a class="btn btn-ghost" href="research.html">Explore research projects</a>
      </p>
    </div>
    <div class="ladder">
      <p class="cap">What &ldquo;multiscale&rdquo; means here</p>
      <div class="rung"><span class="u">10<sup>&minus;10</sup> m</span><span class="m">Electrons and bonds<em>DFT · Hartree&ndash;Fock</em></span></div>
      <div class="rung"><span class="u">10<sup>&minus;9</sup> m</span><span class="m">Atoms in motion<em>Molecular dynamics · Monte Carlo</em></span></div>
      <div class="rung"><span class="u">10<sup>&minus;8</sup> m</span><span class="m">Proteins and assemblies<em>Coarse-grained models</em></span></div>
      <div class="rung"><span class="u">10<sup>&minus;6</sup> m</span><span class="m">Grains, particles, plasmas<em>Statistical analysis</em></span></div>
      <div class="rung"><span class="u">10<sup>&minus;3</sup> m</span><span class="m">Bulk response<em>Finite element analysis</em></span></div>
    </div>
  </div>
</div>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">The short version</p>
    <h2 class="sec">Ten students. Ten weeks. Real computational research.</h2>
    <div class="narrow stack">
      <p>Every summer, ten undergraduates come to Auburn to spend ten weeks doing computational research — simulating how matter behaves, from single atoms to bulk materials.</p>
      <p>You will not be fetching coffee or reading papers in a corner. You will be running quantum chemistry calculations, molecular dynamics simulations, and machine-learning workflows on some of the largest computers in the Southeast, on a live research problem, with a faculty mentor and a graduate-student mentor who meet with you every week.</p>
      <p>The program is hosted by the <strong>Center for Multiscale Modeling of Materials and Molecules (CM4)</strong> and brings together faculty from Physics, Chemistry and Biochemistry, Materials Engineering, Chemical Engineering, and Statistics.</p>
    </div>
    <div class="callout warm narrow">
      <p><strong>We especially encourage applications from students at community colleges, primarily undergraduate institutions, and any school where research opportunities are hard to come by.</strong></p>
    </div>
  </div>
</section>

<section class="band tint">
  <div class="wrap">
    <div class="grid g4">
      <div class="stat"><span class="n">10</span><span class="l">weeks on the Auburn campus, <span class="ph">[[PROGRAM DATES]]</span></span></div>
      <div class="stat"><span class="n">$6,365</span><span class="l">stipend, plus housing, meals, and travel reimbursement</span></div>
      <div class="stat"><span class="n">10</span><span class="l">students in the cohort, most from outside Auburn</span></div>
      <div class="stat"><span class="n">8</span><span class="l">research projects across five departments</span></div>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Why this one</p>
    <h2 class="sec">What makes this REU different</h2>
    <div class="grid g2">
      <div class="point">
        <h3>You start with a boot camp, not a blank terminal</h3>
        <p>Week 1 is a hands-on tour of the whole toolkit: AI foundation models for materials, density functional theory, molecular dynamics, finite element analysis, and materials informatics in Python — plus Linux and submitting jobs to a supercomputer. Every faculty mentor teaches a piece of it.</p>
      </div>
      <div class="point">
        <h3>You work in a pair, at two different scales</h3>
        <p>Two students take one scientific problem from two directions — one running atom-level quantum calculations, the other working at the molecular or continuum scale. You meet with your partner and both mentors every other week to compare what the two views tell you.</p>
      </div>
      <div class="point">
        <h3>You get two mentors</h3>
        <p>A faculty mentor you meet with at least weekly, and a graduate student in the group as a near-peer mentor for day-to-day tutorials, troubleshooting, and feedback — often more approachable than faculty alone.</p>
      </div>
      <div class="point">
        <h3>Your work doesn't stop in August</h3>
        <p>The program closes with the CM4 research symposium. After that we support publication — in indexed journals or Auburn's undergraduate research journal — and fund travel for students presenting at conferences.</p>
      </div>
    </div>
  </div>
</section>

<section class="ctaband">
  <div class="wrap stack">
    <h2>Applications for Summer <span class="ph">[[YEAR]]</span></h2>
    <p>Open <span class="ph">[[APPLICATION OPENS]]</span> · Close <span class="ph">[[APPLICATION DEADLINE]]</span> · Apply through NSF ETAP</p>
    <p><a class="btn btn-primary" href="apply.html">Start your application</a></p>
  </div>
</section>
"""

PROGRAM = """
<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">The program</p>
    <h1 class="sec">Ten weeks, and how they're spent</h1>
    <p class="lede">Ten weeks is not long. You spend the first getting fluent with the tools, the next eight doing research, and the last one presenting it.</p>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">Week 1</p>
    <h2 class="sec">The boot camp</h2>
    <p class="lede">Before you touch a research problem, you get a working tour of the methods used to model matter at every scale. Each faculty mentor gives an introductory lecture and leads a half-day hands-on workshop on their technique — including what it can and cannot tell you.</p>
    <div class="grid g2">
      <div class="proj"><p class="num">DAY 1</p><h3>Orientation and AI foundation models</h3><p class="d">Getting set up, meeting the cohort, and starting with foundation models trained on chemical and materials data (such as Meta FAIR's UMA) — exploring structure&ndash;property relationships and reaction energetics before the more rigorous methods.</p></div>
      <div class="proj"><p class="num">DAY 2</p><h3>Electronic structure</h3><p class="d">Density functional theory and Hartree&ndash;Fock via the MIT Atomic-Scale Modeling Toolkit. How electrons determine structure, bonding, and reaction mechanisms.</p></div>
      <div class="proj"><p class="num">DAY 3</p><h3>Molecular dynamics and Monte Carlo</h3><p class="d">Using the MIT Atomic-Scale Modeling Toolkit and NAMD to follow atoms through time, and to connect interatomic forces to ensemble-average properties.</p></div>
      <div class="proj"><p class="num">DAY 4</p><h3>Finite element analysis</h3><p class="d">Using OOF2 to model how real materials and structures respond to stress, heat, and vibration at macroscopic scales.</p></div>
      <div class="proj"><p class="num">DAY 5</p><h3>Materials informatics</h3><p class="d">Jupyter notebooks, data science for materials and chemistry, and how data-driven insight can point quantum chemistry and molecular dynamics in new directions.</p></div>
      <div class="proj"><p class="num">ALL WEEK</p><h3>High-performance computing</h3><p class="d">Linux environments, moving data, submitting and monitoring jobs, parallel computing, and benchmarking on Auburn's Easley cluster and the Alabama Supercomputer Authority systems.</p></div>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Weeks 2&ndash;9</p>
    <h2 class="sec">Your research project</h2>
    <p class="lede">You rank your top three projects in your application, and we match you on interests, background, and what each project needs.</p>
    <ul class="tick">
      <li><strong>Weekly</strong> one-on-one meeting with your faculty mentor.</li>
      <li><strong>Daily</strong> access to a graduate-student near-peer mentor for tutorials, debugging, and feedback.</li>
      <li><strong>Every other week</strong>, a joint meeting with your project partner and both mentors to compare results across scales.</li>
      <li><strong>Tuesday mornings</strong>, professional development workshops.</li>
      <li><strong>Every other week</strong>, a social or cultural activity with the cohort and mentors.</li>
    </ul>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">Beyond the bench</p>
    <h2 class="sec">Professional development</h2>
    <div class="grid g3">
      <div class="point"><h3>Writing and literature</h3><p>Literature searches, synthesizing sources, ethical source use, and writing abstracts and grant text — led by specialists from Auburn's Miller Writing Center.</p></div>
      <div class="point"><h3>Communication</h3><p>Effective presentations, poster design, and the &ldquo;3-minute research story&rdquo; — our version of the 3-Minute Thesis, for a non-specialist audience.</p></div>
      <div class="point"><h3>Careers</h3><p>Résumés, interviews, personal statements, and round tables on graduate school and STEM careers with faculty and graduate students.</p></div>
      <div class="point"><h3>MatSci Data Tournament</h3><p>Teams of 2&ndash;3 take a messy materials dataset — missing values, outliers and all — build a predictive model, and present the result.</p></div>
      <div class="point"><h3>Self-driving laboratory</h3><p>Hands-on work with a prototype autonomous lab closing the loop between AI, simulation, and robotics, plus a tour of the National Center for Additive Manufacturing Excellence.</p></div>
      <div class="point"><h3>Facility tours</h3><p>The Auburn HPC data center — power, GPUs, infrastructure cost, cybersecurity — and research labs across Physics, Chemistry, and Engineering.</p></div>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Representative schedule</p>
    <h2 class="sec">The ten weeks</h2>
    <div class="tablewrap">
      <table>
        <caption class="visually-hidden">Week-by-week schedule of research, professional development and community activities</caption>
        <thead><tr><th scope="col">Week</th><th scope="col">Research</th><th scope="col">Professional development</th><th scope="col">Community</th></tr></thead>
        <tbody>
          <tr><td class="wk">0</td><td>Pre-arrival materials from your mentor</td><td>Optional virtual Q&amp;A</td><td>&mdash;</td></tr>
          <tr><td class="wk">1</td><td>Orientation; intro to coding; HPC</td><td>Code of conduct</td><td>Welcome</td></tr>
          <tr><td class="wk">2</td><td>Job submission, parallel computing</td><td>Workshop</td><td>Cookout</td></tr>
          <tr><td class="wk">3</td><td>Methods training</td><td>Workshop</td><td>&mdash;</td></tr>
          <tr><td class="wk">4</td><td>Visualizing data; HPC facility visit</td><td>Workshop</td><td>Jule Collins Smith Museum</td></tr>
          <tr><td class="wk">5</td><td>Coding tournament</td><td>Searching the literature</td><td>Chewacla State Park hike</td></tr>
          <tr><td class="wk">6</td><td>Comparing methods across scales</td><td>Effective presentations</td><td>Star gazing</td></tr>
          <tr><td class="wk">7</td><td>3-minute research story</td><td>Careers in STEM</td><td>&mdash;</td></tr>
          <tr><td class="wk">8</td><td>Big data; HPC</td><td>Résumés and interviews</td><td>Movie night</td></tr>
          <tr><td class="wk">9</td><td>Hackathon</td><td>Post-graduation round table</td><td>CM4 trivia night</td></tr>
          <tr><td class="wk">10</td><td>REU symposium</td><td>&mdash;</td><td>Farewell</td></tr>
        </tbody>
      </table>
    </div>
    <p class="fineprint">Representative; exact activities vary year to year.</p>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">Afterward</p>
    <h2 class="sec">Publish, present, stay in touch</h2>
    <div class="grid g3">
      <div class="point"><h3>Publish</h3><p>With your mentor, in an indexed journal or in the Auburn University Journal of Undergraduate Scholarship, which publishes original undergraduate research in any discipline.</p></div>
      <div class="point"><h3>Present</h3><p>Partial travel funding for participants presenting at local, regional, or national conferences — where you also serve as an ambassador for the program.</p></div>
      <div class="point"><h3>Stay in touch</h3><p>We follow up with alumni to hear where the experience took them, and what we should change.</p></div>
    </div>
  </div>
</section>
"""

PROJECTS = [
    ("01", "Atomic and molecular separation using 2D-material membranes",
     "Dr. Marcelo Kuroda (Physics) · Dr. Rafael Bernardi (Physics)",
     "DFT · Steered molecular dynamics · AI-assisted trajectory analysis",
     "Two-dimensional materials make promising separation membranes: atomically thin, enormous surface-to-volume ratio, and pore edges you can chemically tailor to grab specific molecules. Which molecules a pore lets through depends on its size, geometry, and termination — exactly what simulation predicts well, and exactly what an experimentalist needs before fabricating anything.",
     "analyze how pore geometry and functionalization set selectivity using DFT, and characterize molecular and ionic capture in nanopores with atomistic steered molecular dynamics in gas and liquid."),
    ("02", "Chemical reactions on molecular and heterogeneous catalysts",
     "Dr. Evangelos Miliordos (Chemistry) · Dr. Konstantin Klyukin (Materials Engineering)",
     "Gas-phase quantum chemistry · Periodic DFT",
     "Electrides are materials whose electrons belong to no particular atom. Our groups proposed a new kind — solvated electron precursor electrides — where molecules carrying diffuse electrons are anchored to a metal or insulator surface, giving far more control over where those electrons sit. That control is what makes them interesting for catalysis and quantum computing.",
     "run gas-phase calculations of catalyzed transformations, then the same reactions with the catalyst anchored to a metal and to an insulator — learning both the isolated-molecule and periodic-boundary toolkits."),
    ("03", "Quantum properties of molecular lattices",
     "Dr. Marcelo Kuroda (Physics) · Dr. Yinong Zhou (Physics) · Dr. Roberto Molinari (Statistics)",
     "DFT · Electronic structure modeling · Structure&ndash;property analysis",
     "Nature does not supply many materials with the quantum properties we want, so researchers build them — arranging individual atoms and molecules on surfaces into artificial lattices. The number of possible combinations explodes, which makes the structure&ndash;property relationship the bottleneck for discovery.",
     "study atoms and molecules on surfaces with DFT, assess how deposited elements couple into quantum phases, and catalog component properties against the relationships that emerge."),
    ("04", "Discovery of functional 2D materials",
     "Dr. Konstantin Klyukin (Materials Engineering) · Dr. Jianjun Dong (Physics)",
     "Database screening · Algorithm development · Periodic DFT · AI foundation models",
     "2D materials could reshape electronics and energy technology — but only the ones we can actually make. This project asks which new 2D materials could be produced by selectively etching specific elements out of layered 3D phases, combining materials informatics with quantum chemistry across two groups.",
     "screen materials databases, adapt algorithms to find layered structures with intercalated cations, and calculate extraction and exfoliation energies to judge synthesizability."),
    ("05", "Phase transitions and pattern formation in dusty plasmas",
     "Dr. Evdokiya Kostadinova (Physics) · Dr. Marcelo Kuroda (Physics)",
     "Statistical analysis of ISS experiments · MD with anisotropic potentials",
     "A dusty plasma — charged micron-sized particles suspended in low-temperature plasma — is big enough to watch particle by particle, yet it self-assembles, layers, and forms patterns that look strikingly like liquid-crystal phase transitions. That makes it a macroscopic analogue for studying universality and critical behavior.",
     "analyze experiments performed in the Plasmakristall-4 facility aboard the International Space Station, and run molecular dynamics with anisotropic potentials to reproduce the structures observed."),
    ("06", "Leveraging big data for noncovalent energy descriptors",
     "Dr. Konrad Patkowski (Chemistry) · Dr. Nedret Billor (Statistics)",
     "Data mining · Interaction energy decomposition · Classification",
     "Weak interactions between molecules determine the properties of clusters, liquids, solids, and biomolecular assemblies — and chemists describe them with fuzzy categories: hydrogen-bonded, halogen-bonded, &pi;-stacked. This project uses the open-source QCArchive database to translate those labels into quantitative energy components.",
     "program data-mining workflows against QCArchive, partition interaction energies into electrostatic, exchange, induction, and dispersion parts, and automate classification of complexes."),
    ("07", "Solvent effects in solvatochromic shift predictions",
     "Dr. Filip Pawlowski (Chemistry) · Dr. Paul Ohno (Chemistry)",
     "DFT with implicit solvation (PCM) · Explicit solvation · MD",
     "Solvatochromic molecules shift the wavelengths they absorb and emit depending on their local environment, which makes them useful probes for the phase state of aerosol particles as humidity changes. Predicting those shifts means deciding how much solvent you can afford to model explicitly — the central accuracy-versus-cost question in solvation modeling.",
     "compute spectra with a polarizable continuum, then with the first solvation shell explicit, then fully explicit at the MD level — comparing all three against experiment."),
    ("08", "Ultra-coarse-grained models for protein interactions in viral capsids",
     "Dr. Michael Howard (Chemical Engineering) · Dr. Rafael Bernardi (Physics)",
     "Atomistic MD · Coarse-grained model construction · Validation",
     "A viral capsid is a protein shell that assembles itself around a virus's genetic material — central to the viral life cycle, and therefore a drug target. It is hard to watch experimentally and too large for atomistic simulation, which leaves coarse-graining. Our group recently developed a way to approximate the anisotropic interactions between proteins from limited data.",
     "run atomistic MD of capsid proteins from satellite tobacco mosaic virus to generate training data, build ultra-coarse-grained models from it, and test and validate them."),
]


def projects_page():
    cards = []
    for num, title, who, meth, body, doing in PROJECTS:
        cards.append(f"""      <article class="proj">
        <p class="num">PROJECT {num}</p>
        <h3>{title}</h3>
        <p class="who">{who}</p>
        <p class="meth">{meth}</p>
        <p class="d">{body}</p>
        <p class="d"><strong>You will</strong> {doing}</p>
      </article>""")
    return """
<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Research projects</p>
    <h1 class="sec">Eight problems, each taken at two scales</h1>
    <p class="lede">Every project below is an active research problem, tackled by a pair of students working at different scales with mentors from different departments. You do not need to have done any of this before — projects are scoped for students just starting in computational work as well as those with experience.</p>
    <div class="callout"><p><strong>In your application, rank your top three.</strong> We match you on your preferences, your background, and the fit between your interests and each project's methods.</p></div>
  </div>
</section>

<section class="band tint">
  <div class="wrap">
    <div class="grid g2">
""" + "\n".join(cards) + """
    </div>
    <p class="fineprint">Project availability varies by year with mentor availability and the interests of the incoming cohort.</p>
  </div>
</section>
"""


FACULTY = [
    ("RB", "Dr. Rafael Bernardi", "Associate Professor of Physics",
     "Co-investigator at the NIH Center for Macromolecular Modeling and Visualization — home of NAMD and VMD. Studies protein mechanics and protein complexes under mechanical load."),
    ("NB", "Dr. Nedret Billor", "Professor; Director of Statistics and Data Science Programs",
     "Robust multivariate and functional data analysis, data science education, statistical theory, and outlier detection."),
    ("JD", "Dr. Jianjun Dong", "Professor of Physics",
     "Atomistic simulations of the structure and properties of complex solids, with recent emphasis on thermal transport."),
    ("MH", "Dr. Michael Howard", "Assistant Professor of Chemical Engineering",
     "Simulation and statistical mechanics for soft materials, focusing on nonequilibrium problems where thermodynamics and transport set structure&ndash;property relationships."),
    ("EK", "Dr. Evdokiya Kostadinova", "Assistant Professor of Physics",
     "Anomalous diffusion in disordered media, self-organization and stability of dusty plasmas, and the thermodynamics of driven-dissipative systems."),
    ("RM", "Dr. Roberto Molinari", "Assistant Professor, Mathematics and Statistics",
     "Methods and algorithms for computing models efficiently on big data while preserving interpretability and statistical inference."),
    ("PO", "Dr. Paul Ohno", "Assistant Professor of Chemistry and Biochemistry",
     "Develops and applies linear and nonlinear spectroscopic techniques to characterize interfacial and aerosol chemical systems."),
    ("KP", "Dr. Konrad Patkowski", "Professor; Graduate Program Officer, Chemistry and Biochemistry",
     "Co-author of the open-source quantum chemistry program Psi4. Accurate calculations of noncovalent interaction energies — method development and applications."),
    ("FP", "Dr. Filip Pawlowski", "Assistant Professor of Chemistry and Biochemistry",
     "Method development in quantum chemistry: coupled cluster and perturbation theories, response function theory, and applications."),
    ("YZ", "Dr. Yinong Zhou", "Assistant Professor of Physics",
     "Combines DFT with theoretical models to design and predict nanomaterials and quantum materials — electronic, topological, magnetic, optical, and phononic properties."),
]


def person(initials, name, role, bio):
    return f"""        <div class="person">
          <span class="avatar" aria-hidden="true">{initials}</span>
          <span class="pbody"><span class="nm">{name}</span><span class="rl">{role}</span><span class="bi">{bio}</span></span>
        </div>"""


def mentors_page():
    half = 5
    col1 = "\n".join(person(*f) for f in FACULTY[:half])
    col2 = "\n".join(person(*f) for f in FACULTY[half:])
    return f"""
<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Mentors</p>
    <h1 class="sec">Five departments, two colleges</h1>
    <p class="lede">Our mentors come from the College of Sciences and Mathematics and the Samuel Ginn College of Engineering. Together they have mentored more than 70 undergraduate researchers — over 25 of whom presented at conferences, more than 15 were authors on publications, and more than 25 went on to graduate school.</p>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">Program leadership</p>
    <div class="grid g3">
      <div class="lead-card">
        <p class="nm">Dr. Marcelo A. Kuroda</p>
        <p class="role">Principal Investigator</p>
        <p class="bi">Associate Professor of Physics. Theoretical and computational condensed matter and materials physics, from large-scale first-principles calculations to analytical models. Most Outstanding Professor, Society of Physics Students (2015).</p>
      </div>
      <div class="lead-card">
        <p class="nm">Dr. Konstantin Klyukin</p>
        <p class="role">Co-Principal Investigator</p>
        <p class="bi">Assistant Professor of Materials Engineering. Connects ab initio simulation with machine learning to understand atomic-scale processes at materials interfaces. AU Outstanding Faculty Member 2024 for excellence in undergraduate teaching.</p>
      </div>
      <div class="lead-card">
        <p class="nm">Dr. Evangelos Miliordos</p>
        <p class="role">Senior Investigator</p>
        <p class="bi">J. E. Land Associate Professor, Chemistry and Biochemistry. Quantum chemical calculations on transition metal compounds and systems with solvated electrons.</p>
      </div>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Faculty mentors</p>
    <h2 class="sec">Who you could work with</h2>
    <div class="grid g2">
      <div class="peoplecol">
{col1}
      </div>
      <div class="peoplecol">
{col2}
      </div>
    </div>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack narrow">
    <p class="eyebrow">Near-peer mentoring</p>
    <h2 class="sec">Graduate mentors</h2>
    <p>Every REU student also works with a graduate student in their mentor's research group. Near-peer mentors give step-by-step tutorials, troubleshoot problems as they come up, and provide continuous feedback — often in ways that are more approachable than working with faculty alone.</p>
  </div>
</section>
"""


APPLY = """
<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Apply</p>
    <h1 class="sec">Key dates</h1>
    <div class="kv">
      <div><span class="k">Applications open</span><span class="v ph">[[APPLICATION OPENS]]</span></div>
      <div><span class="k">Application deadline</span><span class="v ph">[[APPLICATION DEADLINE]]</span></div>
      <div><span class="k">Decisions announced</span><span class="v ph">[[DECISION DATE]]</span></div>
      <div><span class="k">Program dates</span><span class="v ph">[[PROGRAM DATES]]</span></div>
    </div>
    <p><a class="btn btn-primary" href="[[ETAP LINK]]">Apply on NSF ETAP</a></p>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">Eligibility</p>
    <h2 class="sec">Check these three things first</h2>
    <ul class="tick">
      <li>You are a <strong>U.S. citizen, U.S. national, or permanent resident</strong>. This is an NSF requirement and we cannot make exceptions.</li>
      <li>You are <strong>enrolled in a degree program</strong> — full-time or part-time — leading to an associate's or bachelor's degree, when you apply and through the summer.</li>
      <li>You will <strong>not graduate before the program ends</strong>. <span class="ph">[[GRAD YEAR CUTOFF]]</span> Students who already hold a bachelor's degree are not eligible.</li>
    </ul>
    <div class="callout narrow">
      <p><strong>Programming experience is preferred but not required.</strong> Familiarity with Python, C++, or MATLAB helps, but we design projects for students just starting in computational work as well as those with experience. If you have never used a command line, you are still a plausible applicant — that is what Week 1 is for.</p>
    </div>
    <p class="narrow">We also expect a <strong>minimum GPA of 3.0</strong> in a STEM major — physics, chemistry, materials science, chemical engineering, mathematics, statistics, computer science, or a related field.</p>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Selection</p>
    <h2 class="sec">What we look for</h2>
    <p class="lede">We read applications holistically. No single number decides anything.</p>
    <div class="grid g2">
      <div class="stack">
        <h3 class="sub">Primary criteria</h3>
        <ul class="clean">
          <li><strong>Academic performance</strong> — a strong record in relevant coursework.</li>
          <li><strong>Computational skills</strong> — any familiarity with programming languages and tools, though not required.</li>
          <li><strong>Research interest</strong> — shown through coursework, prior experience, or extracurricular activities.</li>
          <li><strong>Communication</strong> — written and oral, as evidenced by essays, proposals, or past presentations.</li>
          <li><strong>Potential for success</strong> — intellectual curiosity, problem-solving, and willingness to learn.</li>
        </ul>
      </div>
      <div class="stack">
        <h3 class="sub">Secondary criteria</h3>
        <ul class="clean">
          <li><strong>Your institution</strong> — we build the cohort from a wide range of schools. At least half of our participants come from institutions where research opportunities are limited.</li>
          <li><strong>Letters of recommendation</strong> — from faculty who can speak to your abilities and research potential.</li>
          <li><strong>Engagement in STEM</strong> — service, outreach, or student organizations.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">Process</p>
    <h2 class="sec">How to apply</h2>
    <div class="grid g2">
      <div class="proj"><p class="num">STEP 1</p><h3>Prepare your materials</h3><p class="d">Academic transcript (unofficial is fine), a personal statement, your top three project preferences, and one or two faculty letters of recommendation.</p></div>
      <div class="proj"><p class="num">STEP 2</p><h3>Submit through NSF ETAP</h3><p class="d">All applications go through the NSF Education and Training Application. Create an account, find our program, and complete the application there. Do not email materials to us directly.</p></div>
      <div class="proj"><p class="num">STEP 3</p><h3>Ask your recommenders early</h3><p class="d">Letters are submitted through ETAP. Give your faculty at least three weeks' notice.</p></div>
      <div class="proj"><p class="num">STEP 4</p><h3>Come to a Q&amp;A</h3><p class="d">We run virtual information sessions during the application window (<span class="ph">[[WEBINAR DATES]]</span>). Bring any question. No preparation needed.</p></div>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack narrow">
    <p class="eyebrow">From the people who read them</p>
    <h2 class="sec">Advice on your personal statement</h2>
    <ul class="clean">
      <li><strong>Be specific about the projects.</strong> &ldquo;I am interested in materials science&rdquo; tells us less than a paragraph on why selective etching of layered phases caught your attention.</li>
      <li><strong>Inexperience is not a disqualifier — and pretending isn't necessary.</strong> We are looking for students who want to learn computational methods, not students who already have.</li>
      <li><strong>Tell us what research access looks like at your school.</strong> If your institution has no research groups in this area, say so. That is context we actively want.</li>
      <li><strong>Have someone read it.</strong> Your writing center, an advisor, a friend in another major.</li>
    </ul>
  </div>
</section>
"""

LIFE = """
<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Life at Auburn</p>
    <h1 class="sec">Ten weeks in Auburn, Alabama</h1>
    <p class="lede">You will be living on campus with nine other students who are doing the same thing you are. We put real effort into making that a good ten weeks.</p>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">Support and logistics</p>
    <div class="grid g3">
      <div class="point"><h3>Stipend</h3><p>$6,365 for the ten-week program.</p></div>
      <div class="point"><h3>Housing</h3><p>On-campus for the full ten weeks — suite-style (two rooms joined by a bathroom) or apartment-style (four bedrooms, a common area with a full kitchen, two bathrooms), with access to the student activity center, library, and computing facilities.</p></div>
      <div class="point"><h3>Meals</h3><p>Board is provided for the entire program.</p></div>
      <div class="point"><h3>Travel</h3><p>Travel to and from Auburn — airfare, shuttle bus, and similar — is reimbursed.</p></div>
      <div class="point"><h3>Workspace</h3><p>You are based in your mentor's home department and provided with a laptop for your work and for access to the HPC systems.</p></div>
      <div class="point"><h3>The town</h3><p>Auburn is a college town of about 80,000 in east Alabama, about two hours from Atlanta. Summers are hot; the campus is green and walkable.</p></div>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Community</p>
    <h2 class="sec">Every other week, something that isn't work</h2>
    <p class="lede">These exist so the cohort actually knows each other, and so you meet your mentors somewhere other than a conference room.</p>
    <div class="grid g2">
      <ul class="clean">
        <li><strong>Cookout</strong> with students and mentors in the first weeks</li>
        <li><strong>Chewacla State Park hike</strong> — 696 acres of woods, waterfalls, and trails just south of campus</li>
        <li><strong>Jule Collins Smith Museum of Fine Art</strong> — a half-day visit to Auburn's art museum</li>
      </ul>
      <ul class="clean">
        <li><strong>Star gazing</strong> with the telescopes in the Department of Physics</li>
        <li><strong>CM4 Trivia Night</strong> — famous scientists, breakthroughs in materials, and guessing materials from their properties</li>
        <li><strong>Movie night</strong>, plus trips introducing you to the culture, history, and geography of Alabama</li>
      </ul>
    </div>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack">
    <p class="eyebrow">The machines</p>
    <h2 class="sec">What you'll be computing on</h2>
    <div class="grid g3">
      <div class="point"><h3>Easley (Auburn)</h3><p>A Dell PowerEdge HPC cluster: ~9,424 cores, 46 TB RAM, 3 PB of disk, 500+ TFlops, and NVIDIA Tesla T4 GPUs. You tour the facility in Week 4.</p></div>
      <div class="point"><h3>ASA-X (Alabama)</h3><p>The Alabama Supercomputer Authority's system, free to Alabama's academic community: 4,688 x86-64 processors, 512 GB&ndash;6 TB per node, InfiniBand, and 1.4 PB of shared storage.</p></div>
      <div class="point"><h3>National facilities</h3><p>Auburn groups also have access to NSF ACCESS, TACC Frontera, ORNL CNMS, and DOE NERSC.</p></div>
    </div>
    <p class="narrow"><strong>Software you may use:</strong> VASP, Quantum ESPRESSO, LAMMPS, GROMACS, NAMD, VMD, Gaussian, ORCA, ANSYS, Abaqus, OpenFOAM, Psi4, OOF2, the MIT Atomic-Scale Modeling Toolkit, and Python/Jupyter — plus custom codes from our groups.</p>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack narrow">
    <p class="eyebrow">Code of conduct</p>
    <h2 class="sec">A safe and respectful program</h2>
    <p>Auburn University is committed to a safe, respectful, and inclusive environment. All participants — students, faculty mentors, and graduate mentors — take part in training on expectations of behavior during the first week, covering the REMMMEDIES Code of Conduct and Auburn's policies on sexual and gender-based misconduct, harassment, and discrimination.</p>
    <p>The following will not be tolerated: harassment, intimidation, or discrimination of any kind; and physical, written, electronic, or verbal abuse of any participant. No participant should ever be belittled or made to feel unsafe. Auburn's <a href="https://studentaffairs.auburn.edu/safe-harbor">Safe Harbor</a> office provides confidential support and information about reporting options.</p>
  </div>
</section>
"""

FAQS = [
    ("Do I need programming experience?",
     "No. It helps, and it is listed as preferred, but the first week exists precisely to bring everyone up to speed — Linux, job submission, Python, and the simulation packages. Several projects are designed for students starting in computational work."),
    ("Do I need to be a physics or chemistry major?",
     "No. We take students from physics, chemistry, materials science and engineering, chemical engineering, mathematics, statistics, computer science, and related STEM fields. What matters is interest in computational research."),
    ("Can international students apply?",
     "Unfortunately not. NSF requires REU participants to be U.S. citizens, U.S. nationals, or permanent residents. This is a condition of the funding and we have no discretion over it."),
    ("I'm graduating this spring. Can I still apply?",
     "No — you must still be enrolled in an undergraduate degree program through the summer and cannot have received your bachelor's degree before the program ends."),
    ("I go to a community college. Is this program for me?",
     "Yes, emphatically. Students from community colleges and other institutions where research is hard to access are exactly who this program was built for, and we aim for at least half of each cohort to come from such institutions."),
    ("Can I do this remotely, or for part of the summer?",
     "No. The program is in person in Auburn for the full ten weeks. Being physically present with your partner, your mentors, and the cohort is central to how the program works."),
    ("Do I have to pay for housing or food?",
     "No. On-campus housing and board are provided for the full ten weeks, and travel to and from Auburn is reimbursed. The $6,365 stipend is yours."),
    ("Can I take a class or work another job during the program?",
     "The program is a full-time commitment. Please plan not to enroll in summer coursework or hold another job during the ten weeks."),
    ("How are students matched to projects?",
     "You rank your top three projects in your application. The selection committee weighs your preferences alongside your background and motivation to find a strong fit with each project's research question and methods."),
    ("Who will I actually work with day to day?",
     "Your faculty mentor, whom you meet with at least weekly; a graduate student in their group as your near-peer mentor; and your project partner, the other REU student working on the same problem at a different scale."),
    ("Will I get to publish or present my work?",
     "Many participants do. We support publication in indexed journals or in the Auburn University Journal of Undergraduate Scholarship, and provide partial travel funding for students presenting at conferences after the program."),
    ("Do I need a car?",
     "No. Campus is walkable and Auburn runs a campus transit system. Parking is available if you do drive; ask us about a summer permit."),
]


def faq_page():
    items = []
    for i, (q, a) in enumerate(FAQS):
        openattr = " open" if i == 0 else ""
        items.append(f"""      <details class="faq"{openattr}>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>""")
    return """
<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">FAQ</p>
    <h1 class="sec">Questions we get</h1>
    <div class="faqlist">
""" + "\n".join(items) + """
    </div>
    <p class="fineprint">Something not answered here? Email <span class="ph">[[PROGRAM EMAIL]]</span>.</p>
  </div>
</section>
"""


CONTACT = """
<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">Contact</p>
    <h1 class="sec">Get in touch</h1>
    <div class="grid g2">
      <div class="stack">
        <div class="callout">
          <p class="eyebrow">Program email</p>
          <p class="bigmono ph">[[PROGRAM EMAIL]]</p>
          <p class="d">Monitored by the program leadership and coordinator. The fastest way to reach us, and the right address for questions about eligibility, projects, or the application.</p>
        </div>
        <div>
          <p class="eyebrow">Mailing address</p>
          <p class="addr">Center for Multiscale Modeling of Materials and Molecules (CM4)<br>Auburn University<br>Auburn, AL 36849</p>
        </div>
      </div>
      <div class="stack">
        <p class="eyebrow">Program leadership</p>
        <div class="peoplecol">
          <div class="person"><span class="avatar" aria-hidden="true">MK</span><span class="pbody"><span class="nm">Dr. Marcelo A. Kuroda</span><span class="rl">Principal Investigator · Physics</span></span></div>
          <div class="person"><span class="avatar" aria-hidden="true">KK</span><span class="pbody"><span class="nm">Dr. Konstantin Klyukin</span><span class="rl">Co-Principal Investigator · Materials Engineering</span></span></div>
          <div class="person"><span class="avatar" aria-hidden="true">EM</span><span class="pbody"><span class="nm">Dr. Evangelos Miliordos</span><span class="rl">Senior Investigator · Chemistry and Biochemistry</span></span></div>
          <div class="person"><span class="avatar" aria-hidden="true">&mdash;</span><span class="pbody"><span class="nm ph">[[COORDINATOR NAME]]</span><span class="rl">Project coordinator</span></span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band tint">
  <div class="wrap stack narrow">
    <p class="eyebrow">Information sessions</p>
    <h2 class="sec">Virtual Q&amp;A</h2>
    <p>We hold Zoom sessions during the application window: <span class="ph">[[WEBINAR DATES]]</span>. Bring any question — about the projects, the application, funding, or what living in Auburn is like.</p>
  </div>
</section>

<section class="band paper">
  <div class="wrap stack">
    <p class="eyebrow">For faculty and advisors</p>
    <h2 class="sec">Partner with us</h2>
    <p class="lede">If you advise undergraduates who might be a fit, we would be glad to send you a flyer, visit your campus, or join a virtual session with your students.</p>
    <p class="narrow">We currently partner with institutions across the Southeast including the University of South Alabama, Tuskegee University, Troy University, Alabama State University, Alabama A&amp;M University, Southern Adventist University, Furman University, Florida International University, Spelman College, the University of Alabama in Huntsville, LaGrange College, Central Alabama Community College, and Southern Union Community College.</p>
  </div>
</section>
"""

BODIES = {
    "home": HOME,
    "program": PROGRAM,
    "research": projects_page(),
    "mentors": mentors_page(),
    "apply": APPLY,
    "life": LIFE,
    "faq": faq_page(),
    "contact": CONTACT,
}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    written = []
    for fname, key, label, title, desc in PAGES:
        html = HEAD.format(title=title, desc=desc, site=SITE_NAME,
                           tagline=TAGLINE, nav=nav_html(key))
        html += BODIES[key]
        html += FOOT
        path = os.path.join(root, fname)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        written.append(fname)

    # sitemap
    base = "https://REPLACE-WITH-YOUR-SITE-URL/"
    urls = "\n".join(
        f"  <url><loc>{base}{f if f != 'index.html' else ''}</loc></url>"
        for f, *_ in PAGES)
    with open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                 + urls + "\n</urlset>\n")

    print("Wrote:", ", ".join(written), "and sitemap.xml")

    # report remaining placeholders
    found = {}
    for f, *_ in PAGES:
        text = open(os.path.join(root, f), encoding="utf-8").read()
        for m in set(re.findall(r"\[\[[A-Z ]+\]\]", text)):
            found.setdefault(m, []).append(f)
    if found:
        print("\nPlaceholders still to fill in:")
        for k in sorted(found):
            print(f"  {k:26} {', '.join(sorted(found[k]))}")


if __name__ == "__main__":
    main()
