#!/usr/bin/env python3
"""Validate the mechanical structure of one SDD feature specification."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = {
    "requirements.md": (
        "## Status",
        "## Outcome",
        "## Users",
        "## In Scope",
        "## Out of Scope",
        "## Business Rules",
        "## Acceptance Criteria",
        "## Open Questions",
    ),
    "design.md": (
        "## Context",
        "## Proposed Approach",
        "## Components Affected",
        "## Data and Access Boundaries",
        "## Interfaces",
        "## Decisions and Tradeoffs",
        "## Risks",
        "## Open Questions",
    ),
    "tasks.md": (
        "## Status",
        "## Active Slice",
        "## Implementation Boundary",
        "## Tasks",
        "## Verification Gate",
        "## Blocked Decisions",
        "## Progress Log",
    ),
}

ALLOWED_STATUSES = {
    "requirements.md": {"Draft", "Approved", "Implementing", "Verified"},
    "tasks.md": {"Not Started", "In Progress", "Blocked", "Verified"},
}

PLACEHOLDER_PATTERNS = (
    re.compile(r"<[^>\n]+>"),
    re.compile(r"Draft \| Approved \| Implementing \| Verified"),
    re.compile(r"Not Started \| In Progress \| Blocked \| Verified"),
)


def section_body(text: str, heading: str) -> str:
    lines = text.splitlines()
    try:
        start = lines.index(heading) + 1
    except ValueError:
        return ""

    body: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        body.append(line)
    return "\n".join(body).strip()


def validate_file(path: Path, headings: tuple[str, ...]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    if not text.strip():
        return [f"{path}: file is empty"]
    if not text.startswith("# "):
        errors.append(f"{path}: first line must be an H1 title")

    for heading in headings:
        if heading not in text:
            errors.append(f"{path}: missing required heading {heading!r}")

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.rstrip() != line:
            errors.append(f"{path}:{line_number}: trailing whitespace")

    for pattern in PLACEHOLDER_PATTERNS:
        match = pattern.search(text)
        if match:
            errors.append(f"{path}: unresolved template placeholder {match.group(0)!r}")

    allowed = ALLOWED_STATUSES.get(path.name)
    if allowed is not None:
        status = section_body(text, "## Status").splitlines()
        value = status[0].strip() if status else ""
        if value not in allowed:
            expected = ", ".join(sorted(allowed))
            errors.append(f"{path}: invalid status {value!r}; expected one of {expected}")

    return errors


def meaningful_bullets(body: str) -> list[str]:
    return [
        line.strip()[2:].strip()
        for line in body.splitlines()
        if line.strip().startswith("- ")
        and line.strip()[2:].strip().lower() not in {"none", "none."}
    ]


def validate_cross_file(spec_dir: Path, contents: dict[str, str]) -> list[str]:
    errors: list[str] = []
    requirements = contents["requirements.md"]
    tasks = contents["tasks.md"]

    if not meaningful_bullets(section_body(requirements, "## Acceptance Criteria")):
        errors.append(f"{spec_dir / 'requirements.md'}: acceptance criteria must contain at least one bullet")

    if not re.search(r"^- \[[ xX]\] ", section_body(tasks, "## Tasks"), re.MULTILINE):
        errors.append(f"{spec_dir / 'tasks.md'}: tasks must contain at least one checkbox")

    requirements_status_lines = section_body(requirements, "## Status").splitlines()
    requirements_status = requirements_status_lines[0].strip() if requirements_status_lines else ""
    open_questions = meaningful_bullets(section_body(requirements, "## Open Questions"))
    if requirements_status in {"Approved", "Implementing", "Verified"} and open_questions:
        errors.append(
            f"{spec_dir / 'requirements.md'}: status {requirements_status!r} is incompatible with unresolved open questions"
        )

    task_status_lines = section_body(tasks, "## Status").splitlines()
    task_status = task_status_lines[0].strip() if task_status_lines else ""
    blocked_decisions = meaningful_bullets(section_body(tasks, "## Blocked Decisions"))
    if task_status == "Blocked" and not blocked_decisions:
        errors.append(f"{spec_dir / 'tasks.md'}: Blocked status requires at least one blocked decision")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec_dir", type=Path, help="Directory containing requirements.md, design.md, and tasks.md")
    args = parser.parse_args()
    spec_dir = args.spec_dir

    if not spec_dir.is_dir():
        print(f"Spec validation failed: {spec_dir} is not a directory", file=sys.stderr)
        return 1

    errors: list[str] = []
    contents: dict[str, str] = {}
    for filename, headings in REQUIRED_FILES.items():
        path = spec_dir / filename
        if not path.is_file():
            errors.append(f"{path}: required file is missing")
            continue
        contents[filename] = path.read_text(encoding="utf-8")
        errors.extend(validate_file(path, headings))

    if len(contents) == len(REQUIRED_FILES):
        errors.extend(validate_cross_file(spec_dir, contents))

    if errors:
        print(f"Spec validation failed: {spec_dir}", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Spec validation passed: {spec_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
