# SprintIQ

SprintIQ is an AI-powered Agile Scrum Assistant built using **Neuro SAN
Studio**. It uses a multi-agent architecture to automate Jira story
analysis, estimation, risk assessment, historical comparison,
evaluation, and reporting.

## Features

-   Multi-agent orchestration with Neuro SAN Studio
-   PlannerAgent workflow orchestration
-   Jira story analysis
-   Story point estimation
-   Risk identification
-   Historical comparison
-   Clarification generation
-   Evaluation and reporting
-   Modular HOCON configuration

## Tech Stack

-   Python 3.11+
-   Neuro SAN Studio
-   HOCON configuration
-   LangChain
-   Mistral/OpenAI compatible LLM
-   Jira REST API

## Project Structure

``` text
SprintIQ/
├── agents/
├── coded_tools/
│   └── jira/
├── config/
│   └── llm_config.hocon
├── reports/
├── docs/
├── sprintiq.hocon
└── README.md
```

## Prerequisites

-   Python 3.11 or later
-   Git
-   Jira Cloud account
-   LLM API key (for example, Mistral)

## Installation

Clone the repository:

``` bash
git clone <repository-url>
cd SprintIQ
```

Create a virtual environment:

``` bash
python -m venv .venv
```

Activate it:

Windows

``` powershell
.venv\Scripts\activate
```

Linux/macOS

``` bash
source .venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

## Environment Variables

Configure the required environment variables.

Example:

``` text
MISTRAL_API_KEY=<your_api_key>
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=<jira_email>
JIRA_API_TOKEN=<jira_api_token>
```

## LLM Configuration

Update `config/llm_config.hocon` with your preferred model, for example:

``` hocon
{
  "llm_config"{
    "class":"langchain_mistralai.chat_models.ChatMistralAI",
    "model_name":"mistral-medium-latest",
    "temperature":0
  }
}
```

## Running SprintIQ

Start Neuro SAN Studio:

``` bash
python -m neuro_san_studio run
```

Open the local Neuro SAN Studio interface and load the SprintIQ agent
network if required.

## Example Prompts

``` text
analyse ESS-11
estimate ESS-11
identify risks for ESS-11
generate report for ESS-11
```

## Current Workflow

1.  User submits a Jira issue key.
2.  PlannerAgent extracts the issue key.
3.  PlannerAgent delegates work to child agents.
4.  StoryAnalysisAgent retrieves Jira data through JiraIssueTool.
5.  Specialized agents perform analysis.
6.  ReportingAgent returns the consolidated output.

## Documentation

-   `SprintIQ_Project_Summary.md`
-   `SprintIQ_Project_Architecture.md`

## Troubleshooting

-   Verify API keys are configured.
-   Confirm Jira credentials have permission to access issues.
-   Ensure Python dependencies are installed.
-   Check Neuro SAN Studio logs for agent invocation and
    parameter-passing issues.