---
id: rag-chunking-001
domain: [llm, rag]
role: [ai-engineer, ai-architect]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [chunking, rag, embeddings]
---

# Chunking — How It Works

## 1. What / Why
Split docs into retrievable units that fit embedding + LLM context without losing meaning.

## 2. How it works
Strategies: fixed-size (500 tok, 50 overlap), semantic (split on ##), recursive, parent-child.
Rule for this repo: 400-600 tokens, split on `##`, keep YAML frontmatter per chunk, overlap 10%.

## 3. Prod code snippet
```python
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
md_split = MarkdownHeaderTextSplitter(headers_to_split_on=[("##","section")])
rec = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = rec.split_documents(md_split.split_text(open("doc.md").read()))
```

## 4. Pitfalls
Too large = noisy retrieval. Too small = lost context. No overlap at boundaries. Tables/code split mid-block.

## 5. References
- LlamaIndex chunking guide, LangChain splitters
