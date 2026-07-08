#!/usr/bin/env python3
"""Check that real lesson pages use the shared /teach lesson components."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"
LESSON_ARCHIVE = LESSONS / "archive"
ASSETS = ROOT / "assets"
ASSET_ARCHIVE = ASSETS / "archive"

ARCHIVE_PATTERNS = (
    re.compile(r".*-style-v\d+\.html$"),
    re.compile(r".*-style-gallery\.html$"),
    re.compile(r".*-palette-gallery\.html$"),
)

ARCHIVED_ASSET_DIRS = (
    "assets-v2",
    "assets-v3",
    "assets-v4",
    "assets-v4-palette",
    "assets-v5",
    "assets-v6",
)

REQUIRED_CSS = '../assets/style.css'
REQUIRED_JS = '../assets/quiz.js'
REQUIRED_COMPONENTS = (
    'class="hero"',
    'class="eyebrow"',
    'class="lesson-block"',
    'class="quiz-shell"',
    'id="quiz-root"',
    'window.quizData',
)


def is_archive_name(path: Path) -> bool:
    return any(pattern.fullmatch(path.name) for pattern in ARCHIVE_PATTERNS)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []
    top_level_html = sorted(LESSONS.glob('*.html'))
    real_lessons = [path for path in top_level_html if not is_archive_name(path)]
    misplaced_archive_lessons = [path for path in top_level_html if is_archive_name(path)]
    archived_lessons = sorted(LESSON_ARCHIVE.glob('*.html')) if LESSON_ARCHIVE.exists() else []

    if misplaced_archive_lessons:
        for path in misplaced_archive_lessons:
            fail(f'{path.relative_to(ROOT)}: archive/style experiment HTML should live under lessons/archive/', failures)
    if not (ASSETS / 'style.css').is_file():
        fail('missing assets/style.css', failures)
    if not (ASSETS / 'quiz.js').is_file():
        fail('missing assets/quiz.js', failures)
    if not (ASSETS / 'LESSON_COMPONENTS.md').is_file():
        fail('missing assets/LESSON_COMPONENTS.md', failures)
    if not (LESSON_ARCHIVE / 'README.md').is_file():
        fail('missing lessons/archive/README.md', failures)
    if not (ASSET_ARCHIVE / 'README.md').is_file():
        fail('missing assets/archive/README.md', failures)
    if not real_lessons:
        fail('no real lesson HTML files found', failures)

    for folder in ARCHIVED_ASSET_DIRS:
        if not (ASSET_ARCHIVE / folder / 'style.css').is_file():
            fail(f'missing archived asset stylesheet assets/archive/{folder}/style.css', failures)
        if (ROOT / folder).exists():
            fail(f'old versioned asset folder still at repo root: {folder}/', failures)

    for path in archived_lessons:
        text = path.read_text()
        rel = path.relative_to(ROOT)
        if '../assets-v' in text or 'href="../assets' in text or 'src="../assets' in text:
            fail(f'{rel}: archive links should be rewritten for lessons/archive/ depth', failures)
        if '-style-' in path.name and 'assets/archive/' not in text:
            fail(f'{rel}: archived style experiment should point at assets/archive/', failures)

    for path in real_lessons:
        text = path.read_text()
        rel = path.relative_to(ROOT)
        if REQUIRED_CSS not in text:
            fail(f'{rel}: missing {REQUIRED_CSS}', failures)
        if 'assets-v' in text or 'assets/archive/' in text:
            fail(f'{rel}: real lesson references archive/versioned style experiment assets', failures)
        if 'border-left:' in text:
            fail(f'{rel}: inline/decorative left stripe found in lesson HTML', failures)
        if REQUIRED_JS not in text:
            fail(f'{rel}: missing {REQUIRED_JS}', failures)
        for marker in REQUIRED_COMPONENTS:
            if marker not in text:
                fail(f'{rel}: missing component marker {marker}', failures)
        if 'class="warning"' in text:
            fail(f'{rel}: use read-card step cue instead of old warning block', failures)
        if 'real teaching before the quiz' in text.lower():
            fail(f'{rel}: contains meta placeholder copy instead of lesson content', failures)

    css = (ASSETS / 'style.css').read_text() if (ASSETS / 'style.css').exists() else ''
    required_css_markers = (
        '.read-card',
        '.step-row',
        '.step-dot',
        '.step-label',
        '.route-steps',
        '.example-grid',
        '.memory-grid',
        '.primary-button.secondary',
        'white-space: nowrap',
    )
    for marker in required_css_markers:
        if marker not in css:
            fail(f'assets/style.css: missing {marker}', failures)
    old_palette_markers = ('--ink:', '--accent:', '--paper:', 'border-left: 5px')
    for marker in old_palette_markers:
        if marker in css:
            fail(f'assets/style.css: old palette/decorative marker remains: {marker}', failures)

    print(f'REAL_LESSON_COUNT={len(real_lessons)}')
    print(f'ARCHIVED_HTML_COUNT={len(archived_lessons)}')
    print(f'ARCHIVED_ASSET_DIR_COUNT={len(ARCHIVED_ASSET_DIRS)}')
    for path in real_lessons:
        print(f'REAL_LESSON={path.relative_to(ROOT)}')
    if archived_lessons:
        print('ARCHIVED_HTML=' + ','.join(str(path.relative_to(ROOT)) for path in archived_lessons))
    print('ARCHIVED_ASSET_DIRS=' + ','.join(f'assets/archive/{folder}' for folder in ARCHIVED_ASSET_DIRS))

    if failures:
        print('CHECK_LESSON_COMPONENTS: FAIL')
        print('FAILURES:')
        for item in failures:
            print(f'- {item}')
        return 1

    print('CHECK_LESSON_COMPONENTS: PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
