# SprintIQ -- Project Architecture

## High-Level Architecture

``` text
+----------------------+
|      User / CLI      |
+----------+-----------+
           |
           v
+----------------------+
|   Neuro SAN Studio   |
| Agent Network Runner |
+----------+-----------+
           |
           v
+----------------------+
|    PlannerAgent      |
| Workflow Orchestrator|
+----------+-----------+
           |
   -----------------------------
   |      |      |      |      |
   v      v      v      v      v
Story  Historical Estimation Risk Clarification
Agent     Agent      Agent     Agent    Agent
   \        |         |         |        /
    \_______|_________|_________|_______/
                    |
                    v
          +-------------------+
          | EvaluationAgent   |
          +---------+---------+
                    |
                    v
          +-------------------+
          | ReportingAgent    |
          +---------+---------+
                    |
                    v
              Final Response
```

## Neuro SAN Studio Layers

``` text
User Prompt
     |
     v
PlannerAgent
     |
     +--> StoryAnalysisAgent
     |         |
     |         +--> JiraIssueTool
     |
     +--> HistoricalAgent
     +--> EstimationAgent
     +--> RiskAgent
     +--> ClarificationAgent
     +--> EvaluationAgent
     +--> ReportingAgent
```

## Project Structure

``` text
SprintIQ/
│
├── config/
│   └── llm_config.hocon
│
├── agents/
│   ├── planner_agent.hocon
│   ├── story_analysis_agent.hocon
│   ├── historical_agent.hocon
│   ├── estimation_agent.hocon
│   ├── risk_agent.hocon
│   ├── clarification_agent.hocon
│   ├── evaluation_agent.hocon
│   └── reporting_agent.hocon
│
├── coded_tools/
│   └── jira/
│       └── jira_issue_tool.py
│
├── reports/
├── docs/
└── sprintiq.hocon
```

## Component Responsibilities

  -----------------------------------------------------------------------
  Component                    Responsibility
  ---------------------------- ------------------------------------------
  PlannerAgent                 Receives user requests, extracts the Jira
                               issue key, orchestrates workflow,
                               delegates to child agents.

  StoryAnalysisAgent           Retrieves Jira issue details and performs
                               story analysis.

  JiraIssueTool                Calls Jira APIs to fetch issue
                               information.

  HistoricalAgent              Compares the story with previous work and
                               historical patterns.

  EstimationAgent              Recommends story point estimates.

  RiskAgent                    Identifies technical and delivery risks.

  ClarificationAgent           Generates questions for missing or
                               ambiguous requirements.

  EvaluationAgent              Reviews the quality and completeness of AI
                               outputs.

  ReportingAgent               Consolidates all outputs into a final
                               report.
  -----------------------------------------------------------------------

## Current Request Flow

1.  User submits a request (e.g., `analyse ESS-11`).
2.  PlannerAgent identifies the Jira issue key.
3.  PlannerAgent delegates to StoryAnalysisAgent.
4.  StoryAnalysisAgent invokes JiraIssueTool.
5.  Jira data is analyzed.
6.  Specialized agents contribute their analyses.
7.  EvaluationAgent validates the combined output.
8.  ReportingAgent generates the final response.

## Design Principles

-   Multi-agent architecture with clear separation of responsibilities.
-   PlannerAgent acts solely as an orchestrator.
-   Specialized agents perform focused tasks.
-   Shared LLM configuration through `llm_config.hocon`.
-   Tool-based integration for external systems such as Jira.
-   Modular design enabling future expansion with additional agents and
    integrations.
