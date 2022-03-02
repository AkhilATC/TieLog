import logging
import logging.handlers
from logging import Formatter
import os
import zlib


def namer(name):
    return name + ".gz"


def rotator(source, dest):
    print(f'compressing {source} -> {dest}')
    with open(source, "rb") as sf:
        data = sf.read()
        compressed = zlib.compress(data, 9)
        with open(dest, "wb") as df:
            df.write(compressed)
    os.remove(source)


class SizeBasedLogRotater:

    def __init__(self, size=100, rotate=5, filename="temp"):
        """
        init log rotation params
        """

        filename = f"{filename}.log"
        format_ = '%(asctime)s - %(levelname)s - %(message)s'
        formatter = Formatter(format_)
        level = logging.DEBUG
        logging.basicConfig(format=format_, datefmt="%Y-%m-%dT%H:%M:%S%z", level=level)
        self.logger = logging.getLogger("Size split rotation")
        handler = logging.handlers.RotatingFileHandler(
            filename=f"{os.getcwd()}/{filename}",
            maxBytes=size,
            backupCount=rotate
        )
        handler.setFormatter(formatter)
        handler.rotator = rotator
        handler.namer = namer
        self.logger.addHandler(handler)

    def as_logger(self):
        return self.logger


class TimeBasedLogRotator:

    def __init__(self, rotate=5, filename="temp", interval=10, time_span="m"):

        filename = f"{filename}.log"
        format_ = '%(asctime)s - %(levelname)s - %(message)s'
        formatter = Formatter(format_)
        level = logging.DEBUG
        logging.basicConfig(format=format_, datefmt="%Y-%m-%dT%H:%M:%S%z", level=level)
        self.logger = logging.getLogger("Time split rotation")
        handler = logging.handlers.TimedRotatingFileHandler(
            filename=f"{os.getcwd()}/{filename}",
            when=time_span,
            interval=interval,
            backupCount=rotate
        )
        handler.setFormatter(formatter)
        handler.rotator = rotator
        handler.namer = namer
        self.logger.addHandler(handler)

    def as_logger(self):
        return self.logger