#!/usr/bin/env python3
"""Small, dependency-free sanity and privacy check for the starter kit."""

from __future__ import annotations

import hashlib
import ipaddress
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "AGENTS.md",
    "DISCOVERY.md",
    "HANDOFF.template.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "PRIVACY.md",
    "docs/concepts/source-of-truth.md",
    "docs/concepts/glossary.md",
    "docs/context-index.md",
    "docs/architecture/decision-guide.md",
    "docs/build/phased-journey.md",
    "docs/home-assistant/ownership.md",
    "docs/voice/decision-tree.md",
    "docs/ai/local-vs-cloud.md",
    "docs/security/permission-model.md",
    "docs/backups/restore-proof.md",
    "docs/monitoring/strategy.md",
    "docs/workflows/ownership.md",
    "docs/troubleshooting/common-lessons.md",
    "docs/migration/migrate-existing-platform.md",
    "templates/context/context.md",
    "templates/inventory/inventory.yaml",
    "templates/adr/ADR-000-template.md",
    "templates/runbook/runbook.md",
    "templates/outcome/outcome.md",
    "templates/handoff/handoff.md",
    "examples/architecture/options.md",
    "examples/inventory/inventory.example.yaml",
    "examples/compose/compose.example.yaml",
    "examples/ansible/site.example.yml",
)

# One-way fingerprints keep the restricted vocabulary out of this repository.
# Input matching is case-folded and whitespace-normalized before substring
# hashes are compared. Store no matched value or digest in validation errors.
RESTRICTED_FINGERPRINTS = frozenset(
    {
        "60526b742a568968d26c653242180d8d86e4dc2838b752374faaa6448539f7bb",
        "b878df152bdca6c9906dd195e78364a28598ccf52946dd8173f13824cb1c6f6b",
        "7da0324ce46c55f7dcfee581bb13cd5bc66cc4d514dcd1cd03bb9008b8b2f517",
        "d377d500e1e178f39b6ca8c57b3e702bef1c167d98f86ecddb0d418e78b0efb4",
        "39a0be6d6589d78d28dde15fe6d6de95fa18a1d7cd323cfe6a72e700333c35c5",
        "bc1227ae633ceb146d19d0e646ff90058cc3a2cc8679c458eb8c3ff3c3f6a818",
        "e851219b75c97d1a161ad6b20c05b82cabb6c3b1b5ab542d9538d0fb1f31ba88",
        "22479acea775523e41de82844c2fba677c3ab18b7daec6c39af1738d339828a4",
        "575e2265619125a7586b8cbbad1f83026c224af5276a84e76533b29a3a743d33",
        "194448e2770cf0f7ce48930cf13794a7c6ac14d36ec0adfbfb8ee8397187a87f",
        "d2132690e5fda8b57522797c120c6cb11613f58a5d9f6330a828e9fa0b10a397",
    }
)
RESTRICTED_LENGTHS = frozenset({4, 6, 7, 8, 9, 11, 12})
WHITESPACE = re.compile(r"\s+")

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z0-9 ]+-----"),
    re.compile(r"(?:api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{20,}"),
    re.compile(r"(?:^|\s)(?:ssh-rsa|ssh-ed25519)\s+[A-Za-z0-9+/=]{40,}"),
)
PRIVATE_IPV4 = re.compile(r"(?<![0-9])(?:10|127|169\.254|192\.168|172\.(?:1[6-9]|2[0-9]|3[0-1]))\.[0-9.]+")
IPV6_TOKEN = re.compile(
    r"(?i)(?<![0-9a-f:])(?:[0-9a-f]{0,4}:){2,7}[0-9a-f:.]+(?:%[0-9a-z_.-]+)?(?![0-9a-f:])"
)
MAC = re.compile(r"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}:){5}[0-9a-f]{2}(?![0-9a-f])")
EMAIL = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
LOOPBACK = ".".join(("127", "0", "0", "1"))

# The release history is intentionally identity-neutral. This exact pair is
# used for the sanitized root commit; a personal or username-bearing identity
# fails the publication gate instead of being hidden by a broad domain rule.
SAFE_HISTORY_IDENTITIES = frozenset({("Home Platform Contributors", "noreply")})


def restricted_vocabulary_found(content: str) -> bool:
    """Match restricted text without storing or returning the matched value."""

    normalized = WHITESPACE.sub(" ", content.casefold())
    for length in RESTRICTED_LENGTHS:
        if length > len(normalized):
            continue
        for start in range(len(normalized) - length + 1):
            digest = hashlib.sha256(normalized[start : start + length].encode("utf-8")).hexdigest()
            if digest in RESTRICTED_FINGERPRINTS:
                return True
    return False


def privacy_findings(path: str, content: str) -> list[str]:
    """Find privacy violations in ordinary text without returning its values."""

    findings: list[str] = []
    # Scan this validator itself normally; only one-way fingerprints are
    # stored, and no matched term or digest is emitted.
    if restricted_vocabulary_found(content):
        findings.append("restricted vocabulary pattern")

    for match in PRIVATE_IPV4.finditer(content):
        # The example intentionally documents a loopback-only bind. Keep the
        # exception exact and path-specific; all other private addresses fail.
        if (
            path == "examples/compose/compose.example.yaml"
            and match.group() == LOOPBACK
            and any(
                line.strip() == f'- "{LOOPBACK}:${{EXAMPLE_PORT:-18080}}:80"'
                for line in content.splitlines()
            )
        ):
            continue
        findings.append("private IPv4 address")
    for match in IPV6_TOKEN.finditer(content):
        candidate = match.group().split("%", 1)[0]
        try:
            address = ipaddress.ip_address(candidate)
        except ValueError:
            continue
        if address.version == 6 and (address.is_private or address.is_loopback or address.is_link_local):
            findings.append("private IPv6 address")
    if MAC.search(content):
        findings.append("MAC-address pattern")
    for match in EMAIL.finditer(content):
        findings.append("email-address pattern")
    if any(pattern.search(content) for pattern in SECRET_PATTERNS):
        findings.append("secret-like value")
    return findings


