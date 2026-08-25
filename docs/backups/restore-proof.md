# Backups and Restore Proof

Backups are a recovery design, not an archive checkbox.

## Classify data

| Class | Examples | Treatment |
| --- | --- | --- |
| Rebuildable | package lists, image caches, generated thumbnails | Record how to recreate; back up only if cheap |
| Durable configuration | HA config, Compose/Ansible, dashboards, automations | Encrypted backup plus Git where safe |
| Application state | databases, task history, identity/configuration | Backup with quiesce/consistency procedure |
| Recovery material | secret-encryption keys, recovery codes, restore instructions | Encrypted copies in independent locations |
| Replaceable bulk data | large media or caches | Include only when the value and storage cost justify it |

Never put plaintext credentials or raw private databases in Git. A backup
repository must be encrypted, monitored for freshness, and subject to a size
ceiling or growth review.

## Restore proof levels

1. **Readable** — the backup tool can list metadata.
2. **Extractable** — a representative archive can be restored to an isolated
   temporary directory.
3. **Consistent** — databases pass their native integrity check or the service
   opens the restored state.
4. **Operational** — the documented rebuild procedure recreates a working,
   user-visible capability.
5. **Timed** — the person knows approximate recovery time and remaining manual
   steps.

Test the highest practical level for each important class. Clean up staging
directories and record the evidence, date, scope, and limitation.

## Recovery runbook outline

- declare the incident and protect the surviving source;
- identify the last known-good backup and key location;
- restore to isolated staging first;
- verify checksums/native integrity and redact output;
- rebuild the smallest control path;
- validate Home Control and monitoring;
- promote only after the result is understood;
- update the outcome and improve the runbook.

Do not call a snapshot a backup until it survives the loss of the host that
created it. Do not call a backup a restore plan until someone has followed it.
