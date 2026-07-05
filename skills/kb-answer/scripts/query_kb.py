#!/usr/bin/env python3
"""
Hybrid retrieval (BM25 + ChromaDB vector search) for the CS knowledge base.

This is a scaffold — wire in your existing CS Knowledge Copilot retrieval
logic here (the same ChromaDB collection + BM25 index you already built).

Usage:
    python query_kb.py --query "how does SSO provisioning work" --top-k 5

Env vars:
    KB_INDEX_PATH   Path to the persisted ChromaDB collection
    KB_DOCS_PATH    Path to the raw doc corpus used for the BM25 index
"""
import argparse
import json
import os
import sys


def load_chroma_results(query: str, top_k: int):
    """Replace with your existing ChromaDB query call."""
    index_path = os.environ.get("KB_INDEX_PATH")
    if not index_path:
        return []
    # e.g.
    # import chromadb
    # client = chromadb.PersistentClient(path=index_path)
    # collection = client.get_collection("cs_docs")
    # results = collection.query(query_texts=[query], n_results=top_k)
    # return [{"source": m["source"], "text": d, "score": s}
    #          for d, m, s in zip(results["documents"][0], results["metadatas"][0], results["distances"][0])]
    return []


def load_bm25_results(query: str, top_k: int):
    """Replace with your existing BM25 index query call."""
    docs_path = os.environ.get("KB_DOCS_PATH")
    if not docs_path:
        return []
    # e.g.
    # from rank_bm25 import BM25Okapi
    # ... load corpus, tokenize query, get top_k scores ...
    return []


def merge_results(vector_results, bm25_results, top_k):
    """Simple score-fusion placeholder — replace with your reranking logic."""
    combined = {r["text"]: r for r in vector_results}
    for r in bm25_results:
        if r["text"] not in combined:
            combined[r["text"]] = r
    return list(combined.values())[:top_k]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    vector_results = load_chroma_results(args.query, args.top_k)
    bm25_results = load_bm25_results(args.query, args.top_k)
    results = merge_results(vector_results, bm25_results, args.top_k)

    if not results:
        print(json.dumps({
            "warning": "No KB index configured or no results found. "
                       "Set KB_INDEX_PATH and KB_DOCS_PATH, or wire in your "
                       "existing retrieval logic in this script.",
            "results": []
        }))
        sys.exit(0)

    print(json.dumps({"results": results}, indent=2))


if __name__ == "__main__":
    main()
