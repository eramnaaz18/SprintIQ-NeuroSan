# SprintIQ -- Project Summary

## Overview

SprintIQ is an AI-powered Agile Scrum Assistant built using **Neuro SAN
Studio** to automate Scrum and Jira-centric activities. It uses a
multi-agent architecture where each AI agent is responsible for a
specific task, allowing complex workflows to be executed through
orchestration rather than a single monolithic prompt.

The current MVP focuses on Jira story analysis, estimation, risk
identification, historical comparison, clarification generation,
evaluation, and report generation. The long-term vision is to evolve
SprintIQ into an enterprise AI Scrum Copilot supporting the complete
Agile software development lifecycle.

## Objectives

-   Automate repetitive Scrum activities around Jira.
-   Improve story quality and planning accuracy.
-   Provide AI-assisted estimation and risk analysis.
-   Generate structured reports for Scrum teams.
-   Maintain human approval for critical Jira actions.

## Current Architecture

### Neuro SAN Studio

SprintIQ is built on Neuro SAN Studio using: - HOCON-based
configuration - Multi-agent orchestration - Shared LLM configuration
(`config/llm_config.hocon`) - Custom Python tools - Streaming execution
for debugging and observability

### AI Agents

-   **PlannerAgent** -- Orchestrates the workflow and delegates work.
-   **StoryAnalysisAgent** -- Retrieves and analyzes Jira stories.
-   **HistoricalAgent** -- Compares similar historical work.
-   **EstimationAgent** -- Suggests story point estimates.
-   **RiskAgent** -- Identifies technical and delivery risks.
-   **ClarificationAgent** -- Generates clarification questions for
    incomplete requirements.
-   **EvaluationAgent** -- Reviews output quality and completeness.
-   **ReportingAgent** -- Produces the consolidated SprintIQ report.

### Custom Tool

**JiraIssueTool** connects with Jira APIs to retrieve issue details for
downstream analysis.

## Workflow

Example user request:

`analyse ESS-11`

1.  PlannerAgent detects the Jira issue key.
2.  PlannerAgent invokes StoryAnalysisAgent.
3.  StoryAnalysisAgent calls JiraIssueTool.
4.  Jira details are analyzed.
5.  Historical, estimation, risk, clarification, and evaluation agents
    contribute their outputs.
6.  ReportingAgent generates the final report.

## Current MVP Features

-   Multi-agent workflow orchestration
-   Jira issue retrieval
-   Story analysis
-   Story point estimation
-   Risk assessment
-   Historical comparison framework
-   Clarification generation
-   Evaluation
-   Report generation
-   Modular and extensible architecture

## Current Status

The Neuro SAN Studio environment, agent network, and shared LLM
configuration are operational. Current development focuses on refining
agent-to-agent parameter passing, improving orchestration reliability,
and completing end-to-end Jira analysis before expanding into broader
Jira automation.

## Future Direction

Planned enhancements include Jira automation, sprint and backlog
management, AI-powered planning agents, Microsoft Teams and Outlook
integration, advanced reporting, predictive analytics, semantic search,
human-in-the-loop approvals, enterprise security, and performance
optimizations.

SprintIQ is being designed as a scalable, enterprise-ready AI platform
that combines intelligent automation with transparent, human-controlled
decision making for Agile teams.
