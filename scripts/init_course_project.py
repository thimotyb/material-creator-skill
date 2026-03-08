#!/usr/bin/env python3
"""Bootstrap a course-material project with the default website variant."""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path


INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{course_title}</title>
  <link rel="stylesheet" href="assets/css/theme.css">
</head>
<body data-theme="{theme}">
  <header class="site-header">
    <div class="shell">
      <p class="eyebrow">{course_label}</p>
      <h1>{course_title}</h1>
      <p class="lead">{course_summary}</p>
      <nav class="top-nav" aria-label="Primary">
        <a href="#modules">Modules</a>
        <a href="#labs">Labs</a>
        <a href="#references">References</a>
      </nav>
    </div>
  </header>

  <main class="shell">
    <section id="modules" class="panel">
      <h2>Modules</h2>
      <ol class="module-list">
        <li><a href="chapters/chapter-01.html">M01 - Example module</a></li>
      </ol>
    </section>

    <section id="labs" class="panel">
      <h2>Labs</h2>
      <p>Add lab activities, exercises, or project briefs here.</p>
    </section>

    <section id="references" class="panel">
      <h2>References</h2>
      <h3>Bibliography</h3>
      <ul>
        <li>Add core books, papers, or manuals here.</li>
      </ul>
      <h3>Sitography</h3>
      <ul>
        <li>Add curated websites and online resources here.</li>
      </ul>
    </section>
  </main>
</body>
</html>
"""


THEME_CSS = """:root {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --text: #13253f;
  --muted: #5c6b82;
  --accent: #0f6f8e;
  --accent-strong: #0a5368;
  --border: #d8e1ef;
}

body[data-theme="dark"] {
  --bg: #0f1621;
  --surface: #182231;
  --text: #eaf1ff;
  --muted: #a7b4c7;
  --accent: #50b7d8;
  --accent-strong: #7ad4ef;
  --border: #2d3c52;
}

body[data-theme="colorful"] {
  --bg: #fff8ee;
  --surface: #ffffff;
  --text: #22213a;
  --muted: #6d5c58;
  --accent: #ef6c2f;
  --accent-strong: #c84e17;
  --border: #f1d7c5;
}

body[data-theme="high-contrast"] {
  --bg: #000000;
  --surface: #111111;
  --text: #ffffff;
  --muted: #d9d9d9;
  --accent: #00e5ff;
  --accent-strong: #00ffff;
  --border: #ffffff;
}

body[data-theme="warm"] {
  --bg: #fbf5ef;
  --surface: #fffdf9;
  --text: #3a2b1f;
  --muted: #6f5847;
  --accent: #b5632d;
  --accent-strong: #8b4620;
  --border: #e8d7c7;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}

a { color: var(--accent-strong); }
.shell { width: min(980px, calc(100% - 2rem)); margin: 0 auto; }
.site-header { padding: 3rem 0 2rem; background: linear-gradient(180deg, var(--surface), transparent); }
.eyebrow { letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }
.lead { max-width: 60ch; color: var(--muted); }
.top-nav { display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem; }
.panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.25rem;
  margin: 1rem 0;
}
.module-list { padding-left: 1.2rem; }

@media print {
  .top-nav { display: none; }
  body { background: #ffffff; color: #000000; }
  .panel { border: 0; padding: 0; }
}
"""


SITE_JS = """document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-print]");
  if (button) {
    window.print();
  }
});
"""


MODULE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>M01 - Example module</title>
  <link rel="stylesheet" href="../assets/css/theme.css">
  <script defer src="../assets/js/site.js"></script>
</head>
<body data-theme="{theme}">
  <header class="site-header">
    <div class="shell">
      <p><a href="../index.html">Home</a></p>
      <h1>M01 - Example module</h1>
      <p class="lead">Replace this introduction with study-ready module text.</p>
    </div>
  </header>

  <main class="shell">
    <section class="panel">
      <nav aria-label="Module navigation">
        <span>Previous</span>
        <strong>Current</strong>
        <span>Next</span>
      </nav>
    </section>

    <div class="panel">
      <h2>1. Main section</h2>
      <h3>1.1 Subsection</h3>
      <p>Replace this content with standalone course material.</p>
    </div>

    <section class="panel">
      <h2>Key takeaways</h2>
      <ul>
        <li>Capture the core idea of the module.</li>
        <li>Keep recap points short and study-oriented.</li>
      </ul>
      <p><button type="button" data-print>Print module</button></p>
    </section>
  </main>
</body>
</html>
"""


TASK_MD = """# Project Task Tracker

- Course name: {course_title}
- Audience:
- Output format: static course site
- Theme: {theme}

## Next steps
- [ ] Add source files under `resources/`
- [ ] Update `site/index.html`
- [ ] Replace the example module in `site/chapters/chapter-01.html`
- [ ] Add additional modules as needed
"""


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Target project directory")
    parser.add_argument("--course-title", default="Course Title")
    parser.add_argument("--course-label", default="Course Material")
    parser.add_argument(
        "--course-summary",
        default="Study-ready course content generated from source material.",
    )
    parser.add_argument(
        "--theme",
        choices=["light", "dark", "colorful", "high-contrast", "warm"],
        default="light",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.path).resolve()
    root.mkdir(parents=True, exist_ok=True)

    replacements = {
        "course_title": html.escape(args.course_title),
        "course_label": html.escape(args.course_label),
        "course_summary": html.escape(args.course_summary),
        "theme": args.theme,
    }

    try:
        for rel_path, template in [
            ("site/index.html", INDEX_HTML),
            ("site/assets/css/theme.css", THEME_CSS),
            ("site/assets/js/site.js", SITE_JS),
            ("site/chapters/chapter-01.html", MODULE_HTML),
            ("task-tracker.md", TASK_MD),
        ]:
            write_file(root / rel_path, template.format(**replacements), args.force)

        for rel_dir in ["resources", "site/assets/images", "site/assets/downloads"]:
            (root / rel_dir).mkdir(parents=True, exist_ok=True)
    except FileExistsError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"Initialized course project at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
