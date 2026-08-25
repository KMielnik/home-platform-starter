# Home Platform Starter

An AI-first, hardware-agnostic starter kit for building a home platform around
the equipment, devices, languages, budget, and risk tolerance you actually have.

This is a teaching repository, not a turnkey appliance and not a copy of one
household. A capable agent should inspect your current system, explain the
trade-offs, propose a small checkpoint, execute only within your chosen
permission model, verify the outcome, and document what changed.

## The central idea

The useful product is not a particular hypervisor, container, model, or vendor.
It is a durable operating method:

```text
source of truth + narrow interfaces + evidence + staged changes + recovery proof
```

Home Assistant remains the household control authority where it fits. An
operations control plane keeps plans, credentials, automation, backups, and
agent context understandable. Optional application, voice, and AI roles are
added only when a real need and the hardware justify them.

## Start here

1. Read [AGENTS.md](AGENTS.md) to understand the safe working agreement.
2. Follow [DISCOVERY.md](DISCOVERY.md). Let the agent inspect discoverable facts
   before it asks you questions.
3. Bootstrap the working documents below, then fill them in from the discovery
   evidence:

   ```sh
   mkdir -p context inventory docs/adr docs/outcomes
   cp templates/context/context.md context/context.md
   cp templates/inventory/inventory.yaml inventory/inventory.yaml
   cp templates/adr/ADR-000-template.md docs/adr/ADR-000-bootstrap.md
   cp templates/outcome/outcome.md docs/outcomes/OUTCOME-000-bootstrap.md
   cp templates/handoff/handoff.md HANDOFF.md
   ```

   Keep the mapping intentional: reviewed purpose and constraints go in
   `context/`, current sanitized facts go in `inventory/`, hard-to-reverse
   choices go in `docs/adr/`, checkpoint results go in `docs/outcomes/`, and
   the one next task goes in `HANDOFF.md`. The vocabulary used throughout this
   kit is defined in the [glossary](docs/concepts/glossary.md).
4. Use [the architecture decision guide](docs/architecture/decision-guide.md)
   to compare at least two viable designs.
5. Choose a phase from [the 0–11 journey](docs/build/phased-journey.md). Each
   checkpoint should leave a usable and recoverable system.
6. Keep desired state, observed state, decisions, procedures, and outcomes in
   their intended locations. The model is described in
   [docs/concepts/source-of-truth.md](docs/concepts/source-of-truth.md).

Do not paste credentials, private addresses, device serials, account names, or
raw application databases into this repository. Use placeholders and sanitized
observations.

If voice is not a current requirement, take the explicit no-voice branch:
start with deterministic Home Assistant controls and document voice as out of
scope in `context/` (and an ADR if the boundary is durable). Add speech only
after a concrete need, language, latency, privacy, and recovery test justifies
it; the rest of the platform should remain useful while that branch is absent.

The included `.gitignore` is a safety net, not a privacy strategy. Review every
new file before committing.

## The operating loop

Every meaningful change follows this loop:

```text
Inspect → Explain → Propose → Execute → Verify → Document
```

An inspection describes current evidence. An explanation teaches the mental
model. A proposal names exact scope, risk, verification, and recovery. Execution
is governed by the selected permission mode. Verification tests the requested
outcome, not merely a successful command. Documentation makes the next session
cheaper.

## Adaptation examples

There is no universal architecture. The decision guide covers, among others:

| Starting point | Likely first design question |
| --- | --- |
| 8 GB RAM, no GPU | Keep Home Assistant appliance-like; avoid a dedicated AI guest and prefer cloud or small local speech only if measured viable. |
| Existing HA appliance | Preserve its authority; add only a small management layer if it solves a concrete recovery or documentation problem. |
| Powerful GPU workstation | Treat GPU compute as optional/on-demand; never make basic Home Control depend on a gaming or burst worker. |
| Existing Proxmox host | Reuse it only if the operational cost, backup story, and failure domain are understood. |
| Cloud-first preference | Keep deterministic control local and route only selected conversational work to a provider. |
| Full-local preference | Measure language, latency, thermals, power, and maintenance cost before committing to models. |

## Repository map

- `DISCOVERY.md` — adaptive “grill me” workflow and evidence checklist.
- `AGENTS.md` — agent operating model, permission boundaries, and validation.
- `docs/concepts/` — durable mental models and source-of-truth rules.
- `docs/concepts/glossary.md` — short definitions for the platform vocabulary.
- `docs/architecture/` — role model and hardware-dependent decision logic.
- `docs/build/` — phased journey from discovery to future extensions.
- `docs/home-assistant/` — device/protocol ownership and exposure principles.
- `docs/voice/`, `docs/ai/` — local/cloud speech and conversational AI choices.
- `docs/operations/`, `docs/backups/`, `docs/monitoring/` — run and recover it.
- `docs/workflows/` — choosing HA, a task manager, n8n, or an ops job.
- `docs/security/` — practical access, secrets, and agent permissions.
- `docs/troubleshooting/`, `docs/migration/` — lessons and change paths.
- `templates/` — context, inventory, ADR, runbook, outcome, and handoff forms.
- `examples/` — safe, generic, non-deploying configuration patterns.
- `scripts/validate_repo.py` — structure, syntax, privacy-pattern, and secret-hygiene
  checks.

## What this kit deliberately does not do

- It does not assume your hardware, rooms, vendors, language, or network.
- It does not grant an agent unrestricted root access by default.
- It does not expose infrastructure administration through household voice.
- It does not turn every automation into a visual workflow.
- It does not call an unverified command “recovery.” A restore must be tested.
- It does not contain personal identifiers or a private household topology.

## License

This starter kit is released under the MIT License; see [LICENSE](LICENSE).
