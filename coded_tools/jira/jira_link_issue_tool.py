from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.logger import logger
from coded_tools.jira.jira_client import JiraClient
from config.jira_config import DEFAULT_PROFILE


class JiraLinkIssueTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ):

        self.log_start("JiraLinkIssueTool", args)

        try:

            self.client.link_issues(
                inward_issue=args["inward_issue"],
                outward_issue=args["outward_issue"],
                link_type=args.get("link_type", "Relates")
            )

            self.log_end("JiraLinkIssueTool")

            return self.success({
                "message": "Issues linked successfully."
            })

        except Exception as ex:

            logger.exception(ex)

            return self.failure(str(ex))