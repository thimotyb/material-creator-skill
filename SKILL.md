# Codex Skill: Course Builder from Book Chapters

## Purpose
Build and maintain a study-ready static course website from `.docx` chapter files in `resources/`.

## Trigger
Use this skill when the user asks to:
- create a course site from book chapters
- revise module text/figures
- improve readability/tone/navigation
- publish updates to GitHub Pages

## Inputs
- `resources/chXX.docx` chapter files
- existing site in `site/`
- optional syllabus file in `resources/`

## Output Contract
- English-only content
- one module per file: `site/chapters/chapter-XX.html`
- figures under `site/assets/images/chXX/`
- numbered captions: `MXX.YY - <original source caption text>`
- preserve source figure-to-caption mapping exactly (no swapped captions)
- key takeaways box at end of each module
- compact home nav with section anchors (`Modules`, `Labs`, `References`)
- arrow cues in module navigation and module link lists
- updated home page references/labs when requested
- selectable visual theme presets (minimum 4, recommended 5)
- print icon/button on each module page (local JavaScript, browser print dialog)
- print-optimized CSS for clean PDF/paper output

## Hard Rules
1. Remove structural references such as:
   - "in this section"
   - "in this book"
   - "as discussed earlier"
2. Remove references to extraction/source process (`resources`, "extracted from ...").
3. Keep tone neutral, concise, study-oriented (not conversational).
4. Keep summaries light: preserve enough explanatory depth for study use.
5. Keep navigation coherent (`prev/current/next`).
6. Keep top-level navigation compact and avoid long breadcrumb-like module lists in home top bar.
7. Add clear arrow cues for module progression links.
8. If text is unclear or truncated, check original `resources/chXX.docx` before rewriting.
9. Support a predefined theme choice for the whole site.
10. In body text, remove explicit numeric references to source structure (e.g., "Figure 4.2", "Chapter 3", "Section 2.1").
11. Keep references standalone by replacing those with neutral wording ("the diagram", "related modules", "related topics").
12. Print support must be local-only (no external libraries) and GitHub Pages compatible.

## Theme Presets
Always support these presets:
- `light`
- `dark`
- `colorful`
- `high-contrast`
- `warm` (optional replacement: `minimal`)

## Theme Application Rules
1. Ask/select one preset at project setup (default: `light`).
2. Implement theme via CSS variables (not per-element hardcoded colors).
3. Keep readability first: body text contrast and link contrast must remain high.
4. Keep layout and navigation identical across themes.
5. If no preference is given, keep `light` and document available alternatives.

## Editing Workflow
1. Locate target text/section in HTML.
2. If needed, recover full meaning from matching `.docx`.
3. Rewrite as standalone study content.
4. Validate:
   - no broken sentence
   - no generic image captions
   - captions match original source caption wording
   - no figure/caption mismatches
   - no explicit "Figure N", "Chapter N", or "Section N" references in body text
   - no Italian in English modules
   - no broken links/images
   - print button present and working on every module page
   - print stylesheet hides navigation controls and preserves section/figure readability
5. Publish:
   - `scripts/publish-site.sh https://github.com/<USER>/<PUBLIC-SITE-REPO>.git main`

## Fast Validation Commands
- `rg -n "text to fix" site/chapters/chapter-*.html`
- `rg -n "in this section|in this book|resources" site/chapters/chapter-*.html`
- `rg -n "M[0-9]{2}\\.[0-9]{2}" site/chapters/chapter-*.html`
- `rg -n "\\b(Figure|Chapter|Section)\\s+[0-9]" site/chapters/chapter-*.html`
