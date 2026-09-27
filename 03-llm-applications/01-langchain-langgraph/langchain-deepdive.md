---
id: langchain-deep-001
domain: [llm, agents]
role: [ai-engineer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [langchain, summarization, chains]
---

# LangChain Deep-Dive — Features & Concepts

## 1. Concepts
PromptTemplate -> Model (ChatOpenAI/ChatGoogle) -> OutputParser (Pydantic) via LCEL `prompt | model | parser`. Runnables: `RunnableParallel/Map/Lambda`. Tools via `@tool`, agents via `create_react_agent`.

## 2. Summarization (3 modes)
- **stuff**: one shot (small docs). **map_reduce**: per-chunk then combine (large). **refine**: iterative improve.

```python
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chain = load_summarize_chain(llm, chain_type="map_reduce")
print(chain.invoke({"input_documents": docs})["output_text"])
```

## 3. Retrieval + QA
`create_retrieval_chain(retriever, stuff_chain)` for grounded QA. Vector: `PGVector.from_documents(chunks, embeddings)`.

Docs: https://python.langchain.com/docs/concepts | https://python.langchain.com/docs/how_to/summarization
