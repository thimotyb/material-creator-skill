# Course Build Requirements (Simple)

## Objective
Create a study-ready website in English from chapter `.docx` files in `resources/`, with clear modules, sectioned content, figures, and navigation.

## Inputs
- `resources/chXX.docx` (one file per module/chapter)
- Optional syllabus `.docx` for module order and scope

## Mandatory Output
- Static site under `site/`
- Home page with modules, labs, bibliography, sitography
- One HTML page per module under `site/chapters/`
- Assets under `site/assets/` (CSS, JS, images)
- Theme system with preset selection

## Content Rules
- Language: English only.
- Tone: neutral, study-oriented, concise (not conversational).
- Text must be standalone:
  - Remove references like "in this section", "in this book", "as discussed earlier".
  - Remove references to extraction process or `resources` files.
- Summarize lightly, but keep enough detail for study.
- Every module must include:
  - Title with module number prefix (`MXX - <Title>`)
  - Two-level numbered structure:
    - Level 1 main sections (`1`, `2`, `3`, ...)
    - Level 2 subsections (`1.1`, `1.2`, `2.1`, ...)
  - Meaningful short section titles (not first words of paragraph)
  - A `Key takeaways` box at the end

## Figures Rules
- Import all relevant figures from source chapter.
- Number captions as `MXX.YY` (module.figure).
- Use meaningful caption text (never generic "Study figure").
- Figures must stay inside the correct section context.
- Click behavior:
  - Click image => full-browser zoom
  - No caption shown in zoom view
  - Click again => close zoom and return to text

## UX Rules
- Full HTML navigation between modules.
- Keep home top navigation compact: use section anchors (`Modules`, `Labs`, `References`) instead of listing all modules in the top bar.
- Add arrow cues in module navigation and module link lists to make progression explicit.
- In-module structure tree must indent level-2 entries under their level-1 parent.
- In-module structure tree must highlight the section currently in view while scrolling.
- Anchor jumps from structure/navigation must keep headings fully visible below sticky UI (use adequate vertical offset).
- Structure tree must be rendered as an internal left frame in the content layout (not as fixed overlay).
- Structure tree frame must never overlap breadcrumb/header/top navigation.
- Back-to-top button on pages.
- Print button/icon on every module page.
- Print behavior: click print button => open browser print dialog (`window.print()` via local JavaScript).
- Add print-optimized CSS (`@media print`) to hide navigation controls and keep printed content readable.
- Readable layout and pleasant CSS.
- Minimal dependencies, GitHub Pages compatible.

## Theme Rules
- Support at least 4 predefined themes (recommended 5):
  - `light`
  - `dark`
  - `colorful`
  - `high-contrast`
  - `warm` (or `minimal`)
- Use CSS variables for theme tokens (background, surface, text, accent, border).
- Keep one active default theme per course; default is `light` unless explicitly changed.
- Ensure accessibility and readability across all presets.

## Home Page Rules
- Module index with links.
- Labs section with title + description + links.
- Bibliography + Sitography sections.
- Footer note: selected/edited educational content.

## Quality Gate (before publish)
- No incomplete sentences.
- No broken references or missing images.
- No Italian text in generated English pages.
- No references to book internal structure unless required by learning flow.
- Module nav chain is correct (`prev/current/next`).
- Module structure has both levels (`1` and `1.1`) and is not flat.
- In-module structure tree shows visual indentation for level 2 under level 1.
- In-module structure tree highlights the active section while reading.
- Anchor jumps do not hide headings under sticky navigation/header.
- Structure tree is in an internal left frame and does not overlap breadcrumb/header.
- Print button works on each module.
- Printed output keeps section headings/figures readable and excludes UI controls (nav, back-to-top, print button).
