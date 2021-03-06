import logging
import colorlog

def init_logger(dunder_name, debug_mode=False) -> logging.Logger:
    log_format = (
        '%(asctime)s | '
        '%(levelname)s | '
        '%(name)s | '
        '%(funcName)s | '
        '%(message)s'
    )
    bold_seq = '\033[1m'
    colorlog_format = (
        f'{bold_seq} '
        '%(log_color)s '
        f'{log_format}'
    )
    colorlog.basicConfig(format=colorlog_format)
    logger = logging.getLogger(dunder_name)

    if debug_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Output full log
    fh = logging.FileHandler('logs/server.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Output warning log
    fh = logging.FileHandler('logs/server.warning.log')
    fh.setLevel(logging.WARNING)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Output error log
    fh = logging.FileHandler('logs/server.error.log')
    fh.setLevel(logging.ERROR)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
