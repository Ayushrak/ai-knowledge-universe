---
id: hallu-001
domain: [llm]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [hallucination, eval, self-check]
---

# Hallucination — Detect + Recover

## 1. Why
Model fills gaps when retrieval k=0 or low score, temp high, no grounding instruction.

## 2. Detect
Ragas faithfulness (<0.8 = flag), NLI entailment per sentence, retrieval score <0.7, self-check ask `Is {claim} in {ctx}?`.

## 3. Recover strategies
- Refuse + ask clarify if score low. Re-retrieve with rewritten query (HyDE/step-back). Constrained decode (JSON schema + citations `[doc:chunk]`). Temp 0-0.2 prod. Rerank top-20->5.

```python
if score < 0.7: return {"ans": "Not in docs. Which doc?", "citations": []}
```

Docs: https://docs.ragas.io | https://python.langchain.com/docs/how_to/self_query
