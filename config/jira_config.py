import os

from config.settings import *

DEFAULT_PROFILE = "SCRUM_MASTER"

JIRA_PROFILES = {

    "SCRUM_MASTER": {

        "server": os.getenv("JIRA_SERVER"),

        "username": os.getenv("SCRUM_MASTER_EMAIL"),

        "token": os.getenv("SCRUM_MASTER_TOKEN")
    },

    "BSA": {

        "server": os.getenv("JIRA_SERVER"),

        "username": os.getenv("BSA_EMAIL"),

        "token": os.getenv("BSA_TOKEN")
    },

    "DEVELOPER": {

        "server": os.getenv("JIRA_SERVER"),

        "username": os.getenv("DEVELOPER_EMAIL"),

        "token": os.getenv("DEVELOPER_TOKEN")
    }
}