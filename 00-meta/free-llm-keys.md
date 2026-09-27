---
id: free-llm-keys-001
domain: [llm, backend, javascript, devops]
role: [ai-engineer, software-developer]
level: [beginner]
updated: 2026-09-27
source: [official-docs]
tags: [free-api, gemini, groq, github-models]
---

# Free LLM API Keys — zero money setup (for daily trending updates)

Your repo works with **ZERO key** (GitHub/npm APIs only). Add ANY ONE free key below for AI summaries of what's new/version/changes.

## 1. Recommended (pick 1, all no credit card)

| # | Provider | Free quota 2026 | Get key | Env var |
|---|---|---|---|---|
| 1 | **Google Gemini AI Studio** (Recommended) | ~9000 req/day Flash, 1M context | https://aistudio.google.com/apikey | `GEMINI_API_KEY` |
| 2 | **Groq** (fastest) | 30 RPM / 14400 RPD, Llama-3.3-70B | https://console.groq.com/keys | `GROQ_API_KEY` |
| 3 | **GitHub Models** (you already have) | 150-1000/day, gpt-4o-mini | uses `GITHUB_TOKEN` auto in Actions | `GITHUB_TOKEN` |
| 4 | **HuggingFace Inference** | free tier, Llama/Qwen | https://huggingface.co/settings/tokens | `HF_TOKEN` |
| 5 | **OpenRouter :free** | 50/day, 20+ free models | https://openrouter.ai/keys | `OPENROUTER_API_KEY` |
| 6 | **Ollama local** (offline, unlimited) | `ollama pull llama3.1 && ollama serve` | no key | — |

No official free OpenAI key in 2026 — don't bother.

## 2. Local setup (30 sec)
```powershell
$env:GEMINI_API_KEY="your-key"  # or GROQ_API_KEY
pip install -r agents/requirements.txt
python agents/daily-scan.py --domain all
python -c "from agents.free_llm import summarize_free; print(summarize_free('what is new in LangGraph?'))"
```

## 3. GitHub Actions setup (free)
Repo Settings > Secrets > Actions > New:
- `GEMINI_API_KEY` and/or `GROQ_API_KEY`
- `GITHUB_TOKEN` is automatic — workflow already uses it.

Workflow `daily-update.yml` auto-picks: Gemini > Groq > GitHub Models > HF > OpenRouter > template-only.

## 4. How daily trending covers all domains (no key needed)
- JS: GitHub search `stars:>1000 language:typescript` + npm registry `https://registry.npmjs.org/-/v1/search?text=...`
- LLM: `langchain-ai/*` releases + HF `https://huggingface.co/api/models?sort=likes`
- Backend (.NET/Java): GitHub topics `dotnet, spring-boot`
- DevOps: AWS/Azure blogs RSS

With a free key, each item gets 4-bullet AI summary: what / new version / vs alternative / prod pitfall.

## 5. Privacy note
Gemini free tier may train on data outside EU. For private docs use Ollama local or GitHub Models.
