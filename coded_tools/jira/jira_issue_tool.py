from typing import Any, Dict

from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.logger import logger

from coded_tools.jira.jira_client import JiraClient

from config.jira_config import DEFAULT_PROFILE


class JiraIssueTool(BaseTool):

    def __init__(self, profile=DEFAULT_PROFILE):
        self.client = JiraClient(profile)

    def invoke(
        self,
        args: Dict[str, Any],
        sly_data: Dict[str, Any],
    ) -> Any:

        self.log_start("JiraIssueTool", args)

        issue_key = (
            args.get("issue_key")
            or args.get("issue_id")
        )

        if not issue_key:
            return self.failure("Missing issue_key")

        try:

            print("========== JIRA DEBUG ==========")
            print("Requested issue key:", issue_key)

            issue = self.client.get_issue(issue_key)

            print("Returned Jira key:", issue.get("key"))
            print("Returned summary:", issue.get("fields", {}).get("summary"))
            print("================================")

            fields = issue["fields"]

            result = {

                "key": issue["key"],

                "summary": fields.get("summary"),

                "description": fields.get("description"),

                "status": fields["status"]["name"],

                "priority": fields["priority"]["name"]
                if fields.get("priority")
                else None,

                "assignee": (
                    fields["assignee"]["displayName"]
                    if fields.get("assignee")
                    else None
                ),

                "reporter": (
                    fields["reporter"]["displayName"]
                    if fields.get("reporter")
                    else None
                ),

                "story_points": fields.get("customfield_10019"),

                "issue_type": fields["issuetype"]["name"],

                "labels": fields.get("labels", []),

                "subtasks": [
                    {
                        "key": s["key"],
                        "summary": s["fields"]["summary"],
                    }
                    for s in fields.get("subtasks", [])
                ]
            }

            self.log_end("JiraIssueTool")

            return self.success(result)

        except Exception as ex:

            logger.exception(ex)

            return self.failure(str(ex))