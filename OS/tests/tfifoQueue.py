from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from fifoQueue import FifoQueue

import unittest

class FifoQueueTest(unittest.TestCase):

	def setUp(self):
		self.fqueue = FifoQueue()

	def test_addPcb(self):
		aPcb = Mock()
		self.fqueue.queue = Mock()
		self.fqueue.addPcb(aPcb)
		verify(self.fqueue.queue,times(1)).put(aPcb)

	def test_getMax(self):
		aPcb = Mock()
		pcb = Mock()
		pcb2 = Mock()
		self.fqueue.addPcb(aPcb)
		self.fqueue.addPcb(pcb)
		self.fqueue.addPcb(pcb2)
		assert (self.fqueue.getMax() == aPcb)

