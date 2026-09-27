---
id: llm-obs-001
domain: [llm, agents]
role: [ai-engineer]
level: [production]
updated: 2026-09-27
source: [official-docs, github-trending]
tags: [langsmith, langfuse, langflow, haystack]
---

# Observability & Builder Libs — LangSmith / Langfuse / LangFlow / Haystack

- **LangSmith**: trace every run, eval datasets, prompt hub. `LANGSMITH_TRACING=true`. https://docs.smith.langchain.com
- **Langfuse** (open-source alt): self-host, scores + cost. https://langfuse.com/docs
- **LangFlow**: drag-drop prototype -> export Python. https://docs.langflow.org
- **Haystack** (# = Haystack): prod pipelines `Pipeline.connect`. https://haystack.deepset.ai — alternative to LlamaIndex for search-heavy.
- **LlamaIndex**: `VectorStoreIndex.from_documents` + QueryEngine for RAG-first. https://docs.llamaindex.ai
- **QA chain**: `create_retrieval_chain` (LangChain) = retriever + stuff + citations.

Pick: LangGraph+LangSmith (agents) OR LlamaIndex+Langfuse (RAG+self-host). Daily agent tracks releases in `_daily/`.
