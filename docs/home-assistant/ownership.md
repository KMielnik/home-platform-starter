# Home Assistant and Device Ownership

Home Assistant is usually the clearest authority for household behavior. Keep
protocol plumbing behind it and make the human-facing layer intentional.

## Ownership map

| Capability | Preferred owner | Notes |
| --- | --- | --- |
| Device state and commands | Home Assistant integration | Use supported integration APIs |
| Zigbee network | One selected coordinator/runtime | Do not let multiple systems claim the same radio |
| Thread border routing | One selected border-router responsibility | Document failover limits |
| Matter fabric | Home Assistant or the documented commissioner | Record commissioning authority |
| MQTT transport | Broker/runtime with clear credentials | Devices should not each invent a broker path |
| Deterministic lighting, climate, safety | Home Assistant | Keep latency and outage behavior predictable |
| Human maintenance reminder | Task manager or notification workflow | Create an actionable task only when human work is needed |
| Infrastructure health | Monitoring/operations plane | Translate important failures into household tasks; do not put shell access in HA |

## Human-useful Assist exposure

Expose the broad set of controls a person may reasonably ask for:

- lights, brightness, color temperature, color, scenes, and meaningful switches;
- climate setpoint/mode/fan controls;
- useful appliance operations and status, subject to safety policy;
- vacuum start/return/status/battery where supported;
- media playback and volume where it is genuinely useful;
- human-facing sensors such as temperature, air quality, battery, progress, and
  errors.

Keep firmware, radio permit-join, diagnostics, calibration, raw topology,
internal policy toggles, update buttons, and maintenance entities out of the
voice surface. Remote appliance start or unsafe actions deserve an explicit
policy and confirmation, not an accidental exposure.

## Names and aliases

Use names a person naturally says in the room and language they use. Prefer
specific phrases such as “reading lamp” or “hallway light” over a roomless
generic “light” when several devices could match. Preserve existing aliases,
add bilingual phrases intentionally, and test both languages against the real
Assist pipeline. Document collisions and unavailable entities.

## Integration checklist

- Who owns the device protocol?
- Which entity is the human-facing control?
- Which status answers a useful question?
- Which entities are internal, diagnostic, or destructive?
- What happens if the broker, cloud, or optional AI role is down?
- Is the alias unambiguous in every supported language?
- Is the behavior backed up and documented without raw HA storage?
