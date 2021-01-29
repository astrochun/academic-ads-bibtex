from pathlib import Path
from typing import Union
import sys

import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)8s: %(message)s', "%H:%M:%S")
file_formatter = logging.Formatter('%(asctime)s %(levelname)8s - %(module)10s %(funcName)15s : %(message)s',
                                   "%H:%M:%S")


class LogClass:
    """
    Main class to log information to stdout and ASCII logfile.

    Note: Logging level is set to DEBUG for file and INFO for stdout

    To use:
      ``log = LogClass(logfile).get_logger()``

    :param logfile: Filename for log file
    """

    def __init__(self, logfile: Union[str, Path]):
        self.LOG_FILENAME = logfile

    def get_logger(self) -> logging.Logger:
        file_log_level = logging.DEBUG  # This is for file logging
        log = logging.getLogger("main_logger")
        if not log.handlers:
            log.setLevel(file_log_level)

            sh = logging.StreamHandler(sys.stdout)
            sh.setLevel(logging.INFO)  # Only at INFO level
            sh.setFormatter(formatter)
            log.addHandler(sh)

            fh = logging.FileHandler(self.LOG_FILENAME)
            fh.setLevel(file_log_level)
            fh.setFormatter(file_formatter)
            log.addHandler(fh)

            log.handler_set = True
            log.propagate = False
        return log


def log_stdout() -> logging.Logger:
    """Stdout logging"""

    log_level = logging.INFO
    log = logging.getLogger("stdout_logger")
    if not log.handlers:
        log.setLevel(log_level)
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        log.addHandler(sh)

        log.handler_set = True
        log.propagate = False
    return log
