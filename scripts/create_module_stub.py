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

MODULES_HEADER = "| Module | Title | Output Artifact | Source Files | Notes |"
SOURCE_HEADER = "| Source File | Type | Used In Modules | Notes |"


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
    parser.add_argument(
        "--source-files",
        default="",
        help="Comma-separated source files for this module, e.g. resources/ch03.docx,resources/lab-notes.md",
    )
    parser.add_argument("--notes", default="", help="Notes for course-structure.md")
    parser.add_argument("--force", action="store_true", help="Overwrite existing file")
    return parser.parse_args()


def split_csv(raw: str) -> list[str]:
    return [part.strip() for part in raw.split(",") if part.strip()]


def source_file_type(path: str) -> str:
    suffix = Path(path).suffix.lower()
    if suffix == ".docx":
        return "chapter"
    if suffix == ".md":
        return "notes"
    if suffix == ".pdf":
        return "pdf"
    if suffix:
        return suffix.lstrip(".")
    return "source"


def upsert_markdown_row(lines: list[str], header: str, row_key: str, row: str) -> list[str]:
    try:
        header_index = lines.index(header)
    except ValueError:
        return lines

    insert_index = header_index + 2
    while insert_index < len(lines) and lines[insert_index].startswith("|"):
        current = lines[insert_index]
        if current.startswith(f"| {row_key} |"):
            lines[insert_index] = row
            return lines
        insert_index += 1

    lines.insert(insert_index, row)
    return lines


def update_course_structure(
    course_structure_path: Path,
    module_code: str,
    module_title: str,
    output_artifact: str,
    source_files: list[str],
    notes: str,
) -> None:
    if not course_structure_path.exists():
        return

    lines = course_structure_path.read_text(encoding="utf-8").splitlines()
    source_display = ", ".join(f"`{source}`" for source in source_files) if source_files else "original"
    module_row = f"| {module_code} | {module_title} | `{output_artifact}` | {source_display} | {notes} |"
    lines = upsert_markdown_row(lines, MODULES_HEADER, module_code, module_row)

    for source_file in source_files:
        source_row = (
            f"| `{source_file}` | {source_file_type(source_file)} | `{module_code}` | Added by create_module_stub.py |"
        )
        lines = upsert_markdown_row(lines, SOURCE_HEADER, f"`{source_file}`", source_row)

    course_structure_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
    source_files = split_csv(args.source_files) or [f"resources/ch{args.module_number:02d}.docx"]

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
    update_course_structure(
        project_root / "course-structure.md",
        module_code=module_code,
        module_title=html.escape(args.module_title),
        output_artifact=f"site/chapters/chapter-{args.module_number:02d}.html",
        source_files=source_files,
        notes=html.escape(args.notes),
    )

    print(f"Created {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
