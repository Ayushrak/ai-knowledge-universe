---
id: rag-retrieval-001
domain: [llm, rag]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [retrieval, vector-db, hybrid-search]
---

# Retrieval — How It Works

## 1. What / Why
Fetch top-k relevant chunks for a query to ground LLM.

## 2. How it works
Pipeline: embed query -> hybrid search (vector + BM25 on tags) -> rerank (Cohere/bge) -> top 5 -> prompt.
Vector DBs: pgvector (cheap prod), Qdrant, Pinecone, Chroma. Libraries: LangChain retrievers, LlamaIndex.

## 3. Prod code snippet
```python
# hybrid: vector + keyword filter on frontmatter domain/role
results = store.similarity_search_with_score("how does LangGraph checkpoint?", k=5,
  filter={"domain": "llm"})
ctx = "\n".join(d.page_content for d,_ in results if _ > 0.7)
```

## 4. Pitfalls
No rerank, k too high (context bloat/cost), stale embeddings after doc update, no citations.

## 5. References
- Pinecone hybrid search, Cohere rerank docs
