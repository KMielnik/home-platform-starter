# Voice Decision Tree

Voice is a chain with different latency, privacy, and failure characteristics.
Design each link deliberately:

```text
room microphone/satellite
  → wake word (optional local)
  → Home Assistant Assist
  → speech-to-text
  → deterministic Home Control when possible
  → optional conversational model
  → text-to-speech
  → room speaker
```

## Choose the path

1. **Is this a normal Home Control intent?**
   - Yes: route to Home Assistant’s deterministic intent handling first.
   - No: continue to conversational handling or tell the person it is outside
     the supported scope.
2. **Is local speech fast and accurate enough for the languages and noise?**
   - Yes: prefer local STT/TTS for privacy and predictable latency.
   - No: use a measured cloud or hybrid fallback and document data flow/cost.
3. **Is a conversational model actually needed?**
   - No: keep the path simple.
   - Yes: choose local or cloud using the AI decision guide.
4. **Does the request cause a consequential action?**
   - Yes: require confirmation, a narrow tool, or an attended channel.
   - No: answer with the minimum data needed.

## Satellite commissioning plan

For any new room satellite, pilot one unit:

1. verify the delivered hardware variant and firmware boundary;
2. record microphone/speaker, Wi-Fi, power, and room noise constraints;
3. test wake word and push-to-talk fallback;
4. measure end-to-end latency in every supported language;
5. test AEC and false wake behavior with ordinary household sound;
6. verify Home Control while the conversational worker is offline;
7. document recovery, mute behavior, and privacy indicators;
8. roll out a second unit only after subjective audio and reliability criteria
   pass.

Do not let a satellite become an implicit administrator. Its tools should be
typed household capabilities, not a shell, Docker API, hypervisor API, secrets
store, or maintenance MCP.
