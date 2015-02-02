try:
    import unittest2 as unittest
except ImportError:
    import unittest

import mock

import filehandle

class TestOpen(unittest.TestCase):
    def test_opens_normal_handle(self):
        with mock.patch.object(filehandle.builtins, 'open') as mopen:
            r = filehandle.open('/path/to/foo.bar')
            mopen.assert_called_with('/path/to/foo.bar', 'rb', -1)
            self.assertEqual((mopen.return_value, 'bar'), r)

    def test_opens_gzip_handle(self):
        with mock.patch.object(filehandle, 'gzip') as mgzip:
            r = filehandle.open('/path/to/foo.bar.gz')
            mgzip.open.assert_called_with('/path/to/foo.bar.gz', 'rb', 9)
            self.assertEqual((mgzip.open.return_value, 'bar'), r)

    def test_python_missing_gzip(self):
        with mock.patch.object(filehandle, 'gzip') as mopen:
            mopen.open.side_effect = ImportError
            self.assertRaises(
                ImportError,
                filehandle.open, 'foo.bar.gz'
            )
