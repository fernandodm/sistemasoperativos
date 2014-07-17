from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from scheduler import Scheduler

import unittest

class SchedulerTest(unittest.TestCase):

	def setUp(self):
		self.cpu = Mock()
		self.queue = Mock()
		self.scheduler = Scheduler(self.cpu)
		self.scheduler.currentQueue = self.queue

	def test_getNextPcb(self):
		self.scheduler.getNextPcb()
		verify(self.queue,times(1)).getMax()

	def test_addPcb_toCpu(self):
		pcb = Mock()

		when(self.queue).isEmpty().thenReturn(True)
		when(self.cpu).havePcb().thenReturn(False)

		self.scheduler.addPcb(pcb)

		verify(pcb,times(1)).toRunning()
		verify(self.cpu,times(1)).assignPcb(pcb)

	def test_addPcb_toQueue(self):
		pcb = Mock()

		when(self.queue).isEmpty().thenReturn(False)
		when(self.cpu).havePcb().thenReturn(False)

		self.scheduler.addPcb(pcb)

		verify(self.queue,times(1)).addPcb(pcb)

	def test_removePid(self):
		self.scheduler.removePid(3)
		verify(self.queue,times(1)).removePid(3)