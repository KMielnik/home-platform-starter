# Migrating an Existing Platform

Migration is a sequence of small, reversible boundaries. Do not move every
service to a new topology at once.

## Inventory and classify

Record current authority, dependencies, persistent data, network assumptions,
credentials/recovery material, and acceptable downtime. Mark every fact as
verified or documented-but-not-rechecked.

## Recommended sequence

1. Build the source-of-truth repository without changing runtime behavior.
2. Capture a sanitized observed snapshot and verify a backup/restore sample.
3. Introduce the new management path in read-only mode.
4. Move one non-critical, easily rebuildable service.
5. Verify user-visible behavior, monitoring, and restore coverage.
6. Migrate durable state with a quiesce/rollback procedure.
7. Migrate household control only after the new authority is proven and the old
   path has a recovery plan.
8. Decommission the old layer only after a retention window and documented
   rollback decision.

## Cutover checklist

- exact source and destination versions;
- maintenance window and person available for physical recovery;
- backup and tested restore sample;
- DNS/remote-access implications;
- radio/device ownership and pairing state;
- monitoring and alert routing;
- rollback trigger and time limit;
- handoff and outcome updated.

Never infer that an import succeeded because a file copied. Test the actual
household behavior and the next backup after cutover.
