"""
Logging configuration - reduces verbose output in production.
"""
import logging
import os

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")


def configure_logging() -> None:
    """Set up root logger with the configured level."""
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    if LOG_LEVEL.upper() != "DEBUG":
        logging.getLogger("werkzeug").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
