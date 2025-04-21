from typing import Any

from fastapi.exceptions import HTTPException


class BaseError(HTTPException):
    def __init__(self, detail: Any = None, code=422) -> None:
        super().__init__(detail=detail, status_code=code)


class CategoryBaseError(BaseError):
    def __init__(self, message) -> None:
        error = "Castegory error"
        detail = {
            "error": error,
            "message": message,
        }
        super().__init__(detail)


class CategoryNotFound(BaseError):
    def __init__(self, id) -> None:
        message = f"Category not found: {id}"
        super().__init__(message)
