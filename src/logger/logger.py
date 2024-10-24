from logging import Logger
import logging.config
import yaml
import os
from dotenv import load_dotenv

load_dotenv() 

# Load the config file
with open('src/logger/logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# log mode
# if log_mode is not set, set it to development
log_mode = os.getenv("LOG_MODE")

# Singleton logger object
logger: Logger | None = None

def get_logger():
    global logger
    if logger is None:
        if log_mode == "development":
            logger = logging.getLogger('development')
        elif log_mode == "staging":
            logger = logging.getLogger('staging')
        elif log_mode == "production":
            logger = logging.getLogger('prod')
        else:
            logger = logging.getLogger('root')
    return logger

# Singleton testing logger
test_logger: Logger | None = None

def get_testing_logger():
    global test_logger
    if test_logger is None:
        test_logger = logging.getLogger('TESTING')
    return test_logger

# Get a logger object
dev_logger = logging.getLogger('development')
staging_logger = logging.getLogger('staging')
prod_logger = logging.getLogger('production')
root_logger = logging.getLogger('root')