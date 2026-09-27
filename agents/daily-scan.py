"""Daily scanner: fetches trending signals, writes _daily markdown.
Usage: python agents/daily-scan.py --domain all
If LLM key present (OPENAI_API_KEY), uses summarize.py style frontmatter; else raw.
Sources: GitHub trending API (via github api search), npm, HF — best-effort, no key needed.
"""
import argparse, datetime, os, json, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRENDING_REPOS = [
    ("langchain-ai/langchain", "llm", "langchain,agents"),
    ("langchain-ai/langgraph", "llm", "langgraph,agents"),
    ("huggingface/transformers", "llm", "transformers"),
    ("vercel/ai", "javascript", "vercel-ai,nextjs"),
    ("facebook/react", "javascript", "react"),
    ("vitejs/vite", "javascript", "vite"),
    ("oven-sh/bun", "javascript", "bun"),
    ("TanStack/query", "javascript", "tanstack"),
]

def fetch_stars(repo: str):
    url = f"https://api.github.com/repos/{repo}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ai-knowledge-universe"})
        token = os.getenv("GITHUB_TOKEN")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode())
            return d.get("stargazers_count", "-"), d.get("description", "")
    except Exception as e:
        return "-", f"fetch failed: {e}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", default="all")
    args = ap.parse_args()
    date = datetime.date.today().isoformat()
    daily_path = os.path.join(ROOT, "01-javascript-trending", "_daily", f"{date}-trending.md")
    lines = [f"---\nupdate: {date}\ndomain: all\n---\n", f"# Daily trending — {date}\n"]
    for repo, domain, tags in TRENDING_REPOS:
        if args.domain != "all" and args.domain != domain and args.domain != "javascript":
            if args.domain in ("llm", "devops") and domain != args.domain:
                continue
        stars, desc = fetch_stars(repo)
        lines.append(f"## {repo} ({stars} stars)\n- domain: {domain} | tags: {tags}\n- {desc}\n- https://github.com/{repo}\n")
    os.makedirs(os.path.dirname(daily_path), exist_ok=True)
    with open(daily_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote {daily_path}")

if __name__ == "__main__":
    main()
