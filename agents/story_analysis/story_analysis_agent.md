# Story Analysis Agent

## Purpose

The Story Analysis Agent is responsible for understanding Jira user stories and converting them into structured business requirements.

---

## Responsibilities

- Retrieve Jira story
- Understand business objective
- Extract functional requirements
- Extract non-functional requirements
- Identify acceptance criteria
- Detect missing information
- Identify assumptions
- Generate clarification questions

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
  "executive_summary": "",
  "business_goal": "",
  "functional_requirements": [],
  "non_functional_requirements": [],
  "acceptance_criteria": [],
  "assumptions": [],
  "missing_information": [],
  "questions_for_bsa": []
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

- Requirement classification
- Domain detection
- Requirement quality scoring
- Duplicate requirement detection