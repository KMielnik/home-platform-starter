# Privacy and Sanitization

Before sharing a derivative of this starter, inspect the complete working tree
and Git history for:

- names, email addresses, usernames, private URLs, precise locations, and
  account identifiers;
- private IPv4/IPv6 addresses, host aliases, MAC addresses, serials, appliance
  identifiers, backup IDs, tokens, keys, and secret-like values;
- raw Home Assistant storage, databases, logs, screenshots, and exports;
- household schedules or room details that are not needed to teach the idea;
- provider, indexer, or acquisition/download implementation details.

Use labels such as `<management-address>`, `<device-name>`, and
`${SECRET_FROM_MANAGER}` only in clearly illustrative examples. Do not put
real values in examples, commit history, issue text, or screenshots.

Run `python scripts/validate_repo.py` and perform a human review before making
any derivative public. The validator checks the working tree plus reachable
Git history: commit identity metadata, commit subjects, and tracked blobs.
Review other refs, reflogs, and any copies of the repository separately before
publishing. A clean scanner is useful evidence, not a substitute for
judgment.
