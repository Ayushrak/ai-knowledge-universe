---
id: free-ide-001
domain: [llm, backend]
role: [software-developer, ai-engineer]
level: [beginner]
updated: 2026-09-27
source: [official-docs]
tags: [opencode, antigravity, kiro, pi, openrouter-free, hermes]
---

# Free IDEs + OpenRouter :free Models

All no credit card. One key: https://openrouter.ai/keys → `OPENROUTER_API_KEY`.

## Free models to use (`:free` suffix)
- `meta-llama/llama-3.3-70b-instruct:free` — default coder
- `nousresearch/hermes-3-llama-3.1-405b:free` — Hermes, same key, strong instruction-follow
- `google/gemini-2.0-flash-001:free` — long context alt
- `qwen/qwen-2.5-coder-32b-instruct:free` — code-focused

## 1. OpenCode (opencode.ai)
```json
// opencode.json
{ "provider": "openrouter", "model": "meta-llama/llama-3.3-70b-instruct:free" }
```
```powershell
$env:OPENROUTER_API_KEY="sk-or-..."
opencode run "summarize this repo"
```
Hermes same: swap model to `nousresearch/hermes-3-llama-3.1-405b:free`. Docs: https://opencode.ai/docs

## 2. Google Antigravity (Agentic IDE)
Settings → Models → Custom provider → Base URL `https://openrouter.ai/api/v1`, Key `sk-or-...`, Model `meta-llama/llama-3.3-70b-instruct:free`. Hermes same key, change model ID. Docs: https://cloud.google.com/blog (Antigravity)

## 3. AWS Kiro
Settings → Model provider → OpenAI-compatible → URL `https://openrouter.ai/api/v1`, Key, Model `:free` ID above. Hermes same endpoint. Docs: https://aws.amazon.com/blogs (Kiro)

## 4. Pi (Pi agent / beating local agent)
```powershell
$env:OPENAI_BASE_URL="https://openrouter.ai/api/v1"
$env:OPENAI_API_KEY="sk-or-..."
pi --model "nousresearch/hermes-3-llama-3.1-405b:free"
```
Hermes same — Pi defaults work well with Hermes instruction format.

Limits: 50/day free (1000/day after $10 top-up one-time). For daily repo scans this is enough; heavy use → switch to Gemini/Groq free per `free-llm-keys.md`.
