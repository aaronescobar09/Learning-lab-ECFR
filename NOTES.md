# Notes

## Audience

GTC customers who bought courses for their certifications. Tone should be professional, clear, confidence-building, and exam-practical.

## Core constraint

Students need to learn how to navigate Title 19/eCFR during study, but they cannot use eCFR during the exam. The quiz should therefore train recall and mental navigation, not live-search dependency.

## Initial quiz goal

Create an interactive `/teach` lesson that helps students practice Title 19 CFR navigation:

1. Identify the structure: Title -> Chapter -> Part -> Section -> Paragraph.
2. Read citations such as `19 CFR 111.28(b)`.
3. Recognize common/high-value Title 19 parts by topic.
4. Answer exam-style multiple-choice questions with feedback explaining the navigation logic.

## Seed examples from source input

- Drawback is addressed in Part 190: Modernized Drawback.
- Customs Broker licensing is addressed in Part 111: Customs Brokers.
- 19 CFR 11.1 is about cigars, cigarettes, medicinal preparations, and perfumery within Part 11: Packing and Stamping; Marking.

## Quiz design rules from `/teach`

- Use retrieval practice: ask first, then teach through feedback.
- Give immediate feedback in the browser.
- Keep answer choices similar in form and length where possible so formatting does not reveal the answer.
- Every correct answer should have an official-source basis.
- Feedback should explain how to navigate to the answer, not just say "correct" or "incorrect".
- Avoid overloading the first quiz; make one tight win.

## Recommended first lesson artifact

```text
lessons/0001-title-19-navigation-quiz.html
```

Likely supporting files:

```text
assets/style.css
assets/quiz.js
reference/title-19-navigation-map.html
```

## Build checklist for the first quiz

1. Re-verify current eCFR structure for the target parts and sections.
2. Decide first quiz size: recommended 8-10 questions.
3. Include the 3 provided sample questions, rewritten only if needed for consistency.
4. Add 5-7 new questions that test the same skill without depending on live eCFR during the exam.
5. Write short feedback for each answer.
6. Create a clean HTML lesson with immediate-feedback quiz behavior.
7. Visually verify the quiz in a browser or screenshot, not just by reading files.
8. Commit the finished quiz as a local savepoint.

## Course-owner feedback

- 2026-07-08: A lesson file must contain real teaching before the quiz. A quiz-only page is not enough for `/teach`; use lesson first, quiz second.
- 2026-07-08: The approved lesson visual system lives in `assets/style.css`; future real lessons should link `../assets/style.css` and `../assets/quiz.js`, follow `assets/LESSON_COMPONENTS.md`, and avoid archive/versioned style assets unless explicitly making a preview/archive page. Old preview HTML belongs in `lessons/archive/`; old style assets belong in `assets/archive/`. The primary/action color is Site Training Blue (`#1E73BE`, hover `#155A96`), while amber remains the read-first/learning-support cue.

