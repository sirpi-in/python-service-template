from fastapi.requests import Request
from fastapi import APIRouter, status

from ..middleware.logging import logger
from ..schemas.responses import CustomJSONResponse
from ..schemas.default_schemas import HOME_RESPONSE_MODEL

router = APIRouter(tags=["Utility APIs"])


@router.get(
    "/",
    description="<b>Default endpoint that serves as the entry point for the API.<b>",
    responses=HOME_RESPONSE_MODEL,
)
async def default(request: Request) -> CustomJSONResponse:
    """
    Default entry point for the FASTAPI TEMPLATE API.

    This is a public health check or informational endpoint to confirm that the
    Project microservice is running and accessible.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        CustomJSONResponse: A simple success response indicating that the service is live.
    """
    logger.info(
        "%s - %s - %s",
        request.method,
        "public",
        "Default API is being called",
    )
    return CustomJSONResponse(
        success=True,
        status_code=status.HTTP_200_OK,
        message="This is initial route of FastAPI Template",
    )
