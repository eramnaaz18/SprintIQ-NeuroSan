from typing import Any


def success(data: Any = None, message: str = "Success") -> dict:
    return {
        "success": True,
        "message": message,
        "data": data,
        "error": None,
    }


def failure(message: str, error: Any = None) -> dict:
    return {
        "success": False,
        "message": message,
        "data": None,
        "error": error,
    }