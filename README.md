# ai-knowledge-universe
Golden-dataset monorepo: trending JS libs + backend production + LLM apps + roles + DevOps.
Human-readable docs, AI-recallable (RAG-ready with frontmatter + chunking rules).

## How to use
1. Browse by domain: `01-javascript-trending/`, `02-backend-production/`, `03-llm-applications/`, `04-roles-roadmaps/`, `05-devops-architectures/`
2. Every doc has YAML frontmatter (`id, domain, role, level, updated`) for chunking/retrieval.
3. Daily auto-update: GitHub Action runs `agents/daily-scan.py` at 02:00 UTC, writes to `*/_daily/YYYY-MM-DD.md`, updates `libraries-matrix.md`.
4. Local run: `pip install -r agents/requirements.txt` then `python agents/daily-scan.py --domain all`

## RAG conventions
- Chunk size: 400-600 tokens, split on `##`, keep frontmatter per chunk.
- Retrieval: hybrid (vector embeddings + BM25 on `domain, role, tags`).
- See `00-meta/` for templates and `03-llm-applications/02-rag/` for chunking/retrieval guides.

## Map
- `00-meta/` - templates, taxonomy
- `01-javascript-trending/` - React/Next/Vite/Bun/state libs + daily trending
- `02-backend-production/` - Node/.NET/Java prod patterns
- `03-llm-applications/` - how LLM works, LangChain/LangGraph, RAG, eval
- `04-roles-roadmaps/` - AI Architect, AI Engineer, Frontend, Backend, .NET, .NET Architect, Java, DevOps
- `05-devops-architectures/` - Terraform/IaC, AWS, Azure
- `agents/` - daily scanner + summarizer
- `.github/workflows/daily-update.yml` - cron automation
