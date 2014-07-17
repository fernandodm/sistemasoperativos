from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from memoryManager import MemoryManager

import unittest

class MemoryManagerTest(unittest.TestCase):

    def setUp(self):
    	self.kernel = Mock()
    	self.logicalMemory = Mock()
    	self.memoryManager = MemoryManager(self.logicalMemory, self.kernel)

    def test_getInstruction(self):
    	self.memoryManager.getInstruction(1,4)
    	verify(self.logicalMemory,times(1)).getInstruction(1,4) 

    def test_deleteDataForPcb(self):
    	pcb = Mock()
    	when(pcb).getPid().thenReturn(1)
    	self.memoryManager.deleteDataForPcb(pcb)
    	verify(self.logicalMemory,times(1)).deleteTakenBlock(1)