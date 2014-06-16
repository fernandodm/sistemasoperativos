from mockito import *

import os, sys, threading, time

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from newroutine import NewRoutine
from scheduler import Scheduler
import unittest

class NewRoutineTest(unittest.TestCase):


	def setUp(self):
		self.kernel = Mock()
		self.new = NewRoutine(self.kernel)

	def test_run(self):
		prog = Mock()
		when(prog).getSize().thenReturn(3)
		inst1 = Mock(); inst2 = Mock(); inst3 = Mock()
		when(prog).getInstructions().thenReturn([inst1,inst2,inst3])
		when(prog).getSize().thenReturn(3)

		irq = Mock()
		when(irq).getPid().thenReturn(0)
		when(irq).getProgram().thenReturn("NameProgram")

		disc = Mock()
		when(disc).getProgram(irq.getName()).thenReturn(prog)

		mem = Mock()
		when(mem).getFirstCellWithSize(3).thenReturn(2)

		scheduler = Scheduler()

		when(self.kernel).getDisc().thenReturn(disc)
		when(self.kernel).getMemory().thenReturn(mem)
		when(self.kernel).getScheduler().thenReturn(scheduler)

		assert(scheduler.currentQueue.size() == 0)

		self.new.run(irq)

		verify(mem,times(1)).putDateInCell(inst1,2)
		verify(mem,times(1)).putDateInCell(inst2,3)
		verify(mem,times(1)).putDateInCell(inst3,4)

		assert(scheduler.currentQueue.size() == 1)



