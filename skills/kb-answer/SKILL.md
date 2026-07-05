---
name: kb-answer
description: Answers customer or internal questions by searching whatever knowledge sources are connected — Notion, Confluence, Google Drive, a Zendesk/Intercom help center, or a custom vector index — and generating a grounded, cited answer. Make sure to use this skill whenever the user asks any product, feature, or "how does X work" question, asks about a policy or process, asks you to draft a customer-facing answer, or asks you to look something up — even if they don't mention "knowledge base," "docs," or any tool by name. Default to using this skill for any factual question about how a product or process works, rather than answering from general knowledge, since the user's own docs are almost always more accurate than general training knowledge for their specific product/company.
---

# KB Answer

Retrieves and synthesizes answers from wherever a CSM's team actually keeps documentation, then generates a grounded, cited response. Built to work without requiring a custom search pipeline.

## Design principle: use what's already connected

Most CSMs' knowledge lives in a tool they already have open, not a custom-built index. Check what's connected this session, roughly in this preference order:

1. **Docs/wiki MCP tools** (Notion, Confluence, Google Drive) — search directly if connected
2. **Help center MCP tools** (Zendesk Guide, Intercom Articles) — search directly if connected
3. **Custom retrieval script** (`scripts/query_kb.py`) — only if the user has set up `KB_INDEX_PATH`/`KB_DOCS_PATH` for a bespoke ChromaDB/BM25 pipeline (see `references/setup.md`). This is the power-user path, not the default expectation.

If none of the above are available, say so plainly and ask the user to paste the relevant doc/policy text, rather than guessing from general knowledge.

## Workflow

1. **Check what's connected**: Identify which docs/wiki/help-center tools are available this session.

2. **Search**: Query the connected source(s) for the user's question. If multiple sources are connected, it's fine to check more than one and combine results.

3. **Check retrieval quality**: If nothing relevant comes back, say so directly — do not fabricate an answer. Offer to search with different terms, check another connected source, or escalate to a human.

4. **Synthesize**: Write the answer in your own words based on the retrieved content. Cite the source document/article for each claim (e.g. "per the Enterprise SSO setup guide in Notion"). Keep it concise — 2-4 sentences unless the user asked for a detailed walkthrough.

5. **Format for context**: If the user is drafting a customer reply, match a professional, warm support tone. If it's an internal question, be direct and technical.

## Notes

- Never present retrieved text as a customer-facing answer verbatim without review — always paraphrase and adapt tone.
- If asked about something outside the connected sources' scope, say so rather than guessing.
- State which source an answer came from — a CSM needs to know if it's from an internal wiki vs. a public help article, since tone and audience differ.
