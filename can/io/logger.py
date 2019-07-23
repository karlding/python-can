# coding: utf-8

"""
See the :class:`Logger` class.
"""

from typing import Optional, Union

import os

import logging

from ..listener import Listener
from .generic import BaseIOHandler
from .asc import ASCWriter
from .blf import BLFWriter
from .canutils import CanutilsLogWriter
from .csv import CSVWriter
from .sqlite import SqliteWriter
from .printer import Printer

log = logging.getLogger("can.io.logger")


class Logger(BaseIOHandler, Listener):  # pylint: disable=abstract-method
    """
    Logs CAN messages to a file.

    The format is determined from the file format which can be one of:
      * .asc: :class:`can.ASCWriter`
      * .blf :class:`can.BLFWriter`
      * .csv: :class:`can.CSVWriter`
      * .db: :class:`can.SqliteWriter`
      * .log :class:`can.CanutilsLogWriter`
      * other: :class:`can.Printer`

    The log files may be incomplete until `stop()` is called due to buffering.

    .. note::
        This class itself is just a dispatcher, and any positional an keyword
        arguments are passed on to the returned instance.
    """

    @staticmethod
    def __new__(cls, filename: Optional[Union[str, os.PathLike]], *args, **kwargs):
        """
        :type filename: str or None or path-like
        :param filename: the filename/path the file to write to,
                         may be a path-like object if the target logger supports
                         it, and may be None to instantiate a :class:`~can.Printer`

        """
        if filename:
            # Since we accept PathLike objects here, we don't have access to
            # endswith. Thus, we convert to a string and then grab that value
            if isinstance(filename, os.PathLike):
                logfile = os.fspath(filename)
            else:
                logfile = filename

            if logfile.endswith(".asc"):
                return ASCWriter(logfile, *args, **kwargs)
            elif logfile.endswith(".blf"):
                return BLFWriter(logfile, *args, **kwargs)
            elif logfile.endswith(".csv"):
                return CSVWriter(logfile, *args, **kwargs)
            elif logfile.endswith(".db"):
                return SqliteWriter(logfile, *args, **kwargs)
            elif logfile.endswith(".log"):
                return CanutilsLogWriter(logfile, *args, **kwargs)

        # else:
        log.warning('unknown file type "%s", falling pack to can.Printer', filename)
        return Printer(filename, *args, **kwargs)
