---
id: guard-002
domain: [llm]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [guardrails, pii, prompt-injection]
---

# Guardrails — PII + Attacks + Hallucination Shield

## 1. Layers (in/out)
In: PII redact (Presidio/MS), injection scan (`ignore previous` regex + classifier), length/role allowlist. Out: PII re-check, JSON schema (Instructor), citation required, toxicity filter.

```python
from presidio_analyzer import AnalyzerEngine
an = AnalyzerEngine()
if an.analyze(text=q, language="en"): q = "[REDACTED-PII]"
# + NeMo/Guardrails-AI rail: refuse if no citation
```

## 2. Tools
Presidio, Guardrails-AI, NeMo Guardrails, Langfuse prompt firewall, Rebuff (injection). Log attacks to SIEM, rate-limit attacker IP.

Docs: https://github.com/microsoft/presidio | https://www.guardrailsai.com | https://docs.nemo.guardrails.cloud
