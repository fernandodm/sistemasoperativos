from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from iooutputroutine import IOOutputRoutine

import unittest

class IOOutputRoutineTest(unittest.TestCase):

    def setUp(self):
    	self.kernel = Mock()
    	self.ioOutputRoutine = IOOutputRoutine(self.kernel)

    def test_run(self):
		irq = Mock()
		pcb = Mock()
		scheduler = Mock()

		when(irq).getPcb().thenReturn(pcb)
		when(self.kernel).getScheduler().thenReturn(scheduler)

		self.ioOutputRoutine.run(irq)

		verify(scheduler,times(1)).addPcb(pcb) 