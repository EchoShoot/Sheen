# -*- coding: utf-8 -*-
# @Time    : 2019-09-07 07:37
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : colored.py
# @Explain : About the combined other module with sheen

import logging
from sheen.color import Str
import sys
from logging import StreamHandler, _addHandlerRef, _checkLevel, NOTSET, Formatter, Handler, getLevelName
from functools import singledispatch, update_wrapper
from collections.abc import MutableMapping


# 指向性单分派函数
def directivitysingledispatch(target=0):
    """ more powerful than singledispatch, it can aimed which param is your want """

    def ooo(func):
        dispatcher = singledispatch(func)

        def wrapper(*args, **kw):
            if isinstance(target, int):
                obj_cls = args[target]
                return dispatcher.dispatch(obj_cls.__class__)(*args, **kw)
            elif isinstance(target, str):
                kw.update(dict(zip(func.__code__.co_varnames, args)))
                obj_cls = kw[target]
                return dispatcher.dispatch(obj_cls.__class__)(**kw)
            else:
                raise TypeError("the param 'target' only support the type of 'int' or 'str'")

        wrapper.register = dispatcher.register
        update_wrapper(wrapper, func)
        return wrapper

    return ooo


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
FMT_INFO = FMT_PREFIX + Str(FMT_MSG)
FMT_WARNING = FMT_PREFIX + Str.yellow(FMT_MSG)
FMT_ERROR = FMT_PREFIX + Str.red(FMT_MSG)
FMT_CRITICAL = FMT_PREFIX + Str.RED(FMT_MSG)

_defaultFormatter = Formatter(fmt=str(FMT_DEFAULT), datefmt=FMT_DATE)  # default Formatter


class ColoredHandler(Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a stream. Note that this class does not close the stream, as
    sys.stdout or sys.stderr may be used.
    """

    terminator = '\n'

    def __init__(self, stream=None):
        """
        Initialize the handler.

        If stream is not specified, sys.stderr is used.
        """
        Handler.__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = stream
        self.formatter = {
            logging.DEBUG: Formatter(fmt=str(FMT_DEBUG), datefmt=FMT_DATE),
            logging.INFO: Formatter(fmt=str(FMT_INFO), datefmt=FMT_DATE),
            logging.WARNING: Formatter(fmt=str(FMT_WARNING), datefmt=FMT_DATE),
            logging.ERROR: Formatter(fmt=str(FMT_ERROR), datefmt=FMT_DATE),
            logging.CRITICAL: Formatter(fmt=str(FMT_CRITICAL), datefmt=FMT_DATE),
        }

    def format(self, record):
        fmt = self.formatter.get(record.levelno, None)
        if fmt is None:
            fmt = _defaultFormatter
        return fmt.format(record)

    @directivitysingledispatch(1)
    def setFormatter(self, fmt):
        """
        Set the formatter for this handler.
        """
        raise TypeError(f"Not support '{type(fmt)}' yet, only support 'Formatter' or 'Dict'")

    @setFormatter.register(Formatter)
    def _(self, fmt):
        """
        Set the formatter for this handler.
        """
        self.formatter = {
            logging.DEBUG: Formatter(fmt=str(Str.lightblack(fmt._fmt)), datefmt=fmt.datefmt),
            logging.INFO: Formatter(fmt=str(Str(fmt._fmt)), datefmt=fmt.datefmt),
            logging.WARNING: Formatter(fmt=str(Str.yellow(fmt._fmt)), datefmt=fmt.datefmt),
            logging.ERROR: Formatter(fmt=str(Str.red(fmt._fmt)), datefmt=fmt.datefmt),
            logging.CRITICAL: Formatter(fmt=str(Str.RED(fmt._fmt)), datefmt=fmt.datefmt),
        }

    @setFormatter.register(MutableMapping)
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
                handle.setFormatters({
                    logging.DEBUG: Formatter(fmt=str(Str.lightblack(fmt)), datefmt=datefmt), # 'Formatter' Type
                    logging.INFO: Str.green(fmt),  # 'Str' or 'str' Type
                })
            ```
            """)

    def flush(self):
        """
        Flushes the stream.
        """
        self.acquire()
        try:
            if self.stream and hasattr(self.stream, "flush"):
                self.stream.flush()
        finally:
            self.release()

    def emit(self, record):
        """
        Emit a record.

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        try:
            msg = self.format(record)
            stream = self.stream
            # issue 35046: merged two stream.writes into one.
            stream.write(msg + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

    def setStream(self, stream):
        """
        Sets the StreamHandler's stream to the specified value,
        if it is different.

        Returns the old stream, if the stream was changed, or None
        if it wasn't.
        """
        if stream is self.stream:
            result = None
        else:
            result = self.stream
            self.acquire()
            try:
                self.flush()
                self.stream = stream
            finally:
                self.release()
        return result

    def __repr__(self):
        level = getLevelName(self.level)
        name = getattr(self.stream, 'name', '')
        if name:
            name += ' '
        return '<%s %s(%s)>' % (self.__class__.__name__, name, level)


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handle = ColoredHandler()
    # handle.setFormatter(Formatter(fmt='%(asctime)s - %(levelname)s | %(message)s'))
    handle.setFormatter({
        logging.DEBUG: Formatter(fmt=str(Str.blue('%(asctime)s - %(levelname)s | %(message)s')), datefmt=FMT_DATE),
        logging.INFO: Str.magenta('%(asctime)s - %(levelname)s | %(message)s'),
    })
    logger.addHandler(handle)

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
