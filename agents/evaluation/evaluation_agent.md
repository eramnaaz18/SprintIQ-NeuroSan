# Evaluation Agent

## Purpose

The Evaluation Agent assesses the overall quality and implementation readiness of a Jira user story using Agile and Business Analysis best practices.

It evaluates whether a story is complete, unambiguous, testable, and ready for development by applying the INVEST principle and requirement quality standards.

---

## Responsibilities

- Retrieve Jira story
- Evaluate requirement quality
- Evaluate acceptance criteria quality
- Check INVEST compliance
- Detect ambiguity
- Detect missing information
- Assess implementation readiness
- Calculate overall quality score
- Provide recommendations for improvement

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

    "overall_score": 0,

    "readiness": "",

    "invest_score": {},

    "strengths": [],

    "weaknesses": [],

    "quality_issues": [],

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

- Requirement readability scoring
- AI quality benchmark
- Organization-specific quality rules
- Automated Definition of Ready validation
- Acceptance Criteria quality scoring