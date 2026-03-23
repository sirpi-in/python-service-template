import logging
import coloredlogs
from ..core.config import settings

# ------------------------------------------------------------------------------
# Logger Configuration
# ------------------------------------------------------------------------------

logger = logging.getLogger(settings.PROJECT_NAME)
logger.setLevel(logging.DEBUG)

logger.propagate = False


if not logger.handlers:
    stream_handler = logging.StreamHandler()
    formatter = coloredlogs.ColoredFormatter(
        fmt="[%(name)s] %(asctime)s %(funcName)s:%(lineno)d - %(levelname)s - %(message)s",
        level_styles={
            "debug": {"color": "white"},
            "info": {"color": "cyan", "bold": True},
            "warning": {"color": "yellow", "bold": True},
            "error": {"color": "red", "bold": True},
            "critical": {"color": "white", "bold": True, "background": "red"},
        },
        field_styles={
            "name": {"color": "yellow", "bold": True},
            "asctime": {"color": "green"},
            "funcName": {"color": "magenta", "bold": True},
            "lineno": {"color": "red"},
            "levelname": {"color": "white", "bold": True},
            "message": {"color": "blue"},
        },
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
