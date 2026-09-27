"""Summarizer: turns raw scan JSON into RAG-ready markdown with frontmatter."""
import os, datetime

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
