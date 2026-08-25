# Generic Architecture Options (Illustrative)

These are decision examples, not deployment instructions.

## Option A — appliance-first

```text
one supported Home Assistant appliance
└── optional external encrypted backup target
```

Best for small hardware, low operational appetite, and deterministic Home
Control. Add a separate management surface only when recovery or documentation
needs justify it.

## Option B — role-separated host

```text
base host
├── Home Assistant guest/appliance
├── operations guest
└── optional applications guest
```

Best when independent update boundaries and backup ownership matter. It adds
host and boot-recovery work.

## Option C — burst AI extension

```text
role-separated home platform
└── optional authenticated AI worker (may sleep or be remote)
```

The worker can improve conversation or batch work, but ordinary Home Control
must keep working when it is absent.
