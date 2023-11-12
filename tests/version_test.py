from unittest import TestCase

from mvc_flask.__version__ import __version__


class VersionTest(TestCase):
    def test_version(self):
        self.assertEqual(__version__, "2.7.0")
