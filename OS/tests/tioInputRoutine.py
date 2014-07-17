from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from ioinputroutine import IOInputRoutine

import unittest

class IOInputRoutineTest(unittest.TestCase):

    def setUp(self):
    	self.kernel = Mock()
    	self.ioInputRoutine = IOInputRoutine(self.kernel)

    def test_run(self):
		irq = Mock()
		pcb = Mock()
		cpu = Mock()
		scheduler = Mock()
		io = Mock()
		pcbNext = Mock()

		when(irq).getPcb().thenReturn(pcb)
		when(self.kernel).getCpu().thenReturn(cpu)
		when(self.kernel).getScheduler().thenReturn(scheduler)
		when(scheduler).getNextPcb().thenReturn(pcbNext)
		when(self.kernel).getIO().thenReturn(io)

		self.ioInputRoutine.run(irq)

		verify(cpu,times(1)).removePcb()
		verify(cpu,times(1)).assignPcb(pcbNext)
		verify(self.kernel,times(1)).getIO()

suite = unittest.TestLoader().loadTestsFromTestCase(IOInputRoutineTest)
unittest.TextTestRunner(verbosity=2).run(suite) 