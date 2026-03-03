# Agent Instructions (Simple Course Workflow)

Use this workflow for every edit request.

## 1) Locate and Understand
- Find module + section in `site/chapters/chapter-XX.html`.
- If text is unclear/incomplete, check original chapter in `resources/chXX.docx`.
- Prefer faithful meaning from source, then rewrite to clean study style.

## 2) Edit Rules
- Keep existing HTML structure and CSS classes.
- Keep section numbering and figure numbering format.
- Preserve internal links and navigation.
- Write concise, neutral English.
- If request conflicts with previous style rules, apply latest explicit user instruction.
- Keep selected theme consistent (`light|dark|colorful|high-contrast|warm`).

## 3) Figure Handling
- Place figures in `site/assets/images/chXX/`.
- Add semantic captions.
- Ensure image paths are correct from chapter HTML.
- Do not duplicate identical assets unnecessarily.

## 4) Validation
- Check target sentence/section exists after edit.
- Check no broken HTML around modified area.
- Check links and image references with `rg`.
- Check theme variables exist and are coherent with selected preset.
- Ensure request is fully applied before stopping.

## 5) Publish
- Publish after each accepted change:
  - `scripts/publish-site.sh https://github.com/<USER>/<PUBLIC-SITE-REPO>.git main`
- Report what changed and where.

## Quick Command Pattern
- Search text: `rg -n "text" site/chapters/chapter-*.html`
- Verify links/images: `rg -n "chapter-08|fig-08|https://..." site/index.html site/chapters/*.html`
- Publish: `scripts/publish-site.sh <public-repo-url> main`
