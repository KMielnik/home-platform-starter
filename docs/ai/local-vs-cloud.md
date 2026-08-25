# Local, Cloud, and Hybrid AI

Local and cloud processing are complementary choices. Decide per workload,
not by ideology.

| Workload | Local is attractive when | Cloud is attractive when |
| --- | --- | --- |
| Home Control intent | Low latency, privacy, deterministic behavior | Usually unnecessary |
| Speech-to-text | Languages/models fit the hardware and must work offline | Hardware is weak or a language is poorly supported locally |
| Text-to-speech | Predictable cost and private responses matter | A preferred voice is unavailable locally |
| Open conversation | Enough RAM/VRAM, power, and maintenance appetite exist | Reasoning/current knowledge quality matters more than locality |
| Operations planning | Repository and live inspection can remain local | External research or a hosted model adds value without admin exposure |

## Decision sequence

1. Define the user-visible outcome and an acceptable response time.
2. Measure the actual language, room noise, workload, cold start, memory,
   thermals, power, and failure fallback.
3. Classify data: local-only, shareable with a selected provider, or prohibited
   outside the home.
4. Select the narrowest interface and tool set.
5. Set cost, retention, and outage limits.
6. Test rollback to deterministic Home Control.

A GPU with impressive peak throughput may still be a poor always-on voice
worker if it is noisy, power-hungry, unavailable during other use, or difficult
to reset. Benchmark the task users actually perform, not only a benchmark
score or parameter count.

## Safe routing pattern

```text
Assist intent classifier
├── local deterministic Home Control
├── local speech service (if measured viable)
└── optional conversation endpoint
    ├── local model with typed household tools
    └── cloud model with explicit data and cost policy
```

Neither branch receives infrastructure-maintenance tools by default. Keep an
operator agent and a household assistant as separate principals.
