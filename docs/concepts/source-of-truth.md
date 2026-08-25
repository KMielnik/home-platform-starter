# Source of Truth Without Duplication

An AI can only operate reliably when it can distinguish what the platform is
supposed to be from what it happens to be right now. Keep each kind of truth in
one obvious place.

| Information | Home | Volatility | Good location |
| --- | --- | --- | --- |
| Why the platform exists, non-goals, vocabulary | Reviewed intent | Low | `context/` and `README.md` |
| Desired services, ownership, versions, policies | Configuration | Medium | checked-in YAML/Compose/Ansible |
| Current CPU, disk, versions, health, reachability | Runtime evidence | High | dated `inventory/observed/` |
| A hard-to-reverse choice and alternatives | Decision record | Low | `docs/adr/` |
| A repeatable procedure | Runbook | Medium | `docs/operations/` or `docs/runbooks/` |
| What a checkpoint achieved and what was learned | History | Low | `docs/outcomes/` |
| Ideas not yet approved | Future work | High | `docs/future/` or a roadmap |
| Current next task | Handoff | High | `HANDOFF.md` |

## Authority rules

When facts conflict, classify the conflict rather than silently selecting a
convenient answer:

1. Runtime evidence wins for volatile facts, with a timestamp.
2. Reviewed desired state wins for intended behavior.
3. Historical notes explain why a decision happened; they do not make an old
   state current.
4. An inference stays an inference until confirmed.

## The context index

Keep one navigation page that tells an agent where to look next. A good index
maps task types to context, desired state, live interface, and validation:

| Task | Read first | Inspect | Verify |
| --- | --- | --- | --- |
| Home behavior | household context, HA ownership | HA API/MCP | device action and state |
| Host/platform | architecture, inventory | hypervisor/OS tools | guest health and rollback |
| Voice | voice preferences, pipeline policy | Assist/Wyoming endpoints | language, latency, fallback |
| Backups | backup policy, recovery runbook | repository metadata/logs | isolated restore |
| New service | architecture and workflow ownership | target host/runtime | health, backup, monitoring |

The index should also identify forbidden assumptions, such as “a running
container is backed up” or “an exposed entity is safe for voice.”

## Evidence hygiene

Sanitize observations at capture time. Store counts, versions, roles, status,
and error classes when they teach the lesson; omit credentials, exact private
addresses, serials, and unrelated log noise. Link a dated observation to the
checkpoint that used it.
