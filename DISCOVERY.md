# Adaptive Discovery: Grill Me, but Only After Looking

The first job is not to choose Proxmox, Docker, a model, or a vendor. It is to
understand the person, the existing system, and the failure they are trying to
avoid. This workflow is deliberately inquisitive, but it avoids asking for
facts an agent can safely inspect.

## Discovery contract

The agent should say what it can inspect, what it cannot inspect, and what it
will do with the answers. It should collect evidence in a temporary ledger and
produce a sanitized discovery brief before proposing architecture.

For each fact, record:

| Field | Meaning |
| --- | --- |
| Fact | What was observed or stated |
| Source | Command, API, document, or person |
| Freshness | Timestamp or `stated` |
| Confidence | `verified`, `documented`, `suspected`, or `unknown` |
| Consequence | Which design choice it affects |

Never copy raw command output containing secrets or private identifiers into the
brief.

## Step 1 — Inspect before asking

With read-only access, inspect as much as is safe:

- operating system and kernel;
- CPU model, cores, memory, storage devices and free space;
- GPU/iGPU and driver visibility;
- network interfaces, link type, DNS, routes, and remote-access tooling;
- battery/UPS and expected power-loss behavior;
- existing guests, containers, Home Assistant, MQTT, Zigbee/Thread/Matter,
  dashboards, automations, backups, monitoring, and task systems;
- reachable service versions and health endpoints;
- current repository structure, desired-state files, and recent handoff.

Do not wake an offline computer, restart a service, pair a device, or change a
firewall merely to answer a discovery question. Mark it as an evidence gap.

## Step 2 — Grill the goals

Ask these in conversation, adapting to earlier answers. Skip questions already
answered by reliable evidence.

### Hardware and power

- Which machine(s) may run continuously, and which must remain available for
  another purpose?
- What downtime and boot-recovery effort are acceptable?
- Is power cost, fan noise, heat, or battery runtime a hard constraint?
- What upgrades are affordable later, and which hardware is fixed?

### Network and access

- Is the home network wired, wireless, or mixed?
- Do devices require multicast discovery, an IoT segment, or vendor clouds?
- Is remote access needed, and may it be tailnet-only, VPN-only, or public?
- How comfortable is the person with DNS, certificates, VLANs, and routing?

### Home behavior

- Which rooms and devices matter daily?
- What currently fails or feels annoying?
- Which automations are safety-critical, comfort-related, or just experiments?
- Which devices must keep working if every optional service is down?
- Which protocols or vendor accounts already exist?

### Services and operations

- Is Home Assistant already authoritative, or should it be preserved as-is?
- Are household apps, dashboards, task tracking, development tools, or optional
  media services actually wanted?
- Who will perform updates, approve changes, and respond to an alert?
- What should a future agent be allowed to inspect, propose, execute, or never
  touch?

### AI and voice

- Is AI an operator, a household assistant, or both? Keep these roles separate.
- Which languages, accents, rooms, noise levels, and latency targets matter?
- Is local processing required, preferred, or merely interesting?
- What recurring API cost is acceptable?
- Are room satellites needed now, or is phone/desktop voice sufficient?

### Recovery and learning

- What data would be painful or impossible to recreate?
- How quickly must the home recover after a host or disk loss?
- Where can an encrypted off-site recovery copy live?
- Does the person want to understand each layer, or optimize for low effort?

## Step 3 — Explore alternatives

Do not stop at one design. Produce at least two coherent options, for example:

1. a minimal appliance-first design;
2. a role-separated design with operations and optional apps;
3. a local-AI extension only if measured hardware and goals support it.

For every option show resource fit, complexity, failure domains, backup scope,
privacy, power, migration path, and what it intentionally does not provide.

## Step 4 — Decide what is enough

Discovery is sufficient when the agent can answer, with evidence:

- what must work during an optional-service outage;
- which system owns each household behavior;
- what state must be backed up and restored;
- which hardware/network constraints eliminate an option;
- whether local or cloud speech/conversation is practical;
- what the next smallest reversible checkpoint is;
- how the person can approve or roll back that checkpoint.

If an answer remains unknown, label it and choose the safest reversible path.

## Discovery brief output

Copy [the context template](templates/context/context.md) and record:

- goals and non-goals;
- discovered hardware and network summary without private identifiers;
- device/protocol ownership;
- data classes and recovery objectives;
- AI/voice preferences;
- permission mode;
- architecture options and selected checkpoint;
- evidence gaps and questions deferred.

Then create an inventory snapshot from [the inventory template](templates/inventory/inventory.yaml), an ADR for any hard-to-reverse decision, and a handoff for the next session.
