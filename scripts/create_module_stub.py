#!/usr/bin/env python3
"""Create a course module HTML stub inside an existing website variant project."""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path


MODULE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{module_code} - {module_title}</title>
  <link rel="stylesheet" href="../assets/css/theme.css">
  <script defer src="../assets/js/site.js"></script>
</head>
<body data-theme="{theme}">
  <header class="site-header">
    <div class="shell">
      <p><a href="../index.html">Home</a></p>
      <h1>{module_code} - {module_title}</h1>
      <p class="lead">{summary}</p>
    </div>
  </header>

  <main class="shell">
    <section class="panel">
      <nav aria-label="Module navigation">
        <span>{previous_label}</span>
        <strong>{module_code}</strong>
        <span>{next_label}</span>
      </nav>
    </section>

    <section class="panel">
      <h2>1. Main section</h2>
      <p>Replace this section with study-ready content.</p>
      <h3>1.1 Subsection</h3>
      <p>Add supporting explanation, examples, or figures here.</p>
    </section>

    <section class="panel">
      <h2>Key takeaways</h2>
      <ul>
        <li>Summarize the main concept.</li>
        <li>Highlight what learners should retain.</li>
      </ul>
      <p><button type="button" data-print>Print module</button></p>
    </section>
  </main>
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", help="Project root containing site/chapters")
    parser.add_argument("module_number", type=int, help="Module number, e.g. 3")
    parser.add_argument("module_title", help="Module title")
    parser.add_argument("--theme", default="light")
    parser.add_argument(
        "--summary",
        default="Replace this introduction with standalone study-ready content.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_path).resolve()
    chapters_dir = project_root / "site" / "chapters"
    if not chapters_dir.is_dir():
        print(f"Missing chapters directory: {chapters_dir}", file=sys.stderr)
        return 1

    module_code = f"M{args.module_number:02d}"
    filename = chapters_dir / f"chapter-{args.module_number:02d}.html"
    if filename.exists() and not args.force:
        print(f"Refusing to overwrite existing file: {filename}", file=sys.stderr)
        return 1

    previous_label = f"M{args.module_number - 1:02d} - Previous" if args.module_number > 1 else "Previous"
    next_label = f"M{args.module_number + 1:02d} - Next"

    filename.write_text(
        MODULE_TEMPLATE.format(
            module_code=module_code,
            module_title=html.escape(args.module_title),
            summary=html.escape(args.summary),
            theme=html.escape(args.theme),
            previous_label=html.escape(previous_label),
            next_label=html.escape(next_label),
        ),
        encoding="utf-8",
    )

    print(f"Created {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
