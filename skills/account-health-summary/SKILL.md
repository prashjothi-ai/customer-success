---
name: account-health-summary
description: Produces a synthesized account health summary for a customer by pulling whatever CRM, support, product-usage, call-intelligence, and customer-health data sources are connected — regardless of which specific vendors (Salesforce, HubSpot, Zendesk, Intercom, Gainsight, Totango, Gong, Chorus, Amplitude, Hex, etc.) the CSM uses. Use this whenever the user asks for an account status, health check, QBR prep, renewal risk assessment, or "what's going on with [customer]" — even if they only name the account and don't specify which systems to check.
---

# Account Health Summary

Pulls cross-system signals for a named account and synthesizes them into a single health view a CSM can act on — built to work regardless of which specific tools are connected.

## Design principle: work with whatever's connected

This skill is intentionally vendor-agnostic. Do not assume any specific tool is available. Instead, think in terms of **data categories**, and check what MCP tools are actually available in this session for each one:

| Category | Typical sources (any of these, or others) | What to pull |
|---|---|---|
| CRM / account data | Salesforce, HubSpot, Pipedrive, Close | ARR/MRR, renewal date, NRR/expansion, open opportunities, last logged touchpoint |
| Support tickets | Zendesk, Intercom, Freshdesk, Help Scout | Open ticket count, severity/priority, escalations, avg. resolution time |
| Customer health / analytics platform | Gainsight, Totango, ChurnZero, Vitally | Existing health score, engagement trend, risk flags already computed by that platform |
| Product usage | Amplitude, Mixpanel, Hex, Pendo, internal dashboards | DAU/WAU/MAU or equivalent, feature adoption, usage trend direction |
| Call intelligence | Gong, Chorus, Fireflies | Sentiment trend, recent call summaries, flagged risk language (churn signals, competitor mentions, budget concerns) |

At the start of a run, check which MCP tools are actually connected in this session (do not assume — verify). Map each connected tool to the category it serves, and only pull from categories you have real access to.

## Workflow

1. **Identify the account**: Confirm the account name/ID. If ambiguous (multiple similarly named accounts), ask which one rather than guessing.

2. **Check available tools first**: Look at what's connected this session. Silently note which of the five categories above are covered and which aren't — you'll report this at the end.

3. **Pull signals from each covered category** using whatever tool serves it. If a call to a connected tool fails, say so explicitly rather than silently dropping that category.

4. **Synthesize, don't just list**: Combine whatever categories you have into a short narrative:
   - Overall health signal (green/yellow/red) with the one or two drivers behind it — based only on what was actually retrieved
   - Renewal or churn risk factors, if visible in the data
   - Recommended next action (e.g. "schedule an EBR before renewal", "escalate the open P1 ticket internally")

5. **Always state coverage**: End with a one-line note on which categories were included and which weren't connected this session (e.g. "No call-intelligence tool connected — call sentiment not included"). This is not a caveat to bury; a CSM needs to know if they're seeing a partial picture.

6. **Keep it scannable**: CSMs reading this before a call need it in under 30 seconds. Lead with the health signal and recommended action; put supporting detail and the coverage note after.

## Notes

- Never assert a churn risk or health score you can't trace back to actual retrieved data — flag inference vs. fact.
- Absence of data (no open tickets, no recent calls) is not the same as a positive signal — say so plainly.
- If zero relevant tools are connected, don't fabricate a summary — tell the user which categories of tool they'd need to connect (via `/plugin` or their MCP settings) to get a real answer, and offer to work from whatever they paste in manually instead.
