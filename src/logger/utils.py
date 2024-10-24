from logger.logger import get_logger

# Get the logger object based on LOG_MODE environment variable
logger = get_logger()

def log_debug(msg: str) -> None:
    logger.debug(msg)

def log_info(msg: str) -> None:
    logger.info(msg)

def log_warning(msg: str) -> None:
    logger.warning(msg)

def log_error(msg: str) -> None:
    logger.error(msg)

def log_critical(msg: str) -> None:
    logger.critical(msg)