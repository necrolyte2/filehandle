[![Build Status](https://travis-ci.org/necrolyte2/filehandle.svg?branch=master)](https://travis-ci.org/necrolyte2/filehandle)
[![Coverage Status](https://coveralls.io/repos/necrolyte2/filehandle/badge.png?branch=master)](https://coveralls.io/r/necrolyte2/filehandle?branch=master)
[![Docs](https://readthedocs.org/projects/filehandle/badge/?version=latest)](http://filehandle.readthedocs.org/en/latest/)

filehandle
==========

Normalize the way you get file handle from either gzip or normal file

Typical way to open gzip or regular file

.. code-block:: python

    >>> import gzip
    >>> files = ['/path/to/foo.bar.gz', '/path/to/foo.bar']
    >>> for f in files:
    ...   if f.endswith('.gz'):
    ...     handle = gzip.open(f)
    ...   else:
    ...     handle = open(f)

Using filehandle
----------------

.. code-block:: python

    >>> import filehandle
    >>> files = ['/path/to/foo.bar.gz', '/path/to/foo.bar']
    >>> for f in files:
    ...   handle = filehandle.open(f)
