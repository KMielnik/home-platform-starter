# Architecture Decision Guide

Choose the smallest architecture that meets the goals and preserves a clear
recovery path. A role is a responsibility, not necessarily a VM, LXC,
container, or physical machine.

## First branch: is virtualization justified?

Use a hypervisor when at least two of these are true:

- workloads need different operating systems or update/reboot boundaries;
- snapshots and guest isolation solve a real recovery problem;
- the person is willing to operate the host and its boot/storage path;
- hardware resources and power budget leave comfortable headroom.

Prefer an appliance plus one small management host when none are true. Existing
Home Assistant hardware should not be moved into a larger stack merely because
virtualization is fashionable.

## Role selection

| Role | Add it when | Do not add it when |
| --- | --- | --- |
| Home Assistant appliance | Household devices and deterministic automation are the goal | It would duplicate an already healthy HA appliance without a recovery benefit |
| Operations control plane | Git-backed documentation, backups, automation, or narrow AI tooling need a home | It would only be a second shell with no ownership boundary |
| Application host | Several independent household applications justify a shared runtime | One or two apps could stay on an existing appliance safely |
| AI/voice worker | Measured local speech or model latency is useful and hardware can sustain it | It would make basic Home Control depend on a hot, scarce, or gaming-priority GPU |
| Task manager | Human follow-up, recurring maintenance, or acknowledgement needs a lifecycle | An alert or HA notification is sufficient |
| Workflow engine | Cross-system orchestration, approvals, or APIs are awkward in HA/ops | A local device automation is clear in HA |

## Constraint profiles

### 8 GB RAM, no GPU

Keep the design flat and appliance-first. Reserve memory for Home Assistant and
the host OS; avoid a dedicated AI guest and large local models. Use cloud
conversation selectively or a separate phone/desktop for AI. Local speech may
be possible with small measured services, but test latency and swap pressure.
Back up configuration and use monitoring that costs little memory.

### Existing Home Assistant appliance

Preserve the appliance as household authority. Start with a source-of-truth
repository, backup/restore proof, and a narrow management plane. Add a separate
host only for a demonstrated need such as a backup repository, optional app,
or measured voice worker. Do not break a working radio topology to make the
architecture look symmetrical.

### Powerful GPU workstation

Treat the GPU as an optional burst worker. Keep Home Control, local speech
fallback, and recovery independent of a workstation that may be asleep or busy.
Use an authenticated, narrow model endpoint if needed; set power, thermal, and
availability expectations. Do not expose a general shell through voice.

### Existing Proxmox host

Inventory storage, boot recovery, guest boundaries, backup coverage, and
reboot access before reusing it. Start with one manually understood guest per
responsibility. A host that cannot be recovered without a physical console is
an attended operational dependency, not a reason to automate firewall or kernel
changes.

### Cloud-first AI

Keep device intent and speech routing local where practical. Send only the
conversation or data needed for the selected query to the provider. Define
retention, cost, outage behavior, and tool allowlists. Cloud quality does not
justify exposing maintenance controls.

### Full-local AI

Measure model memory, cold start, sustained latency, language quality, power,
thermals, and update burden on the actual machine. Start with local STT/TTS and
deterministic Home Control; add a conversational model only if the remaining
work is worth the cost. Maintain a local fallback and a rollback profile.

## Compare options explicitly

Use this table in an ADR:

| Criterion | Minimal | Separated roles | Local-AI extension |
| --- | --- | --- | --- |
| Hardware fit | | | |
| Failure domains | | | |
| Operational effort | | | |
| Privacy/cost | | | |
| Recovery proof | | | |
| Future migration | | | |
| What remains unavailable | | | |

Recommend one option only after the person has seen the trade-offs and the
next checkpoint is reversible.
