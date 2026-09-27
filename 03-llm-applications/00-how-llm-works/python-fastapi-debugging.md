---
id: py-fastapi-001
domain: [llm, backend]
role: [ai-engineer, backend-developer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [python, generators, fastapi, debugging]
---

# Python Basics for AI + FastAPI + Debug

## 1. Generators (why: stream tokens/docs, low RAM)
```python
def chunks(docs, n=500):
    for i in range(0, len(docs), n): yield docs[i:i+n]  # lazy, not list
async def stream(app, q):
    async for tok in app.astream({"q": q}): yield f"data: {tok}\n\n"  # SSE
```

## 2. Functions to master
`async def + await`, closures for tools (`@tool`), decorators (`@traceable`), `yield from`, `contextlib.asynccontextmanager` lifespan.

## 3. FastAPI SSE
```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
app = FastAPI()
@app.get("/chat")
async def chat(q: str): return StreamingResponse(stream(graph, q), media_type="text/event-stream")
```

## 4. Debug
`LANGSMITH_TRACING=true`, `python -m pdb`, `breakpoint()`, log `thread_id + retrieval_score` per turn, replay in LangSmith/Langfuse.

Docs: https://fastapi.tiangolo.com | https://docs.python.org/3/howto/functional.html#generators
