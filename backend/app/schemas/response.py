from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ErrorDetail(BaseModel):
    message: str
    code: str

class APIResponse(BaseModel, Generic[T]):
    success: bool
    data: T | None = None
    error: ErrorDetail | None = None

    @classmethod
    def ok(cls, data: Any = None) -> "APIResponse":
        return cls(success=True, data=data, error=None)

    @classmethod
    def fail(cls, message: str, code: str) -> "APIResponse":
        return cls(success=False, data=None, error=ErrorDetail(message=message, code=code))