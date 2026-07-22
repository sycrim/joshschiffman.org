#!/usr/bin/env python3
"""Generate staging/pubs.html from pubs.md, with "Cite" widgets from pubs_cites.py.

Usage: pip install -r requirements.txt && python3 build_pubs.py

To add a publication: add its citation line to pubs.md, then add a matching
add(...) call to pubs_cites.py in the same position (list order matters -
each <li> in pubs.md is paired positionally with an entry in pubs_cites.py).
"""
import html as htmllib
import re
from pathlib import Path

import markdown

import pubs_cites

ROOT = Path(__file__).parent
SRC = ROOT / "pubs.md"
OUT = ROOT / "staging" / "pubs.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="Joshua Schiffman's peer-reviewed publications in computer and systems security">
<meta name="keywords" content="Joshua Schiffman Security Publications HP Trusted Computing">
<title>Joshua Serratelli Schiffman, PhD</title>
<link rel="stylesheet" href="style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-G5VP9QW8KF"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-G5VP9QW8KF');
</script>
</head>
<body>

<header class="site-header">
  <div class="container">
    <h1>Joshua Serratelli Schiffman, PhD</h1>
    <nav>
      <a href="index.html">Home</a>
      <a href="pubs.html" class="active">Publications</a>
      <a href="vita.html">Vita</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</header>

<main class="container">
  <h2 class="page-title">Publications</h2>

  <p class="pub-jump">
    <a href="#journal">Journal</a> |
    <a href="#conference">Conference</a> |
    <a href="#workshops">Workshops</a> |
    <a href="#misc">Misc</a> |
    <a href="#techreports">Tech Reports</a>
  </p>

  <p class="pub-note">Patents and invited talks are listed on the <a href="vita.html">Vita</a> page.</p>

  <div class="pub-body">
{body}
  </div>
</main>

<footer class="site-footer">
  <div class="container">&copy; Joshua Schiffman</div>
</footer>

</body>
</html>
"""


def details_html(e):
    bib = htmllib.escape(pubs_cites.render_bibtex(e), quote=False)
    plain = htmllib.escape(pubs_cites.render_plain(e), quote=False)
    return (
        '\n    <details class="cite">\n'
        '      <summary>Cite</summary>\n'
        f'      <pre>{bib}</pre>\n'
        f'      <p class="cite-plain">{plain}</p>\n'
        '    </details>'
    )


def insert_cites(body_html):
    pattern = re.compile(r'<li(?=[\s>])[^>]*>.*?</li>', re.DOTALL)
    matches = list(pattern.finditer(body_html))
    if len(matches) != len(pubs_cites.entries):
        raise SystemExit(
            f"pubs.md has {len(matches)} <li> entries but pubs_cites.py has "
            f"{len(pubs_cites.entries)} - keep them in sync (same order, same count)."
        )

    out = []
    last_end = 0
    for m, e in zip(matches, pubs_cites.entries):
        out.append(body_html[last_end:m.start()])
        block = m.group(0)
        idx = block.rfind('</li>')
        out.append(block[:idx] + details_html(e) + '\n    ' + block[idx:])
        last_end = m.end()
    out.append(body_html[last_end:])
    return ''.join(out)


def main():
    text = SRC.read_text()
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    body = insert_cites(body)
    OUT.write_text(TEMPLATE.format(body=body))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
