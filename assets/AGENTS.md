# Agent Instructions

Use this workflow for any request that creates or revises course material.

## 1) Understand the Task
- Identify the target artifact: module, lesson page, course home, labs, references, summary, or full site.
- Identify the source material: `.docx`, notes, syllabus, existing HTML, or mixed inputs.
- Confirm user constraints when present: language, audience, depth, theme, publication target, or scope.

## 2) Recover Meaning Before Editing
- If the existing text is incomplete, unclear, or too extraction-like, inspect the original source before rewriting.
- Prefer preserving meaning, then improving structure and readability.
- Remove references that only make sense in the original source context.

## 3) Apply the Course Standard
- Keep the output concise, neutral, and study-oriented.
- Keep terminology and naming consistent across modules.
- Prefer explicit section titles and visible hierarchy over long flat prose.
- Reuse the project's established file structure and CSS/UI patterns.
- If the request conflicts with older conventions, follow the latest explicit user instruction.

## 4) Handle Structure and Assets Carefully
- Preserve valid internal links, navigation, and stable paths.
- Keep figure-to-caption mapping correct.
- Use meaningful captions and avoid placeholder text.
- Place assets in the project's existing asset structure.
- Avoid unnecessary duplication of equivalent assets.

## 5) Validate Before Stopping
- Check the requested content exists after the edit.
- Check for broken HTML, broken links, or missing assets.
- Check that structure remains coherent with neighboring modules/pages.
- Check that no source-process phrasing remains unless intentionally requested.
- Check that theme/layout behavior remains consistent where applicable.
- Ensure the request is fully applied before stopping.

## Default Website Variant

If the project follows the current website pattern:
- content usually lives in `site/`
- modules usually live in `site/chapters/chapter-XX.html`
- source chapters may live in `resources/chXX.docx`
- figures may live under `site/assets/images/`

In that variant:
- keep module navigation coherent
- preserve the in-module structure tree if present
- keep anchor targets visible below sticky UI
- keep print behavior local-only and static-host compatible
- keep the selected theme consistent

## Quick Command Pattern
- Search text: `rg -n "text" site/chapters/ site/`
- Search unwanted source references: `rg -n "in this section|in this chapter|in this book|resources|extracted from" site/`
- Verify links/images: `rg -n "chapter-|assets/images|href=|src=" site/index.html site/chapters/*.html`
