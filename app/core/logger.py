import os

from loguru import logger
from .tools import get_config


def get_logger():
    conf = get_config()
    log_dir = conf["dirs"]["logsdir"]
    log = logger
    log.add(os.path.join(log_dir, "api.log"), rotation="5MB", retention=5)

    return log
