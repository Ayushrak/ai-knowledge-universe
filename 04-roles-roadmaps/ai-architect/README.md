---
id: role-ai-arch-001
domain: [llm, architecture]
role: [ai-architect]
level: [expert]
updated: 2026-09-27
source: [official-docs]
tags: [roadmap, governance, rag-architecture]
---

# Role: AI Architect

## 1. Responsibilities
Decide LLM vs RAG vs agent vs fine-tune. Design retrieval topology, eval strategy, data governance, multi-env rollout, cost model.

## 2. Required skills
System design, CAP for vector DBs, Azure OpenAI / Bedrock, VPC / Private Link, KeyVault, OTel, FinOps for tokens.

## 3. 90-day roadmap
- Days 0-30: Audit 5 use-cases, classify (chat / search / agent). Define golden dataset from `ai-knowledge-universe`.
- Days 30-60: Reference architecture: Blob/S3 docs -> chunk -> pgvector -> hybrid retriever -> LangGraph -> App Service/ECS. ADR docs.
- Days 60-90: Prod hardening: IaC (`05-devops-architectures/`), eval gates in CI, red-teaming, DPIA.

## 4. Interview / Prod checklist
- [ ] When NOT to use RAG (small static knowledge -> fine-tune / prompt cache)
- [ ] Parent-child chunk + rerank justification
- [ ] Multi-tenancy: namespace isolation, PII redaction
- [ ] Disaster recovery for embeddings (re-index pipeline)

## 5. Linked docs in this repo
`03-llm-applications/`, `05-devops-architectures/terraform-iac/README.md`, `03-llm-applications/03-eval-guardrails/eval-guardrails.md`
