# Course Material Requirements

Use these requirements as the baseline quality bar for educational content projects.

Adapt them to the user's request, but do not silently drop clarity, structure, or consistency.

## Objective

Create or maintain study-ready course materials from source content such as `.docx`, notes, syllabi, or existing lesson pages.

The output may be:
- a full static course site
- one or more lesson or module pages
- supporting pages such as labs, references, bibliography, or summaries
- revised existing content that needs a consistent instructional standard

## Inputs

Possible inputs include:
- chapter files such as `resources/chXX.docx`
- syllabus or outline files
- existing site files under `site/`
- HTML, Markdown, notes, or mixed draft material
- explicit user constraints for tone, audience, depth, or delivery format

## Output Standard

Unless the user specifies otherwise, the output should be:
- English
- neutral and study-oriented
- concise but not shallow
- standalone, without source-structure wording that breaks when read in isolation
- consistent with the rest of the course or project
- tracked through a main course structure file that maps modules to their source materials

## Main Structure File

Each project must have a main file that defines:
- the course module structure
- the output artifact for each module
- the source files used by each module

For the default website variant, use `course-structure.md` at the project root.

This file is the canonical map for planning and maintenance. Keep it updated when:
- modules are added, merged, split, or renamed
- source files change
- one module uses multiple sources
- one source feeds multiple modules

## Content Rules

- Remove structural references such as "in this section", "in this chapter", "in this book", or "as discussed earlier" unless they are intentionally needed.
- Remove references to extraction pipelines or raw source provenance unless the user explicitly wants them.
- Prefer meaningful titles, section labels, and summaries over copied source wording.
- Preserve enough explanatory depth to support study use.
- Keep terminology consistent across artifacts.
- Avoid conversational filler and generic educational fluff.

## Structure Rules

For module-like outputs, prefer:
- a clear title
- visible section hierarchy
- coherent navigation or progression
- a recap, summary, or key takeaways block when appropriate for the project pattern

If the project already uses numbered sections, preserve and normalize them.
If the project already uses a two-level hierarchy, keep it consistent.

Do not collapse well-structured material into flat prose.

## Figures and Media Rules

When figures or media are part of the task:
- preserve the correct mapping between each figure and its caption
- use meaningful captions, not placeholders
- keep figures in the right section context
- store assets in the project's existing asset structure
- verify paths from consuming pages
- avoid duplicating equivalent assets unnecessarily

If the project already uses a caption numbering convention such as `MXX.YY`, preserve it.

## Website Variant Rules

When the project is a static course site, require:
- consistent navigation between modules or pages
- compact and readable top-level navigation
- clean asset organization under the site structure
- theme consistency across the site
- static-host compatible behavior with minimal dependencies

When present, also preserve:
- in-module structure trees
- sticky-header-safe anchor behavior
- print-friendly output
- references, labs, bibliography, and sitography sections

## Theme Rules

If the project uses themes:
- prefer CSS variables for reusable design tokens
- keep layout behavior consistent across themes
- keep text and link contrast readable
- use the project default theme unless the user asks for a different one

For the current default website variant, reuse the presets in `THEMES.md`.

## Quality Gate

Before considering the task complete, verify the relevant subset of:
- no incomplete or broken sentences
- no broken links or missing assets
- no accidental language mixing
- no leftover source-process wording
- no figure/caption mismatch
- structure is consistent with neighboring artifacts
- navigation still works
- theme/layout remains coherent
- requested scope is fully delivered

## Current Default Variant

For the currently established pattern in this skill:
- source chapters may live in `resources/chXX.docx`
- output pages may live in `site/chapters/`
- shared assets may live in `site/assets/`
- the final delivery may be a GitHub Pages compatible static site

Treat this as the default implementation variant, not as the only allowed output form.
