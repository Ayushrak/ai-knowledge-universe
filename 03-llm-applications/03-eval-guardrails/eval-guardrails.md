---
id: eval-guard-001
domain: [llm]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [eval, guardrails]
---

# Eval + Guardrails

## 1. What / Why
Prevent hallucination, cost blowout in prod.

## 2. How it works
Golden Q/A set from this repo -> faithfulness, relevancy scores (Ragas/DeepEval). Guardrails: PII filter, prompt-injection check, JSON schema validation.

## 3. Prod checklist
- [ ] Ragas faithfulness >0.85
- [ ] p95 latency logged
- [ ] refusal on low retrieval score

## 4. References
- Ragas, Guardrails-AI
