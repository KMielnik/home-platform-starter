# Phased Journey: 0–11

Each phase has a purpose, exit evidence, and a safe stopping point. Do not
advance because a checklist is fashionable; advance because the prior layer is
understood and recoverable.

## Phase 0 — Discovery and source of truth

Inventory the real hardware, network, home goals, services, AI preferences,
permission model, and recovery objectives. Create context, inventory, a context
index, and the first handoff.

Exit: two architecture options, known evidence gaps, and one selected
checkpoint.

## Phase 1 — Hypervisor or base host

Install or validate the smallest base layer that fits. Record boot recovery,
storage health, time sync, access boundaries, and update policy.

Exit: host can reboot under attended control and the management path is tested.

## Phase 2 — Storage, network, and recovery foundation

Separate durable configuration from replaceable bulk data. Define naming,
mounts, network ownership, remote access, and encrypted backup destinations.

Exit: a small representative restore succeeds in isolation.

## Phase 3 — Operations control plane

Create Git authority, sanitized context, secret management, SSH boundaries,
and the agent workflow. Build one layer manually before automating repetition.

Exit: a future agent can inspect and propose without guessing access or scope.

## Phase 4 — Home Assistant

Install or preserve HA. Assign ownership for Zigbee, Thread, Matter, MQTT,
ESPHome, areas, devices, automations, dashboards, and Assist exposure.

Exit: normal household control works when optional services are unavailable.

## Phase 5 — Optional application/services host

Add only services tied to a stated goal. Pin images, isolate app data from bulk
data, define health checks, logging, backups, and user-facing access.

Exit: every service has an owner, dependency list, recovery class, and monitor.

## Phase 6 — Repeatable configuration

Automate a known-good layer with Ansible, Compose, or an equivalent tool. Keep
the desired state readable and validate it before applying.

Exit: a second run is idempotent or its intentional differences are recorded.

## Phase 7 — Backups and restore proof

Back up durable state, credentials/recovery material, and critical application
data according to a retention plan. Test restores into a temporary location;
metadata without a restore is not proof.

Exit: the person can state what can be restored, how long it takes, and what
still requires manual work.

## Phase 8 — Monitoring

Monitor host health, storage, guests/containers, critical endpoints, backup
freshness, and user-visible failures. Alert only where someone can respond.

Exit: an intentionally stopped test service produces a useful signal and the
alert can be cleared.

## Phase 9 — Voice and AI worker

Choose local/cloud speech and conversation based on measured language, latency,
privacy, cost, and hardware. Add a pilot room first. Keep deterministic Home
Control and a fallback independent of the AI worker.

Exit: voice has a tested fallback, narrow tools, and an explicit data path.

## Phase 10 — Optional workflows

Introduce a task manager or workflow engine only for cross-system state,
human acknowledgement, approvals, or integrations that do not belong in HA.

Exit: each workflow has a single owner, retry behavior, duplicate handling,
and a manual recovery path.

## Phase 11 — Future extensions

Consider energy, more sensors, satellites, burst compute, model routing,
hardware migration, or new rooms. Rank proposals by value, effort, risk,
dependency, and attended requirement. Do not turn the backlog into automatic
deployment.

## Checkpoint contract

Before closing a phase, update the inventory observation, outcome note, and
handoff. Link tests and recovery evidence. If the phase is incomplete, say so;
“not yet verified” is a useful state.
