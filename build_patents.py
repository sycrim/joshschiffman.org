#!/usr/bin/env python3
"""Generate patents.html from patents.md.

Usage: pip install -r requirements.txt && python3 build_patents.py
"""
import markdown
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "patents.md"
OUT = ROOT / "patents.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Joshua Schiffman's issued U.S. patents in computer and systems security">
<meta name="keywords" content="Joshua Schiffman Patents Security HP AMD Samsung">
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
      <a href="pubs.html">Publications</a>
      <a href="patents.html" class="active">Patents</a>
      <a href="vita.html">Vita</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</header>

<main class="container">
  <h2 class="page-title">Patents</h2>

  <p class="pub-jump">
    <a href="#hp">HP Inc.</a> |
    <a href="#amd">Advanced Micro Devices</a> |
    <a href="#samsung">Samsung Electronics</a>
  </p>

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


def main():
    text = SRC.read_text()
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    OUT.write_text(TEMPLATE.format(body=body))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
