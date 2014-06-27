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

		memMan = Mock()

		scheduler = Scheduler()

		when(self.kernel).getDisc().thenReturn(disc)
		when(self.kernel).getMemoryManager().thenReturn(memMan)
		when(self.kernel).getScheduler().thenReturn(scheduler)

		assert(scheduler.currentQueue.size() == 0)

		self.new.run(irq)

		verify(memMan,times(1)).putData(0,[inst1,inst2,inst3])

		assert(scheduler.currentQueue.size() == 1)



