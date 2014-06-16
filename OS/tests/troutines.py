from mockito import *

import os, sys, threading, time

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from routines import Routines
from newroutine import NewRoutine
from killroutine import KillRoutine
from timeoutroutine import TimeOutRoutine
from interruption import Interruption
import unittest

class RoutinesTest(unittest.TestCase):

	def setUp(self):
		self.r = Routines(Mock())
		self.classNew = Mock()
		self.classKill = Mock()
		self.classTime = Mock()
		self.r.routines = {Interruption.NEW : self.classNew, Interruption.KILL: self.classKill, Interruption.TIMEOUT: self.classTime}

	def test_returnRoutineType_New(self):
		irq = Mock()
		when(irq).getType().thenReturn(Interruption.NEW)
		assert(self.r.returnRoutineType(irq) == self.classNew)

	def test_returnRoutineType_Kill(self):
		irq = Mock()
		when(irq).getType().thenReturn(Interruption.KILL)
		assert(self.r.returnRoutineType(irq) == self.classKill)

	def test_returnRoutineType_TimeOut(self):
		irq = Mock()
		when(irq).getType().thenReturn(Interruption.TIMEOUT)
		assert(self.r.returnRoutineType(irq) == self.classTime)

	def test_execute_WithNewIrq(self):
		irq = Mock()
		when(irq).getType().thenReturn(Interruption.NEW)
		self.r.execute(irq)
		verify(self.classNew,times(1)).run(irq)

	def test_execute_WithKillIrq(self):
		irq = Mock()
		when(irq).getType().thenReturn(Interruption.KILL)
		self.r.execute(irq)
		verify(self.classKill,times(1)).run(irq)

	def test_execute_WithTimeIrq(self):
		irq = Mock()
		when(irq).getType().thenReturn(Interruption.TIMEOUT)
		self.r.execute(irq)
		verify(self.classTime,times(1)).run(irq)
