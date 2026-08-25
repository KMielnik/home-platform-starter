# Security Model and Reporting

This repository is educational. It is not a security boundary and must not be
copied into production without adapting its examples and reviewing every
permission.

## Practical defaults

- Keep Home Assistant household control separate from infrastructure
  administration.
- Prefer tailnet/VPN or LAN-only access over public exposure.
- Use short-lived, least-privilege credentials and encrypted secret storage.
- Back up configuration and recovery material, but exclude replaceable bulk
  data unless there is a reason to retain it.
- Test restores into an isolated location.
- Treat a voice or LLM request as untrusted input; require explicit approval
  for consequential operations.
- Do not mount a host or container-management socket into an AI worker merely
  for convenience.

If you find a security issue in this repository, avoid posting private details
in a public issue. Use the project’s private reporting channel if one exists,
or provide a minimal reproducible description without credentials or personal
data.
