---
id: llm-e2e-001
domain: [llm, agents, rag]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [e2e, rag, agents, fastapi]
---

# End-to-End AI App (RAG + Agent)

## 1. Flow
Docs (S3/Blob) -> chunk (see `02-rag/chunking-strategies-all.md`) -> embed (bge/openai) -> pgvector/Qdrant -> hybrid retriever + rerank -> LangGraph (retrieve -> grade -> generate/retry) -> FastAPI SSE -> Next.js chat -> LangSmith/Langfuse trace.

```python
# graph: retrieve -> grade -> generate (retry if low score)
from langgraph.graph import StateGraph, END
g = StateGraph(dict); g.add_node("retrieve", retrieve); g.add_node("grade", grade_docs)
g.add_node("generate", generate); g.add_conditional_edges("grade", lambda s: "generate" if s["score"]>0.7 else "retrieve")
```

## 2. Stack
LangChain (chains/tools), LangGraph (state+checkpointer), LlamaIndex **or** Haystack (ingest alternative), LangSmith/Langfuse (trace/eval), LangFlow (prototype UI).

Docs: https://docs.langchain.com | https://langchain-ai.github.io/langgraph | https://docs.llamaindex.ai | https://haystack.deepset.ai
