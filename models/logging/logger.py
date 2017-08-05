import logging
import time
import os

from logging.handlers import RotatingFileHandler

LOG_LEVEL_MAP = {
    "debug" : logging.DEBUG,
    "info" : logging.INFO,
    "warning" : logging.WARNING,
    "error" : logging.ERROR
}



def GetLogHandler(path, debug_level, prod_level):
    """
        GetLogHandler

        Parameters:
            path: string 
                The path for the log file (from config)
            debug_level: string 
                Log level for debugging (from config)
            prod_level: string 
                Log level for production (from config)

        Returns:
            A handler to add to the app object logger

        Description:
            Configures and returns a rotating file handler for file logging

    """
    handler = RotatingFileHandler(path, maxBytes=5000000, backupCount=5)
    handler.setLevel(LOG_LEVEL_MAP[debug_level] \
                        if os.environ.get('FLASK_DEBUG') == "True" \
                        else LOG_LEVEL_MAP[prod_level])
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    return handler


