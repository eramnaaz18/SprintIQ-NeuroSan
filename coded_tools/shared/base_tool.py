from neuro_san.interfaces.coded_tool import CodedTool

from coded_tools.shared.logger import logger
from coded_tools.shared.response import success, failure


class BaseTool(CodedTool):

    def log_start(self, tool_name: str, args: dict):
        logger.info(f"[{tool_name}] Started")
        logger.info(f"[{tool_name}] Args : {args}")

    def log_end(self, tool_name: str):
        logger.info(f"[{tool_name}] Completed")

    def success(self, data=None, message="Success"):
        return success(data=data, message=message)

    def failure(self, message, error=None):
        return failure(message=message, error=error)