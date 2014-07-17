from mockito import *

import os, sys, threading, time

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from killroutine import KillRoutine
from scheduler import Scheduler
from pcb import Pcb
import unittest

class KillRoutineTest(unittest.TestCase):


	def setUp(self):
		self.kernel = Mock()
		self.kill = KillRoutine(self.kernel)

	def test_run(self):
		aIrq = Mock()
		aPcb = Mock()
		instruction = Mock()
		handler = Mock()
		aDisc = Mock()
		aCpu = Mock()
		aMem = Mock()
		aSched = Mock()

		when(aIrq).getPcb().thenReturn(aPcb)
		when(self.kernel).getHandler().thenReturn(handler)
		when(self.kernel).getDisc().thenReturn(aDisc)
		when(aDisc).getInstructions().thenReturn({aPcb : [instruction]})
		when(self.kernel).getCpu().thenReturn(aCpu)
		when(self.kernel).getMemoryManager().thenReturn(aMem)
		when(self.kernel).getScheduler().thenReturn(aSched)
		
		self.kill.run(aIrq)

		verify(aCpu,times(1)).removePcb()
		verify(self.kernel,times(1)).removePcb(aPcb)
		verify(aPcb,times(1)).toExit()
		verify(aMem, times(1)).deleteDataForPcb(aPcb)
		verify(aSched,times(1)).getNextPcb()
		verify(handler,times(1)).toSwapOut()
		verify(aCpu,times(1)).assignPcb(None)
		
suite = unittest.TestLoader().loadTestsFromTestCase(KillRoutineTest)
unittest.TextTestRunner(verbosity=2).run(suite) 