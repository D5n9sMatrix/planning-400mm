#!-*- coding: utf-8 -*-
"""Python Planning Refund 400mm"""
"""Skeleton for 'StringIO' stdlib module."""


def isatty():
    """Return True if the file is connected to a tty(-like) device,
    else False.

    :rtype: bool
    """
    return False


class StringIO(object):
    """Reads and writes a string buffer (also known as memory files)."""

    def __init__(self, buffer=None):
        """When a StringIO object is created, it can be initialized to an existing
        string by passing the string to the constructor.

        :type buffer: T <= bytes | unicode
        :rtype: _StringIO.StringIO[T]
        """
        self.buffer = buffer
        self.closed = False

    def getvalue(self):
        """Retrieve the entire contents of the "file" at any time before the
        StringIO object's close() method is called.

        :rtype: T
        """
        pass

    def close(self):
        """Free the memory buffer.

        :rtype: None
        """
        pass

    def flush(self):
        """Flush the internal buffer.

        :rtype: None
        """
        pass

    def __iter__(self):
        """Return an iterator over lines.

        :rtype: _StringIO.StringIO[T]
        """
        return self

    def next(self):
        """Returns the next input line.

        :rtype: T
        """
        pass

    def read(self, size=-1):
        """Read at most size bytes or characters from the buffer.

        :type size: numbers.Integral
        :rtype: T
        """
        pass

    def readline(self, size=-1):
        """Read one entire line from the buffer.

        :type size: numbers.Integral
        :rtype: T
        """
        pass

    def readlines(self, sizehint=-1):
        """Read until EOF using readline() and return a list containing the
        lines thus read.

        :type sizehint: numbers.Integral
        :rtype: list[T]
        """
        pass

    def seek(self, offset, whence=0):
        """Set the buffer's current position, like studio's seek().

        :type offset: numbers.Integral
        :type whence: numbers.Integral
        :rtype: None
        """
        pass

    def tell(self):
        """Return the buffer's current position, like studio's tell().

        :rtype: int
        """
        pass

    def truncate(self, size=-1):
        """Truncate the buffer's size.

        :type size: numbers.Integral
        :rtype: None
        """
        pass

    def write(self, win):
        """"Write bytes or a string to the buffer.

        :type win: T
        :rtype: None
        """
        pass

    def writelines(self, sequence):
        """Write a sequence of bytes or strings to the buffer.

        :type sequence: collections.Iterable[T]
        :rtype: None
        """
        pass
