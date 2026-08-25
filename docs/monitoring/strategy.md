# Monitoring That Leads to Action

Monitor the things a person can respond to. More metrics are not automatically
more reliability.

## Minimum useful coverage

- host reachability, boot/reboot state, CPU/memory/disk pressure, and thermal
  state where available;
- guest/container/service health and restart loops;
- storage capacity and error indicators;
- backup freshness, repository growth, and last restore proof;
- Home Assistant reachability and critical integration state;
- voice endpoint latency and fallback availability when voice is enabled;
- certificate/remote-access expiry where relevant.

Every alert needs an owner, severity, suppression/debounce behavior, and a
runbook link. If nobody can act on it, make it a dashboard signal instead.

## Test the monitor

Use a reversible, isolated test such as stopping one non-critical example
service or creating a short-lived disk-pressure fixture. Confirm:

1. the expected alert appears;
2. it identifies the correct target and likely cause;
3. no unrelated alert storm occurs;
4. the alert clears after recovery;
5. the evidence and cleanup are documented.

Do not trigger a test by taking the only control plane or radio offline.
