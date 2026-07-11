import requests
from requests.auth import HTTPBasicAuth

from config.jira_config import (
    JIRA_PROFILES,
    DEFAULT_PROFILE,
)

from config.constants import (
    REQUEST_TIMEOUT,
    VERIFY_SSL,
    JIRA_API_VERSION,
)

from coded_tools.shared.logger import logger


class JiraClient:

    def __init__(self, profile: str = DEFAULT_PROFILE):

        if profile not in JIRA_PROFILES:
            raise ValueError(f"Unknown Jira profile: {profile}")

        self.profile_name = profile
        self.profile = JIRA_PROFILES[profile]

        self.server = self.profile["server"].rstrip("/")

        self.auth = HTTPBasicAuth(
            self.profile["username"],
            self.profile["token"],
        )

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        logger.info(
            f"[JiraClient] Connected using profile : {profile}"
        )

    ###########################################################
    # Generic HTTP Methods
    ###########################################################

    def _get(self, endpoint, params=None):

        url = f"{self.server}{endpoint}"

        logger.info(f"GET {url}")

        response = requests.get(
            url=url,
            headers=self.headers,
            auth=self.auth,
            params=params,
            timeout=REQUEST_TIMEOUT,
            verify=VERIFY_SSL,
        )

        response.raise_for_status()

        return response.json()

    def _post(self, endpoint, payload):

        url = f"{self.server}{endpoint}"

        logger.info(f"POST {url}")

        response = requests.post(
            url=url,
            headers=self.headers,
            auth=self.auth,
            json=payload,
            timeout=REQUEST_TIMEOUT,
            verify=VERIFY_SSL,
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        if response.text:
            return response.json()

        return {}

    ###########################################################
    # Issue APIs
    ###########################################################

    def get_issue(self, issue_key):

        endpoint = f"/rest/api/{JIRA_API_VERSION}/issue/{issue_key}"

        return self._get(endpoint)

    ###########################################################
    # Search APIs
    ###########################################################

    def search(self, jql, max_results=25):

        endpoint = f"/rest/api/{JIRA_API_VERSION}/search/jql"

        params = {
            "jql": jql,
            "maxResults": max_results,
        }

        return self._get(endpoint, params)

    ###########################################################
    # Comments
    ###########################################################

    def add_comment(self, issue_key: str, comment: str):
        endpoint = f"{self.server}/rest/api/3/issue/{issue_key}/comment"

        response = requests.post(
            endpoint,
            auth=self.auth,
            headers=self.headers,
            json={
                "body": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": comment
                                }
                            ]
                        }
                    ]
                }
            },
        )

        response.raise_for_status()

        return response.json()

    ###########################################################
    # Workflow Transition
    ###########################################################
    def get_transitions(self, issue_key: str):

        endpoint = f"/rest/api/3/issue/{issue_key}/transitions"

        return self._get(endpoint)

    def transition_issue(self, issue_key: str, transition_name: str):

        transitions = self.get_transitions(issue_key)["transitions"]

        transition_id = None

        for transition in transitions:
            if transition["name"].lower() == transition_name.lower():
                transition_id = transition["id"]
                break

        if transition_id is None:
            raise Exception(
                f"Transition '{transition_name}' not found. "
                f"Available: {[t['name'] for t in transitions]}"
            )

        endpoint = f"/rest/api/3/issue/{issue_key}/transitions"

        payload = {
            "transition": {
                "id": transition_id
            }
        }

        return self._post(endpoint, payload)

    ###########################################################
    # User
    ###########################################################

    def current_user(self):

        endpoint = (
            f"/rest/api/{JIRA_API_VERSION}/myself"
        )

        return self._get(endpoint)

    ###########################################################
    # Update Issue
    ###########################################################

    def update_issue(self, issue_key: str, fields: dict):

        endpoint = f"/rest/api/3/issue/{issue_key}"

        payload = {
            "fields": fields
        }

        return self._put(endpoint, payload)

    def _put(self, endpoint: str, payload: dict):

        url = f"{self.server}{endpoint}"

        response = requests.put(
            url=url,
            headers=self.headers,
            auth=self.auth,
            json=payload,
            timeout=REQUEST_TIMEOUT,
            verify=VERIFY_SSL,
        )

        logger.info(f"PUT {url}")

        response.raise_for_status()

        if response.text:
            return response.json()

        return {}

    ###########################################################
    # Similar Stories
    ###########################################################

    def search_similar_stories(self, issue):

        fields = issue.get("fields", {})

        project = issue["key"].split("-")[0]

        labels = fields.get("labels", [])

        components = fields.get("components", [])

        summary = fields.get("summary", "")

        keywords = summary.split()[:4]

        jql = f'project = "{project}"'

        if labels:
            jql += f' AND labels in ("{"\",\"".join(labels)}")'

        if components:
            component_names = [c["name"] for c in components]
            jql += f' AND component in ("{"\",\"".join(component_names)}")'

        if keywords:
            keyword_query = " OR ".join(
                [f'summary ~ "{k}"' for k in keywords]
            )
            jql += f" AND ({keyword_query})"

        jql += " ORDER BY created DESC"

        return self.search(jql)

    ###########################################################
    # Assignment
    ###########################################################

    def assign_issue(
        self,
        issue_key: str,
        account_id: str,
    ):

        endpoint = f"/rest/api/3/issue/{issue_key}/assignee"

        payload = {
            "accountId": account_id
        }

        return self._put(endpoint, payload)

    def get_assignable_users(self, issue_key: str):

        endpoint = "/rest/api/3/user/assignable/search"

        params = {
            "issueKey": issue_key
        }

        return self._get(endpoint, params)

    ###########################################################
    # Create Issue
    ###########################################################

    def create_issue(
        self,
        project_key: str,
        summary: str,
        description: str,
        issue_type: str = "Story",
    ):

        endpoint = f"/rest/api/{JIRA_API_VERSION}/issue"

        payload = {

            "fields": {

                "project": {
                    "key": project_key
                },

                "summary": summary,

                "issuetype": {
                    "name": issue_type
                },

                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": description
                                }
                            ]
                        }
                    ]
                }

            }

        }

        return self._post(endpoint, payload)

    ###########################################################
    # Link Issues
    ###########################################################

    def link_issues(
        self,
        inward_issue: str,
        outward_issue: str,
        link_type: str = "Relates",
    ):

        endpoint = f"/rest/api/{JIRA_API_VERSION}/issueLink"

        payload = {

            "type": {
                "name": link_type
            },

            "inwardIssue": {
                "key": inward_issue
            },

            "outwardIssue": {
                "key": outward_issue
            }

        }

        return self._post(endpoint, payload)

    ###########################################################
    # Sprint APIs
    ###########################################################

    def add_issue_to_sprint(
        self,
        sprint_id: int,
        issue_key: str,
    ):

        endpoint = f"/rest/agile/1.0/sprint/{sprint_id}/issue"

        payload = {
            "issues": [
                issue_key
            ]
        }

        return self._post(endpoint, payload)