# Role-Oriented Reference Model

One possible arrangement is:

```text
home server or appliance
├── Home Assistant role
│   ├── devices and protocol bridges
│   ├── deterministic automations
│   └── Assist Home Control
├── optional application role
│   └── household services justified by goals
├── operations control plane
│   ├── Git-backed context and desired state
│   ├── narrow automation and agent interfaces
│   ├── encrypted secrets
│   └── backups and restore verification
└── optional AI/voice worker
    ├── local speech services
    ├── optional local conversation model
    └── authenticated, tailnet/VPN-only endpoints
```

These roles may be one appliance, separate guests, containers, or separate
machines. The important boundaries are ownership and recovery, not the number
of boxes.

## Interface rules

- HA exposes household capabilities to Assist, not infrastructure maintenance.
- The operations plane can inspect HA through supported APIs and manage desired
  state through reviewed files.
- Optional applications receive only the storage, network, and credentials
  they need.
- A voice or LLM worker receives a narrow, typed Home Control interface.
- Monitoring observes every role without becoming the owner of household
  behavior.
- Backups cover durable configuration and recovery material, not automatically
  every replaceable byte.
