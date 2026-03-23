from pydantic import BaseModel
from typing import Dict, List, Literal, Union


class SuccessfulResponse(BaseModel):
    success: bool = True
    message: str = "This is initial route of FastAPI Template"
    data: None
    error: None = None
    meta: None


class CreatedResponse(BaseModel):
    success: bool = True
    message: str = "Created"
    data: None
    error: None = None
    meta: None


class BadRequestError(BaseModel):
    code: Literal["BAD_REQUEST"]
    details: Literal[
        "The request could not be understood or was missing required parameters."
    ]


class BadRequestErrorResponse(BaseModel):
    success: bool = False
    message: str = "Bad Request"
    data: None = None
    error: BadRequestError
    meta: None = None


class UnauthorizedError(BaseModel):
    code: Literal["UNAUTHORIZED"]
    details: Union[
        Literal["Invalid token"],
        Literal["Token has expired"],
        Literal["Invalid authentication scheme"],
        Literal["Authorization header is missing"],
        Literal["Invalid authorization header format. Expected 'Bearer <token>'"],
    ]


class UnauthorizedErrorResponse(BaseModel):
    success: bool = False
    message: str = "Unauthorized"
    data: None = None
    error: UnauthorizedError
    meta: None = None


class ForbiddenErrorResponse(BaseModel):
    success: bool = False
    message: str = "Forbidden access"
    data: None = None
    error: Dict[str, str] = {
        "code": "FORBIDDEN",
        "details": "You are not authorized to access this resource.",
    }
    meta: None = None


class NotFoundErrorResponse(BaseModel):
    success: bool = False
    message: str = "Not Found"
    data: None = None
    error: Dict[str, str] = {
        "code": "NOT_FOUND",
        "details": "The requested resource could not be found.",
    }
    meta: None = None


class ConflictErrorResponse(BaseModel):
    success: bool = False
    message: str = "Conflict Error"
    data: None = None
    error: Dict[str, str] = {
        "code": "CONFLICT_ERROR",
        "details": "The resource you are trying to access is already in use.",
    }
    meta: None = None


class ValidationErrorDetails(BaseModel):
    field: str
    error: str


class ValidationErrorError(BaseModel):
    code: Literal["VALIDATION_ERROR"]
    details: List[ValidationErrorDetails]


class ValidationErrorResponse(BaseModel):
    success: bool = False
    message: Literal["Validation Error"]
    data: None = None
    error: ValidationErrorError
    meta: None = None


class TooManyRequestsError(BaseModel):
    success: bool = False
    message: str = "Too Many Requests"
    data: None = None
    error: Dict[str, str] = {
        "code": "TOO_MANY_REQUESTS",
        "details": "Rate limit exceeded. Try again later.",
    }
    meta: None = None


class BackendError(BaseModel):
    code: Literal["INTERNAL_SERVER_ERROR"]
    details: Literal[
        "Something went wrong. Please contact developers if issue persists."
    ]


class BackendErrorResponse(BaseModel):
    success: bool = False
    message: str = "Internal Server Error"
    data: None = None
    error: BackendError
    meta: None = None


HOME_RESPONSE_MODEL = {
    200: {"model": SuccessfulResponse},
    500: {"model": BackendErrorResponse},
}
