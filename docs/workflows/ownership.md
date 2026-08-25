# Choosing the Workflow Owner

Many systems can send a notification or call an API. Pick the owner by the
semantics of the work, not by which tool is newest.

| Need | Home Assistant | Task manager | Workflow engine | Ops job/agent |
| --- | --- | --- | --- | --- |
| Device-local reaction | Best fit | No | Usually too much | No |
| Human follow-up with due date/acknowledgement | Trigger the signal | Best fit | Optional connector | No |
| Cross-system API orchestration and approval | Source/target only | Task state | Best fit | Optional |
| Host maintenance, backups, updates | Observe/notify | Human task | Proposal/approval connector | Best fit |
| Weekly report or audit | Provide data | Deliver action | Coordinate sources | Generate/verify |

## Selection test

Ask:

1. Is the trigger about a household device and must it work locally? Use HA.
2. Does a person need to acknowledge, schedule, or repeat work? Use a task
   manager.
3. Are several APIs, approvals, retries, or transformations involved? Consider
   a workflow engine.
4. Is the work privileged, host-scoped, or best expressed as code? Use an ops
   job or attended agent.

Keep one owner for state. A workflow engine may create a task, but it should not
also become a second task database. A task manager may show a failed backup, but
it should not replace the backup system’s evidence.

For every workflow document source signal, owner, idempotency key, retry policy,
human action, notification, failure mode, and manual recovery.
