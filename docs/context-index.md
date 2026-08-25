# Context Index

Use this page as the low-discovery entry point for a future agent. Read the
global operating agreement first, then the task-specific pack. Query live
interfaces only to confirm volatile facts.

## Always read

1. [`AGENTS.md`](../AGENTS.md) — loop, permission, safety, and validation.
2. [`DISCOVERY.md`](../DISCOVERY.md) — adaptive discovery and evidence ledger.
3. [`docs/concepts/source-of-truth.md`](concepts/source-of-truth.md) — where each
   kind of truth belongs.
4. The current [`HANDOFF.template.md`](../HANDOFF.template.md) copy, if the
   derivative repository has one.

## Task packs

| Task | Read | Live confirmation | Acceptance evidence |
| --- | --- | --- | --- |
| Architecture | `architecture/decision-guide.md`, `architecture/reference-model.md`, context, inventory | host/guest facts and constraints | ADR with compared options |
| Home Assistant | `home-assistant/ownership.md`, household context | supported HA API/MCP and device state | human-useful control/status test |
| Voice | `voice/decision-tree.md`, `ai/local-vs-cloud.md` | pipeline, language, latency, fallback | bilingual/room test where relevant |
| Host/service change | `operations/checkpoint-runbook.md`, service desired state | OS/runtime health and dependencies | health, resource, rollback tests |
| Backup/recovery | `backups/restore-proof.md` | backup metadata, key availability, staging space | isolated restore proof |
| Monitoring | `monitoring/strategy.md` | current alerts and target reachability | alert fires and clears |
| Workflow | `workflows/ownership.md` | current owners and APIs | idempotency/retry/manual recovery |
| Migration | `migration/migrate-existing-platform.md` | source and destination inventory | cutover plus rollback test |

## Do not infer

- A desired version is not proof that it is running.
- A snapshot is not proof of restore.
- A service being reachable is not proof that its data is backed up.
- An exposed HA entity is not automatically suitable for voice.
- A GPU is not an always-on AI worker.
- A cloud model is not allowed to see all home or infrastructure data.

## Evidence conventions

Use dated, sanitized observations. Include the command/API class and the test
result, not raw secrets or unrelated logs. Mark uncertain claims explicitly and
link the next verification task.
