from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from clock import Clock

import unittest

class ClockTest(unittest.TestCase):

	def setUp(self):
		self.clock = Clock()

	def test_startUp(self):
		assert (self.clock.isRunning == False)
		self.clock.startUp()
		assert (self.clock.isRunning == True)

suite = unittest.TestLoader().loadTestsFromTestCase(ClockTest)
unittest.TextTestRunner(verbosity=2).run(suite) 
