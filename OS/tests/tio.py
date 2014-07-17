from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from io import IO
from irq import Irq

import unittest

class IOTest(unittest.TestCase):

    def setUp(self):
    	self.kernel = Mock()
        self.io = IO(self.kernel)

    def test_queueisEmpty_true(self):
    	assert(self.io.queueisEmpty())

    def test_queueisEmpty_false(self):
    	instruction = Mock()
    	self.io.getQueue().put(instruction)
    	assert(not self.io.queueisEmpty())

    def test_receivePcb(self):
    	pcb = Mock()
    	self.io.receivePcb(pcb)
    	assert(not self.io.queueisEmpty())

    def test_fetch(self):
    	pcb = Mock()
    	self.io.receivePcb(pcb)
    	assert(not self.io.queueisEmpty())
    	self.io.fetch()
    	assert(self.io.queueisEmpty())


    def test_run(self):
    	pcb = Mock()
    	memManager = Mock()
    	handler = Mock()
    	instruction = Mock()
    	self.io.receivePcb(pcb)

    	when(self.kernel).getMemoryManager().thenReturn(memManager)
    	when(memManager).getInstruction(1, 5).thenReturn(instruction)
    	when(self.kernel).getHandler().thenReturn(handler)
    	when(pcb).getPid().thenReturn(1)
    	when(pcb).getDisplacement().thenReturn(5)

    	self.io.run()
    	
    	verify(handler,times(1)).handler(any(Irq))

suite = unittest.TestLoader().loadTestsFromTestCase(IOTest)
unittest.TextTestRunner(verbosity=2).run(suite) 