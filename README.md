# Learning Lab: eCFR Title 19 Navigation

A small `/teach` workspace for GTC certification students learning how to navigate Title 19 of the CFR.

## Published site

GitHub Pages serves the course as static HTML.

- Course home: `index.html`
- Lesson 0001: `lessons/0001-title-19-navigation-quiz.html`
- Reference map: `reference/title-19-navigation-map.html`

## Local verification

```bash
python3 scripts/check-lesson-components.py
```

The lessons are plain HTML/CSS/JS. Keep reusable lesson components in `assets/` and real lessons directly under `lessons/`.
