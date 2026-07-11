# Risk Analysis Agent

## Purpose

The Risk Analysis Agent evaluates a Jira user story to identify risks that may impact sprint execution, software quality, or successful delivery.

The agent helps Scrum Masters, Product Owners, Developers, QA Engineers, and Technical Leads proactively identify potential issues before development begins.

---

## Responsibilities

- Retrieve Jira story
- Analyze implementation complexity
- Identify technical risks
- Identify business risks
- Identify dependency risks
- Identify testing risks
- Identify deployment risks
- Recommend mitigation actions
- Determine overall implementation risk

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
  "overall_risk": "",
  "technical_risks": [],
  "business_risks": [],
  "dependency_risks": [],
  "testing_risks": [],
  "deployment_risks": [],
  "security_risks": [],
  "accessibility_risks": [],
  "performance_risks": [],
  "mitigation_plan": []
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

- AI-based risk scoring
- Historical defect correlation
- Sprint capacity analysis
- Team skill assessment
- Probability vs Impact matrix
- Automatic mitigation recommendations