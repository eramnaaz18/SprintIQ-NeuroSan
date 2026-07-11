from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.logger import logger

from coded_tools.jira.jira_client import JiraClient

from config.jira_config import DEFAULT_PROFILE


class JiraCommentTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Any:

        self.log_start("JiraCommentTool", args)

        issue_key = args.get("issue_key")
        comment = args.get("comment")

        if not issue_key:
            return self.failure("Missing issue_key")

        if not comment:
            return self.failure("Missing comment")

        try:

            self.client.add_comment(issue_key, comment)

            self.log_end("JiraCommentTool")

            return self.success({
                "issue_key": issue_key,
                "message": "Comment added successfully."
            })

        except Exception as ex:

            logger.exception(ex)

            return self.failure(str(ex))