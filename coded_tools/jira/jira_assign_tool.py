from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.logger import logger

from coded_tools.jira.jira_client import JiraClient

from config.jira_config import DEFAULT_PROFILE


class JiraAssignTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Any:

        self.log_start("JiraAssignTool", args)

        issue_key = args.get("issue_key")
        account_id = args.get("account_id")

        if not issue_key:
            return self.failure("Missing issue_key")

        if not account_id:
            return self.failure("Missing account_id")

        try:

            self.client.assign_issue(
                issue_key,
                account_id
            )

            self.log_end("JiraAssignTool")

            return self.success({
                "issue_key": issue_key,
                "assigned_to": account_id
            })

        except Exception as ex:

            logger.exception(ex)

            return self.failure(str(ex))