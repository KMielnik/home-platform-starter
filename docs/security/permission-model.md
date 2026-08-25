# AI Permission Models

An AI is useful because it can inspect and coordinate many systems. That is
also why its authority must be explicit.

## Two axes

Record both the **mode** and the **scope**.

| Mode | Meaning | Suitable default |
| --- | --- | --- |
| Attended | Agent proposes; person approves each consequential action | Yes |
| Bounded autonomous | Person names exact targets, commands, time window, and rollback; agent may execute within that boundary | Only after trust is earned |
| Unrestricted autonomous | Agent may choose broad changes or destructive actions | Do not use for a home platform |

Scope should name host/guest, files, services, and action types. “Manage the
server” is not a scope.

## Capability tiers

| Tier | Example | Voice/LLM default |
| --- | --- | --- |
| Observe | status, inventory, logs with secrets redacted | Allowed through narrow read-only tools |
| Explain | summarize health or propose a change | Allowed |
| Reversible action | restart one known service, create a temporary test | Attended or explicitly bounded |
| Durable configuration | edit desired state, apply an update | Attended |
| Security boundary | firewall, credentials, public exposure, identity | Attended with recovery path |
| Destructive | delete data/guest, wipe disk, revoke recovery | Human-only, deliberate runbook |

## Approval record

Before bounded autonomy, record:

- principal and human owner;
- exact targets and allowed commands/tools;
- start/end time or expiry;
- forbidden actions;
- backup and rollback path;
- success tests and stop conditions;
- how logs are redacted.

## Household voice boundary

Voice can control a lamp or ask whether a service is healthy. It should not
implicitly administer a hypervisor, open a firewall, rotate keys, expose a
container, or read secret-bearing logs. Use a separate attended operations
channel for those tasks.
