---
id: rag-adv-001
domain: [llm, rag, agents]
role: [ai-engineer, ai-architect]
level: [expert]
updated: 2026-09-27
source: [official-docs]
tags: [retrieval, rerank, top-k, self-rag, crag, react]
---

# Retrieval Strategies — Evolution, Top-k, Re-rank

## 1. Parts
Query rewrite -> hybrid fetch (vector + BM25) -> filter (tenant/date) -> re-rank -> compress -> cite.

## 2. Evolution
- **Naive RAG**: embed -> top-k -> stuff. Breaks on multi-hop.
- **Advanced RAG**: rewrite + HyDE + sentence-window + rerank.
- **Modular RAG**: routers (route by intent), Corrective RAG (CRAG: grade -> web fallback), Self-RAG (model decides retrieve/reflect).
- **ReAct agents**: Thought->Action(search)->Observe loop via LangGraph. Use for multi-step QA.

## 3. Top-k how-to
Start k=20 fetch -> rerank -> keep 5. k=3 precise/cheap, k=10 recall/cost. Tune by hit-rate@5 + faithfulness, not vibes. Dynamic: k=3 if score>0.85 else k=10 + HyDE retry.

```python
docs = hybrid_search(q, k=20)
top5 = rerank("bge-reranker-v2", q, docs)[:5]  # Cohere rerank / bge / RankGPT
ctx = compress(top5, max_tokens=3000)
```

## 4. Re-rank + other methods
BGE/Cohere cross-encoder (+10-15% NDCG), RankGPT LLM rank, ColBERT late-interaction, Hypothetical Doc (HyDE), step-back query, parent-child fetch, query routing per domain.

Docs: https://arxiv.org/abs/2310.01549 (Self-RAG) | https://arxiv.org/abs/2401.15884 (CRAG) | https://docs.cohere.com/docs/rerank