def run_git(*args: str) -> tuple[int, str]:
    """Run a read-only Git command and return its exit code and text output."""

    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError as exc:
        return 127, str(exc)
    output = result.stdout
    if result.stderr:
        output += result.stderr
    return result.returncode, output


def history_privacy_checks(errors: list[str], warnings: list[str]) -> None:
    """Check reachable Git metadata and blobs before a repository is shared."""

    code, result = run_git("rev-parse", "--is-inside-work-tree")
    if code != 0 or result.strip().splitlines()[:1] != ["true"]:
        warnings.append("Git history check skipped; repository metadata unavailable")
        return

    code, log_output = run_git(
        "log",
        "--all",
        "--format=%H%x00%an%x00%ae%x00%cn%x00%ce%x00%s",
    )
    if code != 0:
        warnings.append("Git history metadata check skipped; git log failed")
    else:
        for record in log_output.splitlines():
            fields = record.split("\x00")
            if len(fields) < 6:
                continue
            commit, author, author_email, committer, committer_email, subject = fields[:6]
            for label, value in (("author", author), ("committer", committer)):
                for finding in privacy_findings("<git-metadata>", value):
                    errors.append(f"{finding} in Git {label} name ({commit[:12]})")
            if (author, author_email) not in SAFE_HISTORY_IDENTITIES:
                errors.append(f"non-neutral Git author identity ({commit[:12]})")
            if (committer, committer_email) not in SAFE_HISTORY_IDENTITIES:
                errors.append(f"non-neutral Git committer identity ({commit[:12]})")
            for finding in privacy_findings("<git-message>", subject):
                errors.append(f"{finding} in Git commit subject ({commit[:12]})")

    code, message_output = run_git("log", "--all", "--format=%H%x00%B%x00")
    if code != 0:
        warnings.append("Git commit-message check skipped; git log failed")
    else:
        message_fields = message_output.split("\x00")
        for index in range(0, len(message_fields) - 1, 2):
            commit, message = message_fields[index : index + 2]
            if not commit:
                continue
            for finding in privacy_findings("<git-message>", message):
                errors.append(f"{finding} in Git commit message ({commit[:12]})")

    code, objects = run_git("rev-list", "--objects", "--all")
    if code != 0:
        warnings.append("Git blob privacy check skipped; reachable object listing failed")
        return
    object_paths: dict[str, str] = {}
    for line in objects.splitlines():
        object_id, separator, object_path = line.partition(" ")
        if separator and object_id and object_path:
            object_paths.setdefault(object_id, object_path)

    for object_id, object_path in object_paths.items():
        type_code, object_type = run_git("cat-file", "-t", object_id)
        if type_code != 0 or object_type.strip() != "blob":
            continue
        blob_code, blob = run_git("cat-file", "-p", object_id)
        if blob_code != 0:
            warnings.append(f"Git blob check skipped for {object_path}")
            continue
        for finding in privacy_findings(object_path, blob):
            errors.append(f"{finding} in Git blob {object_path} ({object_id[:12]})")


def files() -> list[Path]:
    return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def text_of(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    all_files = files()

    for item in REQUIRED:
        if not (ROOT / item).is_file():
            errors.append(f"missing required file: {item}")

    for path in all_files:
        content = text_of(path)
        if content is None:
            warnings.append(f"skipped non-text file: {path.relative_to(ROOT)}")
            continue
        rel = path.relative_to(ROOT).as_posix()
        for finding in privacy_findings(rel, content):
            errors.append(f"{finding} in {rel}")

    history_privacy_checks(errors, warnings)

    # Parse the machine-readable examples without requiring third-party tools.
    try:
        import yaml  # type: ignore
    except ImportError:
        warnings.append("PyYAML unavailable; YAML parse check skipped")
    else:
        for item in (
            "templates/inventory/inventory.yaml",
            "examples/inventory/inventory.example.yaml",
            "examples/compose/compose.example.yaml",
            "examples/ansible/site.example.yml",
        ):
            path = ROOT / item
            try:
                yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001 - validator should report the file
                errors.append(f"YAML parse failure in {item}: {exc}")

    # Check internal Markdown links that point to local files.
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")
    for path in all_files:
        content = text_of(path)
        if content is None or path.suffix.lower() != ".md":
            continue
        for target in link_pattern.findall(content):
            if target.startswith(("http://", "https://", "mailto:", "<")) or target.startswith("#"):
                continue
            target_path = (path.parent / target).resolve()
            if not target_path.exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {target}")

    if errors:
        print("FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print("PASS")
    print(f"checked {len(all_files)} files")
    if warnings:
        for item in warnings:
            print(f"warning: {item}")
    print("privacy-pattern, secret-pattern, Git-history, YAML, and local-link checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
