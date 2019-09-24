# -*- coding: utf-8 -*-
# @Time    : 2019-09-07 07:37
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : colored.py
# @Explain : About the combined other module with sheen

import logging
from sheen.color import Str
from logging import StreamHandler, _addHandlerRef, _checkLevel, NOTSET, Formatter

# 公开给外部的函数 (interface)
__all__ = (
    'ColoredHandler',  # Design colored logger for yourself to integrate more imagination
    'FMT_DEFAULT',
    'FMT_DEBUG',
    'FMT_INFO',
    'FMT_WARNING',
    'FMT_ERROR',
    'FMT_CRITICAL'
)

FMT_TIME = Str.cyan.Underline("%(asctime)s")
FMT_NAME = Str.lightcyan("[%(name)s]")
FMT_LEVEL = Str.cyan("%(levelname)s: ")
FMT_MSG = Str("%(message)s")
FMT_DATE = "%Y-%m-%d %X"  # default date format
FMT_PREFIX = Str(' ').join([FMT_TIME, FMT_NAME, FMT_LEVEL])

# init Config
FMT_DEFAULT = FMT_PREFIX + FMT_MSG
FMT_DEBUG = FMT_PREFIX + Str.lightblack(FMT_MSG)
FMT_INFO = FMT_PREFIX + Str.green(FMT_MSG)
FMT_WARNING = FMT_PREFIX + Str.yellow(FMT_MSG)
FMT_ERROR = FMT_PREFIX + Str.red(FMT_MSG)
FMT_CRITICAL = FMT_PREFIX + Str.RED(FMT_MSG)

_defaultFormatter = Formatter(fmt=str(FMT_DEFAULT), datefmt=FMT_DATE)  # default Formatter


class ColoredHandler(StreamHandler):
    def __init__(self, level=NOTSET, stream=None):
        """
        Initializes the instance - basically setting the formatter to None
        and the filter list to empty.
        """
        StreamHandler.__init__(self, stream)
        self._name = None
        self.level = _checkLevel(level)
        self.formatter = {
            logging.DEBUG: Formatter(fmt=str(FMT_DEBUG), datefmt=FMT_DATE),
            logging.INFO: Formatter(fmt=str(FMT_INFO), datefmt=FMT_DATE),
            logging.WARNING: Formatter(fmt=str(FMT_WARNING), datefmt=FMT_DATE),
            logging.ERROR: Formatter(fmt=str(FMT_ERROR), datefmt=FMT_DATE),
            logging.CRITICAL: Formatter(fmt=str(FMT_CRITICAL), datefmt=FMT_DATE),
        }
        # Add the handler to the global _handlerList (for cleanup on shutdown)
        _addHandlerRef(self)
        self.createLock()

    def format(self, record):
        fmt = self.formatter.get(record.levelno, None)
        if fmt is None:
            fmt = _defaultFormatter
        return fmt.format(record)

    def setFormatter(self, fmt):
        raise ValueError("Did you mean 'setFormatters'? (There is a 's' at the end)")

    def setFormatters(self, fmts):
        """
            Design colored logger for yourself to integrate more imagination.
        ```
            handle = ColoredHandle()
            handle.setFormatter({
                    logging.DEBUG: Formatter(fmt=str(Str.lightblack(fmt)), datefmt=datefmt), # 'Formatter' Type
                    logging.INFO: Str.green(fmt),  # 'Str' or 'str' Type
                })
        ```
        """
        if isinstance(fmts, dict):
            formats = {}
            for key, value in fmts.items():
                if isinstance(value, Formatter):
                    formats[key] = value
                else:
                    formats[key] = Formatter(str(value), datefmt=FMT_DATE)
            else:
                self.formatter.update(formats)
        else:
            raise ValueError("""
            [!] the parameter fmts receive format like this (support 2 types):
            ```
                handle = ColoredHandle()
                handle.setFormatter({
                    logging.DEBUG: Formatter(fmt=str(Str.lightblack(fmt)), datefmt=datefmt), # 'Formatter' Type
                    logging.INFO: Str.green(fmt),  # 'Str' or 'str' Type
                })
            ```
            """)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handle = ColoredHandle()
    handle.setFormatters({
        logging.DEBUG: Formatter(fmt=str(Str.blue('%(asctime)s - %(levelname)s | %(message)s')), datefmt=FMT_DATE),
        logging.INFO: Str.magenta('%(asctime)s - %(levelname)s | %(message)s'),
    })
    logger.addHandler(handle)

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
