# Setting up the KB index

This skill expects two things to already exist:

1. **A ChromaDB collection** of your product docs / help center articles / resolved tickets, embedded and persisted to disk.
2. **A BM25 index** over the same corpus for keyword-exact matches (useful for error codes, feature names, SKUs — things vector search alone tends to miss).

If you already have the CS Knowledge Copilot pipeline (ChromaDB + BM25 + Claude-generated answers), point this skill at it:

```bash
export KB_INDEX_PATH=/path/to/chroma_persist_dir
export KB_DOCS_PATH=/path/to/doc_corpus
```

Then fill in `scripts/query_kb.py`'s `load_chroma_results` and `load_bm25_results`
functions with your existing query code — this scaffold intentionally stubs
them out rather than guessing at your schema/embedding model.

## If you don't have an index yet

Minimal path to bootstrap one:
1. Export your Notion help docs / Zendesk help center articles as markdown or plain text.
2. Chunk them (500-1000 tokens per chunk works well for support content).
3. Embed with any Claude-compatible embedding model and load into a persistent ChromaDB collection.
4. Build a parallel BM25 index (e.g. via `rank_bm25`) over the same chunks, keyed by the same source IDs.
