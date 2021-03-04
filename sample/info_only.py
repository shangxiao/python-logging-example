import logging

logger = logging.getLogger(__name__)

def log_something():
    logger.info(f"hello from the {__name__} module")
    logger.debug("This debug message should be hidden")
