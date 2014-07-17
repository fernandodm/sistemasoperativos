from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from logicalMemory import LogicalMemory

import unittest

class LogicalMemoryTest(unittest.TestCase):

    def setUp(self):
    	self.mainMemory = Mock()
    	when(self.mainMemory).getSize().thenReturn(6)
    	self.logicalMemory = LogicalMemory(self.mainMemory)


    def test_allocTakenBlock(self):
    	self.logicalMemory.allocTakenBlock(1,0,3)
    	block = self.logicalMemory.getTakenBlocks()[1]
    	assert(block.getSize() == 3)
    	assert(block.getBase() == 0)
    	assert(block.getFinish() == 3)
   

suite = unittest.TestLoader().loadTestsFromTestCase(LogicalMemoryTest)
unittest.TextTestRunner(verbosity=2).run(suite) 