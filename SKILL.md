---
name: material-creator-skill
description: Create or maintain course materials with a consistent workflow, structure, tone, and quality bar. Use when the user wants to build or revise educational content such as modules, course websites, lesson pages, labs, references, or derived material from source files like DOCX, notes, syllabi, or existing HTML.
---

# Material Creator Skill

Use this skill when the user wants a repeatable way to create course content "sempre allo stesso modo".

This skill is intentionally broader than a single website generator. It defines a standard workflow for educational material production, while still supporting the current concrete pattern based on `resources/chXX.docx` and `site/`.

## Use This Skill When

Trigger this skill when the user asks to:
- create a new course or module from source material
- convert chapter files, notes, or syllabus content into study-ready material
- revise existing modules for tone, clarity, structure, navigation, or consistency
- standardize a course website or lesson pages across modules
- generate or refresh labs, references, summaries, or supporting course pages
- maintain a course publishing workflow with stable formatting and quality checks

## Default Assumptions

Unless the user says otherwise:
- language: English
- tone: neutral, concise, study-oriented
- output should be standalone and not depend on book-local wording like "in this chapter" or "as discussed earlier"
- structure should be explicit, scannable, and consistent across modules
- keep the workflow deterministic and reusable rather than inventing a new format each time

## Typical Inputs

Accept any combination of:
- source chapters in `resources/` such as `resources/chXX.docx`
- a syllabus, outline, or reading list
- an existing course site in `site/`
- existing module HTML, Markdown, or notes
- explicit user requirements about audience, depth, tone, theme, and publication target

## Typical Outputs

Depending on the task, produce one or more of:
- a course website under `site/`
- one lesson or module per file, usually under `site/chapters/`
- revised study text for modules or sections
- labs, references, bibliography, sitography, summaries, and key takeaways
- reusable content structure that stays coherent across the whole course

When the project already uses the website pattern from this skill, keep:
- one module per page
- assets under `site/assets/`
- stable navigation across modules
- a shared theme system

## Standard Workflow

Follow this order unless the user asks for a smaller scoped edit.

1. Understand the course context.
   Determine audience, source material, desired outputs, constraints, and whether the task is a new build or a revision.

2. Identify the target artifact.
   Decide whether you are editing a module, building a new lesson, updating home/references/labs, or standardizing the whole course structure.

3. Recover source meaning before rewriting.
   If existing text is unclear, incomplete, or mechanically extracted, check the source files before editing.

4. Rewrite into standalone learning material.
   Remove source-structure references, keep the meaning, and present content in a way that works independently.

5. Apply the course standard.
   Keep naming, section hierarchy, navigation, captions, and UI patterns consistent with the rest of the course.

6. Validate before stopping.
   Check content integrity, structure, links, assets, and consistency with the project conventions.

## Course Content Standard

Apply these rules by default:
- write for study use, not for marketing
- prefer clarity over flair
- avoid conversational filler
- preserve enough detail to support learning, not just a thin summary
- use meaningful section titles
- keep terminology consistent within and across modules
- remove references to extraction pipelines or file provenance unless the user explicitly wants them

Replace structural references such as:
- "in this section"
- "in this chapter"
- "in this book"
- "as discussed earlier"

with standalone phrasing that still makes sense when read in isolation.

## Structure Standard

For module-like outputs, prefer:
- a clear module title
- explicit section hierarchy
- predictable navigation
- a closing recap or key takeaways block

If the project uses numbered sections, preserve and normalize them.
If the project uses a two-level module structure, keep that pattern consistent.

Do not flatten a structured module into an unstructured wall of text.

## Figure and Asset Standard

When the task includes figures or diagrams:
- keep figure-to-caption mapping correct
- use meaningful captions, never generic placeholders
- place assets in the project's established asset structure
- verify paths from the consuming page
- avoid duplicating equivalent assets unnecessarily

If the current course pattern uses module-based caption numbering such as `MXX.YY`, preserve it.

## Website Pattern

When the project follows the existing course-site layout:
- keep the home navigation compact
- keep module navigation coherent (`prev/current/next` where applicable)
- preserve the in-module structure tree if present
- ensure anchor jumps do not hide headings below sticky UI
- keep print behavior local-only and static-host compatible
- prefer minimal dependencies and GitHub Pages compatible solutions

Theme handling should stay token-based through CSS variables. Reuse the theme presets in `assets/THEMES.md` unless the user asks for a different visual system.

## Validation Checklist

Before stopping, verify the relevant subset of:
- no broken or incomplete sentences
- no source-process references left behind
- no broken links or missing assets
- no accidental language mixing
- structure is consistent with neighboring modules/pages
- figures and captions still match
- navigation still works
- theme and layout remain coherent
- requested output is complete, not partially applied

## Bundled Assets

Use the bundled assets instead of re-inventing the workflow:
- `assets/AGENTS.md` for the step-by-step editing workflow
- `assets/REQUIREMENTS.md` for the baseline website/content requirements
- `assets/TASK.md` for project tracking
- `assets/THEMES.md` for reusable theme presets

Load only the file(s) needed for the task.

## Concrete Current Variant

For the current implementation pattern already captured by this skill:
- source files often live in `resources/chXX.docx`
- module pages often live in `site/chapters/chapter-XX.html`
- site assets often live in `site/assets/`
- publishing may use a GitHub Pages workflow

Treat this as the default project variant, not as the only valid use of the skill.
