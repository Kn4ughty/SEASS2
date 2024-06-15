import logging
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
log_level_str = config.get("general", "log_level")

match log_level_str.lower():
    case "debug":
        log_level = logging.DEBUG
    
    case "info":
        log_level = logging.INFO
    
    case "warning":
        log_level = logging.WARNING
    
    case "error":
        log_level = logging.ERROR
    
    case "critical":
        log_level = logging.CRITICAL
    
    case _:
        log_level = logging.WARNING


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger