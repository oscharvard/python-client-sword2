"""
Test framework - basic skeleton to simplify loading testsuite-wide data/config or even
starting up a local SWORD2 server if later tests require this.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from unittest import TestCase

class TestController(TestCase):

    def __init__(self, *args, **kwargs):
        # Load some config if required...
        TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        pass
        
    def tearDown(self):
        pass
