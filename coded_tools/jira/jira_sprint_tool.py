from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from config.jira_config import DEFAULT_PROFILE
from coded_tools.jira.jira_client import JiraClient


class JiraSprintTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Any:

        self.log_start("JiraSprintTool", args)

        issue_key = args.get("issue_key")
        sprint_id = args.get("sprint_id")

        if not issue_key:
            return self.failure("Missing issue_key")

        if sprint_id is None:
            return self.failure("Missing sprint_id")

        try:

            self.client.add_issue_to_sprint(
                sprint_id,
                issue_key,
            )

            self.log_end("JiraSprintTool")

            return self.success(
                {
                    "issue_key": issue_key,
                    "sprint_id": sprint_id,
                    "message": "Issue added to sprint successfully."
                }
            )

        except Exception as ex:

            return self.failure(str(ex))