# Checkpoint Runbook Pattern

Use this pattern for host, service, Home Assistant, voice, and migration work.

## Before

- state current evidence and desired outcome;
- identify affected roles, dependencies, and user-visible risk;
- verify backup/recovery boundary;
- define approval scope and stop conditions;
- prepare a rollback command or documented manual step;
- capture a baseline health check.

## During

- make one bounded change;
- record exact versions/identifiers without secrets;
- stop if output contradicts the proposal;
- keep optional services from becoming a hidden dependency.

## After

- test the requested outcome and a relevant failure/fallback;
- check logs, health, resource pressure, and monitoring;
- remove temporary artifacts;
- update desired state, observed evidence, outcome, and handoff;
- review the diff and run repository validation.
