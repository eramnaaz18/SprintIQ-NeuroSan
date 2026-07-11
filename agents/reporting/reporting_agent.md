{
  "workflow": {

    "name": "AnalyzeStoryWorkflow"

    "description": "Performs end-to-end analysis of a Jira user story using SprintIQ specialized agents."

    "entry_agent": "PlannerAgent"

    "input": {

      "issue_key": "string"

    }

    "execution": [

      {
        "agent": "StoryAnalysisAgent"
      },

      {
        "agent": "HistoricalAgent"
      },

      {
        "agent": "EstimationAgent"
      },

      {
        "agent": "RiskAgent"
      },

      {
        "agent": "EvaluationAgent"
      },

      {
        "agent": "ReportingAgent"
      }

    ]

    "output": {

      "story_analysis": "StoryAnalysisAgent",

      "historical_analysis": "HistoricalAgent",

      "estimation": "EstimationAgent",

      "risk_analysis": "RiskAgent",

      "evaluation": "EvaluationAgent",

      "report": "ReportingAgent"

    }

  }
}