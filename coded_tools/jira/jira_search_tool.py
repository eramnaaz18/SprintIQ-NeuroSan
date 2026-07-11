from coded_tools.shared.base_tool import BaseTool
from coded_tools.shared.response import success_response, error_response
from coded_tools.shared.logger import logger

from coded_tools.jira.jira_client import JiraClient


class JiraSearchTool(BaseTool):

    def __init__(self):

        self.client = JiraClient()

    def invoke(self, args, sly_data):

        logger.info("[JiraSearchTool] Started")

        logger.info(f"[JiraSearchTool] Args : {args}")

        issue_key = args.get("issue_key")

        if not issue_key:

            return error_response("issue_key is required")

        try:

            issue = self.client.get_issue(issue_key)

            response = self.client.search_similar_stories(issue)

            stories = []

            for item in response.get("issues", []):

                fields = item["fields"]

                stories.append({

                    "issue_key": item["key"],

                    "summary": fields.get("summary"),

                    "story_points": fields.get("customfield_10019"),

                    "status": fields["status"]["name"]

                })

            return success_response(

                "Similar stories found",

                stories

            )

        except Exception as ex:

            logger.exception(ex)

            return error_response(str(ex))