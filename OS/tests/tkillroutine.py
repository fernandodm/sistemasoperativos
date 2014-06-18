from mockito import *

import os, sys, threading, time

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from killroutine import KillRoutine
from scheduler import Scheduler
import unittest

class KillRoutineTest(unittest.TestCase):


	def setUp(self):
		self.kernel = Mock()
		self.kill = KillRoutine(self.kernel)

	def test_run(self):
		aIrq = Mock()
		aPcb = Mock()
		when(aIrq).getPcb().thenReturn(aPcb)

		aCpu = Mock()
		when(self.kernel).getCpu().thenReturn(aCpu)

		aMem = Mock()
		when(self.kernel).getMemory().thenReturn(aMem)
        
		aSched = Mock()
		when(self.kernel).getScheduler().thenReturn(aSched)
		
		self.kill.run(aIrq)

		verify(aCpu,times(1)).removePcb()
		verify(aMem, times(1)).deleteDatesForPcb(aPcb)
		verify(aSched,times(1)).getNextPcb()

suite = unittest.TestLoader().loadTestsFromTestCase(KillRoutineTest)
unittest.TextTestRunner(verbosity=2).run(suite) 