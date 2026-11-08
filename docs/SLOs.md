# Draft service-level objectives

These initial targets are for the learning prototype. Establish measured baselines and revise targets as retrieval and model calls are added.

| Measure | Initial target | Measurement |
| --- | --- | --- |
| API latency | p95 below 500 ms for non-LLM endpoints | Request duration, excluding model calls |
| Availability | 99% during a local demo session | Successful `/health` checks / total checks |
| Evaluation pass rate | Establish a retrieval baseline, then target at least 80% on a versioned golden set | Evaluation runner, once available |
| Cost per query | $0 before model integration; establish baseline before hosted models | Provider cost and tokens per answered query |

Only health and request latency can be measured by the starter API. Evaluation and cost targets become measurable in later milestones.
