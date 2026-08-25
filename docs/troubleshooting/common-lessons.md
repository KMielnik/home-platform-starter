# Common Lessons and Failure Patterns

## “Everything is in one container, so it is backed up”

Containers are replaceable. Identify the application data, database consistency
procedure, secret recovery material, and recreation steps separately.

## “The command succeeded, so the feature works”

Test the user-visible outcome: can Home Assistant control the device, can voice
understand the intended language, can the restored service open its state, and
does the monitor alert and clear?

## “A newer model must be better”

Benchmark representative utterances, languages, noise, cold starts, and
fallbacks. Interactive latency and false actions may matter more than a score.

## “A firewall can be enabled after the fact”

Map management, backup, monitoring, device discovery, and tailnet flows first.
Keep a physical or out-of-band rollback path. Enable one boundary at a time and
verify from an external client.

## “Expose every entity so the assistant is powerful”

Expose human-useful controls and status. Firmware, radio, diagnostics, raw
topology, policy toggles, and reset functions create ambiguity and risk.

## “A gaming workstation is always-on infrastructure”

Keep Home Control independent of a machine that sleeps, overheats, or has a
competing workload. Add a narrow burst endpoint only when the fallback is clear.

## “A visual workflow should own all automations”

Device-local behavior belongs in the home automation authority. Use cross-system
workflow tooling for a real coordination need and document duplicate handling.

## “A snapshot equals a disaster plan”

Prove extraction, consistency, and at least one operational restore. Write down
what still needs human pairing, firmware, physical access, or account recovery.
