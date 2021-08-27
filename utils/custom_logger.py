import logging
import os
from simple_settings import settings


class LogGen:
    logcli = settings.LOG_CLI
    format = settings.LOG_CLI_FORMAT
    level = settings.LOG_CLI_LEVEL
    datefmt = settings.LOG_CLI_DATE_FORMAT
    location = settings.LOG_FILENAME
    logs_location = os.path.join(os.getcwd(), location)

    @classmethod
    def loggen(cls):
        logging.basicConfig(
            filename=cls.logs_location,
            format=cls.format,
            datefmt=cls.datefmt,
            level=cls.level,
            force=True,
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
