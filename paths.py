import os
import sys
from pathlib import Path
import logging

import config

logger = logging.getLogger()

MAIN_FOLDER = config.MAIN_FOLDER


def get_data_path() -> Path:
    """
    Get path for persistent data storage.

    I.E $XDG_DATA_HOME
    """

    if sys.platform.startswith("win"):
        os_path = os.getenv("LOCALAPPDATA")
    elif sys.platform.startswith("darwin"):
        os_path = "~/Library/Application Support"
    elif sys.platform.startswith("linux"):
        os_path = os.getenv("XDG_DATA_HOME")
        if os_path is None:
            logger.warn("$XDG_CONFIG_HOME envvariable not found. Using $HOME")
            os_path = os.getenv("HOME")
            if os_path is None:
                logger.warn("The $HOME variable was not found. What even the heck.")
                os_path = "~/.local/share"
            os_path += "/.local/share"
    else:
        logging.error("Unknown os. Cant continue.")

    logger.debug(f"os_path set to {os_path}")

    return Path(os_path).expanduser() / MAIN_FOLDER


DATA_PATH = get_data_path()
