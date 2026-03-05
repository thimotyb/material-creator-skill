# Material Creator Skill

Reusable skill pack to create and maintain study-ready course websites from chapter `.docx` files.

## What this skill does
- Converts chapter files (`resources/chXX.docx`) into structured HTML modules.
- Enforces a consistent course format:
  - module numbering (`MXX`)
  - two-level section numbering (`1`, `1.1`)
  - figure numbering (`MXX.YY`)
  - `Key takeaways` box at end of each module
- Improves text quality (standalone phrasing, neutral study tone, no conversational fillers).
- Supports figure import/captioning and basic site UX conventions.
- Includes quality gates and publishing workflow for GitHub Pages.
- Supports predefined visual themes:
  - `light`, `dark`, `colorful`, `high-contrast`, `warm`
- Adds a print action on each module page (`Print` icon/button) using local JavaScript.
- Applies print-specific CSS so printed/PDF output is clean and readable.
- Requires a structure tree panel with indented second-level items and active-section highlighting while scrolling.

## Repository contents
- `SKILL.md` - Codex skill behavior
- `assets/REQUIREMENTS.md` - reusable requirements template
- `assets/AGENTS.md` - reusable execution workflow
- `assets/TASK.md` - reusable task checklist
- `assets/CLAUDE.md` - Claude-oriented instruction template
- `assets/THEMES.md` - theme presets and token examples

## Install in Codex

### Option A (recommended: project-local)
1. Copy this repository files into:
   - `<your-project>/.codex/skills/course-builder/`
2. Ensure at least:
   - `<your-project>/.codex/skills/course-builder/SKILL.md`
   - `<your-project>/.codex/skills/course-builder/assets/*`
3. In your project, reuse templates from `assets/` as needed.

### Option B (global/user skills)
1. Copy the same folder into your Codex home skills directory:
   - `$CODEX_HOME/skills/course-builder/`
2. Keep the same structure (`SKILL.md` + `assets/`).

## Install in Claude
Claude does not use Codex `SKILL.md` natively, so use the templates this way:
1. Copy `assets/CLAUDE.md` into your project as:
   - `CLAUDE.md` or your preferred project instruction file.
2. Copy supporting templates into your project:
   - `assets/REQUIREMENTS.md`
   - `assets/AGENTS.md`
   - `assets/TASK.md`
   - `assets/THEMES.md`
3. Reference these files in your workflow prompts when starting a new course build.

## Quick start for a new course
1. Put chapter files in `resources/` (`ch01.docx`, `ch02.docx`, ...).
2. Fill `REQUIREMENTS.md` and `TASK.md`.
3. Build/update modules under `site/chapters/`.
4. Validate quality gates.
5. Publish to your public Pages repo.
