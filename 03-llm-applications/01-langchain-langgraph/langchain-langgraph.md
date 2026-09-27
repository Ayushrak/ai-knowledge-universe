---
id: langchain-langgraph-001
domain: [llm, agents]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [langchain, langgraph, agents, tools]
---

# LangChain vs LangGraph — Libraries in Use

## 1. What / Why
LangChain = chains + tools + retrievers. LangGraph = stateful graph orchestration for multi-step agents.

## 2. How it works
LangChain: Prompt -> Model -> Parser, `create_react_agent(tools)`.
LangGraph: nodes + edges + checkpointer. Supports cycles, human-in-loop, persistence.

## 3. Prod code snippet
```python
from langgraph.graph import StateGraph, END
from typing import TypedDict
class S(TypedDict): q: str; ctx: list; ans: str
def retrieve(s: S): return {"ctx": ["doc1"]}
def generate(s: S): return {"ans": f"Answer {s['q']} with {s['ctx']}"}
g = StateGraph(S); g.add_node("r", retrieve); g.add_node("g", generate)
g.set_entry_point("r"); g.add_edge("r","g"); g.add_edge("g", END)
app = g.compile()
print(app.invoke({"q":"what is chunking?","ctx":[],"ans":""}))
```

## 4. Pitfalls
Unbounded loops, no eval, leaking keys in tools, no checkpointing.

## 5. Libraries matrix (see ../libraries-matrix.md)
LangChain, LangGraph, LlamaIndex, Haystack, Vercel AI SDK, Instructor, Guardrails.

## 6. References
- docs.langchain.com, langchain-ai.github.io/langgraph
