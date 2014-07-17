from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from bestsetting import BestSetting

import unittest

class BestSettingTest(unittest.TestCase):

	def setUp(self):
		self.best = BestSetting()
		self.block1 = Mock()
		self.block2 = Mock()
		self.block3 = Mock()
		self.freeBlocks = [self.block1,self.block2,self.block3]

	def test_getFreeCellWithSize_found(self):
		when(self.block1).getSize().thenReturn(3)
		when(self.block1).getBase().thenReturn(0)

		when(self.block2).getSize().thenReturn(1)
		when(self.block2).getBase().thenReturn(5)

		when(self.block3).getSize().thenReturn(7)
		when(self.block3).getBase().thenReturn(10)

		assert self.best.getFreeCellWithSize(self.freeBlocks,3) == 0

	def test_getFreeCellWithSize_notFound(self):
		when(self.block1).getSize().thenReturn(3)
		when(self.block1).getBase().thenReturn(0)

		when(self.block2).getSize().thenReturn(1)
		when(self.block2).getBase().thenReturn(5)

		when(self.block3).getSize().thenReturn(7)
		when(self.block3).getBase().thenReturn(10)

		assert self.best.getFreeCellWithSize(self.freeBlocks,8) == None
		
