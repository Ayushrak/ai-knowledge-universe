"""Summarizer: turns raw scan JSON into RAG-ready markdown with frontmatter.
Free-mode: uses agents/free_llm.py if a free key exists, else template-only (zero cost).
"""
import os, datetime
try:
    from agents.free_llm import summarize_free
except ImportError:
    try:
        from free_llm import summarize_free
    except ImportError:
        summarize_free = None

TEMPLATE = """---
id: {id}
domain: [{domain}]
role: [ai-engineer, software-developer]
level: [production]
updated: {date}
source: [github-trending]
tags: [{tags}]
---

# {title}

## 1. What / Why
{summary}

## 2. How it works
{details}

## 3. Prod code snippet
See upstream repo README.

## 4. Pitfalls
Verify license, maintenance, prod readiness.

## 5. References
- {url}
"""

def summarize_item(name: str, description: str) -> tuple[str, str]:
    """Free LLM summary for trending lib: what's new / version / use-case. Returns (text, provider)."""
    if summarize_free is None or not any(os.getenv(k) for k in ("GEMINI_API_KEY", "GROQ_API_KEY", "GITHUB_TOKEN", "HF_TOKEN", "OPENROUTER_API_KEY")):
        return description[:500], "template-only-no-key"
    prompt = (
        f"Library: {name}\nContext: {description[:800]}\n"
        "In 4 bullets: 1) what it does 2) latest version/feature trend 3) when to use vs alternative 4) prod pitfall."
    )
    try:
        return summarize_free(prompt)
    except Exception as e:
        return description[:500], f"fallback:{e}"

def to_markdown(item: dict, domain="javascript") -> str:
    date = datetime.date.today().isoformat()
    return TEMPLATE.format(
        id=item.get("id", "auto-001"),
        domain=domain,
        date=date,
        tags=",".join(item.get("tags", [])) or "trending",
        title=item.get("name", "Untitled"),
        summary=item.get("description", "")[:500],
        details=f"Stars: {item.get('stars','-')}. Trending signal from automated scan.",
        url=item.get("url", "https://github.com/trending"),
    )
