# Historical Agent

## Purpose

The Historical Agent searches Jira for similar completed stories to help SprintIQ make informed decisions during estimation.

---

## Responsibilities

- Retrieve the current Jira story
- Search Jira using JQL
- Identify similar stories
- Compare complexity
- Compare functionality
- Provide historical context

---

## Input

```json
{
  "issue_key": "ESS-11"
}