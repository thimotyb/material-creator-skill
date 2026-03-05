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
  - Numbered sections (`S01`, `S02`, ...)
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
- Print button works on each module.
- Printed output keeps section headings/figures readable and excludes UI controls (nav, back-to-top, print button).
