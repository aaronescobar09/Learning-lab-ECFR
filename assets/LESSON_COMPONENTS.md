# Lesson Components

This workspace follows the `/teach` skill rule: lesson UI is built from reusable components in `./assets/`, not one-off inline styling.

## Required includes

Every real lesson HTML file in `lessons/` should use the shared lesson assets:

```html
<link rel="stylesheet" href="../assets/style.css">
<script src="../assets/quiz.js"></script>
```

Style experiment, gallery, and archive files live under `lessons/archive/` and may use archived styles under `assets/archive/`. New course lessons should not link archive/versioned assets.

## Reference documents

Reference documents in `reference/` are compressed quick-reference sheets, not lessons. They link the shared lesson base first, then a reference-only stylesheet:

```html
<link rel="stylesheet" href="../assets/style.css">
<link rel="stylesheet" href="../assets/reference.css">
```

`reference.css` is scoped entirely under `.reference-page`, so it restyles reference sheets (polished tables, quiet muted section labels, white/stone surfaces, one subtle amber study note) without touching the lesson system. Use `<main class="page reference-page">` with `.ref-head`/`.ref-eyebrow`/`.ref-lede`/`.ref-note`, `.ref-section` cards with an `<h2>` rule, and `.ref-table-wrap` + `<table class="ref-table">` for tables (styled header, row dividers, horizontal overflow safety). Reserve primary blue for real clickable actions; `.primary-button.secondary` is fine for navigation like "return to lesson".

## Component contract

| Purpose | Use | Rule |
|---|---|---|
| Page shell | `<main>` | Keep lessons self-contained and readable. |
| Hero card | `.hero` | Lesson title, short purpose, read-first cue, primary links. |
| Section label | `.eyebrow` | Muted text/rule label near body size. Do **not** use pill/bubble chrome for non-clickable titles. |
| Section card | `.lesson-block` | Main teaching blocks before the quiz. |
| Read-first cue | `.read-card.step-cue` with `.step-row`, `.step-dot`, `.step-label` | Amber support card for exam constraints or "read before answering" guidance. |
| Primary action | `.primary-button` | Primary blue is for the main CTA and quiz highlighted states only. |
| Secondary action | `.primary-button.secondary` | Stone/white pill chrome is for clickable secondary buttons only. |
| CFR citation chip | `<code>` | Quiet stone chip; keep citations together with nowrap. |
| Annotated lesson image | `.lesson-figure` with `<picture>` | Use separate desktop/mobile assets when annotations would become unreadable on a phone. For interface orientation, prefer a cropped capture of the real official interface with browser chrome and unrelated tabs removed. Add useful alt text and a source-aware caption. |
| Route cards | `.route-steps` | Four-step map cards: Title, Chapter, Part, Section. |
| Worked example cards | `.example-grid` | Small amber support cards for breaking down citations. |
| Memory cards | `.memory-grid` | Small amber support cards for recall targets. |
| Compact procedure | `.compact-list` | Ordered study steps. |
| Quiz mount | `.quiz-shell` + `#quiz-root` | Use shared `../assets/quiz.js` and page-local `window.quizData`. |
| Source note | `.source-note` | Official source, scope, disclaimer, and follow-up prompt. |

## Color rules

- White/stone: base surfaces, section labels, headings, neutral text, citations.
- Primary blue (Site Training Blue `#1E73BE` / hover `#155A96`): primary CTA, quiz option hover/focus, correct answer states.
- Amber: learning-support/read-first cards and route/example/memory support cards.
- Do not use pill/bubble styling for static titles like `Worked example` or `What you are learning`.

## New lesson checklist

1. Start from an existing real lesson, not a style experiment.
2. Link `../assets/style.css` and `../assets/quiz.js`.
3. Teach before the quiz: learning goal, worked example, memory/retrieval support, then quiz.
4. Keep answer choices similarly shaped so formatting does not reveal the answer.
5. Do not preview exact quiz answers in pre-quiz teaching. Teach the transferable method with a separate example, then reveal answer-specific explanations only after a response.
6. Use the shared quiz renderer's shuffled choice order rather than keeping correct answers in a predictable position.
7. Cite official/government source material for factual claims.
8. Run `python3 scripts/check-lesson-components.py` before sharing or committing.
9. Visually inspect desktop and mobile screenshots when a lesson contains annotated imagery.
