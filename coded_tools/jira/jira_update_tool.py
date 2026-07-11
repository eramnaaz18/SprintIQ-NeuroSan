from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.logger import logger

from coded_tools.jira.jira_client import JiraClient
from config.jira_config import DEFAULT_PROFILE


class JiraUpdateTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Any:

        self.log_start("JiraUpdateTool", args)

        issue_key = args.get("issue_key")
        fields = args.get("fields")

        if not issue_key:
            return self.failure("Missing issue_key")

        if not fields:
            return self.failure("Missing fields")

        try:

            self.client.update_issue(issue_key, fields)

            self.log_end("JiraUpdateTool")

            return self.success({
                "issue_key": issue_key,
                "updated_fields": list(fields.keys())
            })

        except Exception as ex:

            logger.exception(ex)

            return self.failure(str(ex))