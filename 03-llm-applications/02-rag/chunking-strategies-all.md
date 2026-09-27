---
id: rag-chunk-all-001
domain: [llm, rag]
role: [ai-engineer]
level: [production]
updated: 2026-09-27
source: [official-docs]
tags: [chunking, strategies]
---

# All Chunking Strategies

| # | Strategy | When | Lib |
|---|---|---|---|
| 1 | Fixed 500/50 overlap | baseline logs | RecursiveCharacterTextSplitter |
| 2 | Recursive (para>sentence) | general docs | LangChain recursive |
| 3 | Markdown-header (##) | this repo | MarkdownHeaderTextSplitter |
| 4 | Semantic (embeddings split) | drift topics | SemanticChunker |
| 5 | Parent-child (parent 2000 + child 400 retrieve) | long contracts | ParentDocumentRetriever |
| 6 | Sentence-window (3-prev/next) | QA citations | LlamaIndex SentenceWindow |
| 7 | Code (AST/function) | repos | CodeSplitter |
| 8 | Table-aware (no mid-row) | PDFs | Unstructured partition |

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(
  MarkdownHeaderTextSplitter([("##","sec")]).split_text(open("doc.md").read()))
```

Rule: 400-600 tok, 10% overlap, keep frontmatter, eval hit-rate@5 per strategy. Docs: https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers
