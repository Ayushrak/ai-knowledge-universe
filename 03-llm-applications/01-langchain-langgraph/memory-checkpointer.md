---
id: langgraph-mem-001
domain: [llm, agents]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [memory, checkpointer, langgraph]
---

# LangGraph Memory — Short/Long-Term + Checkpointer

## 1. Short-term (thread)
`MemorySaver`/`PostgresSaver` checkpointer persists state per `thread_id`. Resume, time-travel, human-in-loop `interrupt_before`.

```python
from langgraph.checkpoint.memory import MemorySaver
app = graph.compile(checkpointer=MemorySaver())
app.invoke({"q":"hi"}, config={"configurable":{"thread_id":"user-1"}})
```

## 2. Long-term (store)
`BaseStore` (pgvector) for user facts/preferences across threads: `store.put(("user-1","facts"), "likes-dark-mode", {...})`, recall in node.

## 3. Rules
Summarize thread >20 turns, never stuff full history. Isolate by `thread_id=userId`, TTL PII. LangMem `create_memory_manager` for auto-extract.

Docs: https://langchain-ai.github.io/langgraph/concepts/memory
