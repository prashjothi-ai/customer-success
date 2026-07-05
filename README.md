# cs-toolkit

A Claude Code plugin for customer success work, designed to work regardless of which specific CRM, ticketing, analytics, or call-intelligence tools your team uses.

## What's included

- **`kb-answer`** — answers product/policy questions by searching whatever docs source you have connected (Notion, Confluence, Google Drive, Zendesk/Intercom help center), with a fallback path for teams with a custom retrieval pipeline.
- **`account-health-summary`** — pulls account signals across five categories (CRM, support tickets, customer health platform, product usage, call intelligence) from *whatever tools are actually connected*, and clearly states which categories were and weren't available for a given run.

## Why vendor-agnostic

CS tool stacks vary a lot team to team (Salesforce vs. HubSpot, Zendesk vs. Intercom, Gainsight vs. Totango, Gong vs. Chorus...). A plugin hardcoded to one specific combination only works for teams using that exact stack. This one instead:

- Thinks in **data categories**, not vendor names
- Checks what's actually connected each session rather than assuming
- **Degrades gracefully** — a CSM with only 2 of 5 categories connected still gets a useful, honestly-labeled partial summary instead of an error

## Setup

This plugin doesn't bundle its own MCP servers. Instead, connect whatever CRM/ticketing/docs/analytics/call-intelligence MCP servers you already use via Claude Code's `/plugin` or MCP settings — the skills will detect and use them automatically. No `.mcp.json` editing required.

If you want `kb-answer` to use a custom vector search index instead of (or alongside) a docs tool, see `skills/kb-answer/references/setup.md` and `skills/kb-answer/scripts/query_kb.py`.

### Known limitation: direct tool use vs. skill invocation

Once a docs tool (e.g. Notion) is actually connected, Claude sometimes answers a question by calling that MCP tool directly instead of routing through the `kb-answer` skill — most often for phrasings that read as a direct lookup ("tell me about X") rather than a question needing synthesis ("how does X work?"). When this happens, the underlying answer is usually still accurate since it's genuinely pulling from the connected source, but the skill's extra guarantees (retrieval-quality checks, disciplined paraphrasing, explicit source labeling) don't apply, since Claude bypassed the skill wrapper entirely. This is a known behavior of how Claude decides between using a skill and using a tool directly, not a bug specific to this plugin. If it matters for your use case, explicitly asking Claude to "use the kb-answer skill" reliably routes through it.

## Test it locally

From the parent directory of `cs-toolkit/`:

```bash
claude --plugin-dir ./cs-toolkit
```

Try prompts like:
- "How does SSO provisioning work?" (should trigger `kb-answer`)
- "Give me a health check on Acme Corp before the QBR" (should trigger `account-health-summary`)

Run `/reload-plugins` after editing SKILL.md files to pick up changes without restarting.
