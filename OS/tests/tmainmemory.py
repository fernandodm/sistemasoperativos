from mockito import *

import os, sys, threading, time

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from mainmemory import MainMemory

import unittest

class MainMemoryTest(unittest.TestCase):

	def setUp(self):
		self.memory = MainMemory()
		self.date = Mock()

	def test_putDateInCellRegular(self):
		self.memory.putDateInCell(self.date,0)
		assert(self.memory.cells[0] == self.date)

	def test_putDateInCellInMiddle(self):
		self.memory.cells = {0:Mock(), 1:Mock(), 2:Mock()}
		self.memory.putDateInCell(self.date,1)
		assert(self.memory.cells[1] == self.date)
		assert(len(self.memory.cells) == 3)

	def test_putDateInCellInNotAssignedPosition(self):
		self.memory.cells = {0:Mock(), 1:Mock(), 2:Mock()}
		self.memory.putDateInCell(self.date,8)
		assert(self.memory.cells[8] == self.date)
		assert(len(self.memory.cells) == 4)

	def test_deleteDatesForPcb(self):
		aPcb = Mock()
		self.memory.cells = {0:Mock(), 1:Mock(), 2:Mock(), 3:Mock(), 4:Mock(), 5:Mock()}
		when(aPcb).getBasePointer().thenReturn(1)
		when(aPcb).getSize().thenReturn(3)
		self.memory.deleteDatesForPcb(aPcb)
		for i in range (1,3):
			assert(self.memory.cells[i] == None)
		assert(len(self.memory.cells) == 6)

	def test_getFirstFreeCellWithSize(self):
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None}
		assert(self.memory.getFirstFreeCellWithSize(2) == 4)


suite = unittest.TestLoader().loadTestsFromTestCase(MainMemoryTest)
unittest.TextTestRunner(verbosity=2).run(suite) 