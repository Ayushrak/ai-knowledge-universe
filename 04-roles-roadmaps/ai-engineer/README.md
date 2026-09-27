---
id: role-ai-eng-001
domain: [llm, backend]
role: [ai-engineer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [roadmap, rag, agents, langgraph]
---

# Role: AI Engineer

## 1. Responsibilities
Ship RAG + agents to prod: chunking, hybrid retrieval, tool calling, evals, latency/cost control, guardrails.

## 2. Required skills
- Python + TypeScript, FastAPI / Next.js
- LangChain, LangGraph, LlamaIndex, Vercel AI SDK
- pgvector / Qdrant, Redis, Postgres
- Docker, GitHub Actions, basic Terraform + AWS/Azure OpenAI
- Ragas / DeepEval, prompt versioning

## 3. 90-day roadmap
- Days 0-30: `03-llm-applications/00-how-llm-works/`, `02-rag/chunking.md + retrieval.md`. Build 1 RAG on this repo.
- Days 30-60: `01-langchain-langgraph/` — ReAct agent with 3 tools, checkpointing, eval golden set 50 Q/A.
- Days 60-90: Docker + CI + guardrails (PII, injection, JSON schema), p95 <3s, cost dashboard.

## 4. Interview / Prod checklist
- [ ] Explain chunk overlap vs context bloat
- [ ] Hybrid search + rerank pipeline
- [ ] Agent loop guard (max_steps, human-in-loop)
- [ ] Faithfulness >0.85, citations returned

## 5. Linked docs in this repo
`03-llm-applications/**`, `02-backend-production/patterns/production-checklist.md`, `05-devops-architectures/terraform-iac/README.md`
