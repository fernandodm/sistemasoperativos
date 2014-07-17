from mockito import *

import os, sys, threading, time

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from newroutine import NewRoutine
from scheduler import Scheduler
from pcb import Pcb
import unittest

class NewRoutineTest(unittest.TestCase):


	def setUp(self):
		self.kernel = Mock()
		self.new = NewRoutine(self.kernel)

	def test_run(self):
		prog = Mock()
		inst1 = Mock(); inst2 = Mock(); inst3 = Mock()
		irq = Mock()
		disc = Mock()
		memMan = Mock()
		scheduler = Mock()

		when(prog).getSize().thenReturn(3)
		when(prog).getInstructions().thenReturn([inst1,inst2,inst3])
		when(irq).getPid().thenReturn(0)
		when(irq).getProgram().thenReturn("NameProgram")
		when(disc).getProgram(irq.getName()).thenReturn(prog)
		when(self.kernel).getDisc().thenReturn(disc)
		when(self.kernel).getMemoryManager().thenReturn(memMan)
		when(self.kernel).getScheduler().thenReturn(scheduler)
		when(memMan).putData(0,[inst1,inst2,inst3]).thenReturn(True)

		self.new.run(irq)

		verify(memMan,times(1)).putData(0,[inst1,inst2,inst3])
		verify(self.kernel,times(1)).addPcb(any(Pcb))
		verify(scheduler,times(1)).addPcb(any(Pcb))



