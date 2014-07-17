from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from timeoutroutine import TimeOutRoutine

import unittest

class TimeOutRoutineTest(unittest.TestCase):

	def setUp(self):
		self.kernel = Mock()
		self.timeout = TimeOutRoutine(self.kernel)

	def test_run(self):

		cpu = Mock()
		irq = Mock()
		pcb = Mock()
		nextPcb = Mock()
		scheduler = Mock()

		when(self.kernel).getCpu().thenReturn(cpu)

		when(irq).getPcb().thenReturn(pcb)

		when(self.kernel).getScheduler().thenReturn(scheduler)

		when(scheduler).getNextPcb().thenReturn(nextPcb)

		self.timeout.run(irq)

		verify(cpu,times(1)).removePcb()
		verify(pcb,times(1)).toWait()
		verify(scheduler,times(1)).addPcb(pcb)
		verify(cpu,times(1)).assignPcb(nextPcb)