from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.logger import logger
from coded_tools.jira.jira_client import JiraClient
from config.jira_config import DEFAULT_PROFILE


class JiraCreateIssueTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(self, args: Dict[str, Any], sly_data: Dict[str, Any]):

        self.log_start("JiraCreateIssueTool", args)

        try:

            issue = self.client.create_issue(
                project_key=args["project_key"],
                summary=args["summary"],
                description=args["description"],
                issue_type=args.get("issue_type", "Story")
            )

            self.log_end("JiraCreateIssueTool")

            return self.success(issue)

        except Exception as ex:

            logger.exception(ex)

            return self.failure(str(ex))