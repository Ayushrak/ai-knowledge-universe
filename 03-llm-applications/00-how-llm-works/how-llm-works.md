---
id: llm-how-works-001
domain: [llm]
role: [ai-engineer, ai-architect]
level: [beginner]
updated: 2026-09-27
source: [official-docs]
tags: [transformer, tokens, inference]
---

# How LLM Works

## 1. What / Why
Predicts next token from context using transformer. Needed to reason about chunking, context limits, cost.

## 2. How it works
Tokenizer -> embeddings -> N x transformer blocks (self-attention + MLP) -> logits -> sampling.
Key params: context window, temperature, top-p, max tokens. KV-cache makes long context expensive.

## 3. Prod code snippet
```python
from openai import OpenAI
c = OpenAI()
r = c.chat.completions.create(model="gpt-4o-mini", temperature=0.1,
  messages=[{"role":"system","content":"Answer from context only."},
            {"role":"user","content":"Summarize chunk..."}])
```

## 4. Pitfalls
Hallucination when no retrieval. Context overflow. High temp in prod. No evals.

## 5. References
- Attention Is All You Need, OpenAI tokenizer docs
