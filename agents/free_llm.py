"""Free LLM router: tries free providers in order, OpenAI-compatible.
Priority: Gemini -> Groq -> GitHub Models -> HuggingFace -> OpenRouter-free -> Ollama local
All free, no credit card. Set any one key, code auto-picks.
Env: GEMINI_API_KEY, GROQ_API_KEY, GITHUB_TOKEN, HF_TOKEN, OPENROUTER_API_KEY
"""
import os, json, urllib.request

PROVIDERS = [
    {"name": "gemini", "env": "GEMINI_API_KEY",
     "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
     "note": "9000 RPD free, 1M context — best for daily summaries"},
    {"name": "groq", "env": "GROQ_API_KEY",
     "url": "https://api.groq.com/openai/v1/chat/completions",
     "model": "llama-3.3-70b-versatile",
     "note": "30 RPM / 14400 RPD free, fastest"},
    {"name": "github-models", "env": "GITHUB_TOKEN",
     "url": "https://models.github.ai/inference/chat/completions",
     "model": "openai/gpt-4o-mini",
     "note": "free for any GitHub user"},
    {"name": "huggingface", "env": "HF_TOKEN",
     "url": "https://router.huggingface.co/v1/chat/completions",
     "model": "meta-llama/Llama-3.3-70B-Instruct",
     "note": "free tier, huge catalog"},
    {"name": "openrouter-free", "env": "OPENROUTER_API_KEY",
     "url": "https://openrouter.ai/api/v1/chat/completions",
     "model": "meta-llama/llama-3.3-70b-instruct:free",
     "note": "50/day free, 20+ free models"},
]

def _post_openai_compat(url, key, model, prompt, max_tokens=800):
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens}).encode()
    req = urllib.request.Request(url, data=body, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode())
        return d["choices"][0]["message"]["content"]

def _post_gemini(key, prompt, max_tokens=800):
    import urllib.parse
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"maxOutputTokens": max_tokens}}).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode())
        return d["candidates"][0]["content"]["parts"][0]["text"]

def summarize_free(prompt: str, max_tokens=800) -> tuple[str, str]:
    """Returns (text, provider_name). Raises if no key found."""
    for p in PROVIDERS:
        key = os.getenv(p["env"])
        if not key:
            continue
        try:
            if p["name"] == "gemini":
                return _post_gemini(key, prompt, max_tokens), "gemini"
            return _post_openai_compat(p["url"], key, p["model"], prompt, max_tokens), p["name"]
        except Exception as e:
            print(f"provider {p['name']} failed: {e}, trying next")
            continue
    # Ollama local fallback (no key)
    try:
        return _post_openai_compat("http://localhost:11434/v1/chat/completions", "ollama", "llama3.1", prompt, max_tokens), "ollama-local"
    except Exception as e:
        raise RuntimeError("No free LLM key set. See 00-meta/free-llm-keys.md") from e

if __name__ == "__main__":
    print(summarize_free("Summarize in 1 line: what is LangGraph?"))
