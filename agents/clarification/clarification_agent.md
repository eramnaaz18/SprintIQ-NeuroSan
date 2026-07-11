# Clarification Agent

## Purpose

The Clarification Agent identifies ambiguous, incomplete, or conflicting requirements within a Jira user story and generates precise clarification questions for Business Analysts, Product Owners, and stakeholders before development begins.

---

## Responsibilities

- Retrieve Jira story
- Analyze story completeness
- Detect ambiguous requirements
- Detect missing business rules
- Detect missing acceptance criteria
- Detect missing non-functional requirements
- Detect unclear dependencies
- Detect inconsistent terminology
- Generate clarification questions
- Prioritize clarification items

---

## Input

```json
{
    "issue_key": "ESS-11"
}
```

---

## Output

```json
{
    "issue_key": "ESS-11",

    "clarification_needed": true,

    "critical_questions": [],

    "business_questions": [],

    "technical_questions": [],

    "ui_questions": [],

    "security_questions": [],

    "acceptance_criteria_questions": [],

    "recommendations": []
}
```

---

## Uses

- JiraIssueTool

---

## Called By

- PlannerAgent

---

## Future Enhancements

- AI-generated acceptance criteria
- Business rule inference
- Requirement quality scoring
- Domain-specific question generation
- Requirement completeness score