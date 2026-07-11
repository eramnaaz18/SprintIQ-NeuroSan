from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.logger import logger

from coded_tools.jira.jira_client import JiraClient

from config.jira_config import DEFAULT_PROFILE


class JiraTransitionTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Any:

        self.log_start("JiraTransitionTool", args)

        issue_key = args.get("issue_key")
        transition = args.get("transition")

        if not issue_key:
            return self.failure("Missing issue_key")

        if not transition:
            return self.failure("Missing transition")

        try:

            self.client.transition_issue(
                issue_key,
                transition,
            )

            self.log_end("JiraTransitionTool")

            return self.success({
                "issue_key": issue_key,
                "transition": transition
            })

        except Exception as ex:

            logger.exception(ex)

            return self.failure(str(ex))