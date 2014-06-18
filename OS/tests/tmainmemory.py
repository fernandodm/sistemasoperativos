from mockito import *

import os, sys, threading, time

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from mainmemory import MainMemory
from firstsetting import FirstSetting
from lastsetting import LastSetting
from badwaysetting import BadWaySetting
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

	def test_getFirstFreeCellWithSize_regular(self):
		self.memory.setting = FirstSetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(), 7:None, 8:None}
		assert(self.memory.getFreeCellWithSize(2) == 4)

	def test_getFirstFreeCellWithSize_full_compress(self):
		self.memory.setting = FirstSetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(), 7:None, 8:None}
		assert(self.memory.getFreeCellWithSize(3) == 4)

	def test_getFirstFreeCellWithSize_full_full(self):
		self.memory.setting = FirstSetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(), 7:None, 8:None}
		assert(self.memory.getFreeCellWithSize(6) == None)	

	def test_getLastFreeCellWithSize_regular(self):
		self.memory.setting = LastSetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(), 7:None, 8:None}
		assert(self.memory.getFreeCellWithSize(2) == 7)

	def test_getLastFreeCellWithSize_full_compress(self):
		self.memory.setting = LastSetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(), 7:None, 8:None}
		assert(self.memory.getFreeCellWithSize(3) == 5)

	def test_getLastFreeCellWithSize_full_full(self):
		self.memory.setting = LastSetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(), 7:None, 8:None}
		assert(self.memory.getFreeCellWithSize(6) == None)

	def test_getBadWayWithSize_regular(self):
		self.memory.setting = BadWaySetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(),
		 7:None, 8:None, 9:None, 10:None, 11:Mock(), 12:Mock(), 13:None, 14:None}
		assert(self.memory.getFreeCellWithSize(2) ==7)

	def test_getBadWayWithSize_full_compress(self):
		self.memory.setting = BadWaySetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(),
		7:None, 8:None, 9:None, 10:None, 11:Mock(), 12:Mock(), 13:None, 14:None}
		assert(self.memory.getFreeCellWithSize(5) == 6)

	def test_getBadWayWithSize_full_full(self):
		self.memory.setting = BadWaySetting()
		self.memory.cells = {0:Mock(), 1:None, 2:Mock(), 3:Mock(), 4:None, 5:None, 6:Mock(),
		7:None, 8:None, 9:None, 10:None, 11:Mock(), 12:Mock(), 13:None, 14:None}
		assert(self.memory.getFreeCellWithSize(10) == None)

suite = unittest.TestLoader().loadTestsFromTestCase(MainMemoryTest)
unittest.TextTestRunner(verbosity=2).run(suite) 
