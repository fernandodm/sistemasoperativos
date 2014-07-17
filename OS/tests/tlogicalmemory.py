from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from logicalMemory import LogicalMemory
from instruction import Instruction

import unittest

class LogicalMemoryTest(unittest.TestCase):

    def setUp(self):
        self.mainMemory = Mock()
        when(self.mainMemory).getSize().thenReturn(6)
        self.logicalMemory = LogicalMemory(self.mainMemory)

    def test_allocFreeBlock(self):
        block = self.logicalMemory.getFreeBlocks()[0]
        assert(block.getSize() == 6)
        assert(block.getBase() == 0)
        assert(block.getFinish() == 6)

    def test_allocTakenBlock(self):
        self.logicalMemory.allocTakenBlock(1,0,3)
        block = self.logicalMemory.getTakenBlocks()[1]
        assert(block.getSize() == 3)
        assert(block.getBase() == 0)
        assert(block.getFinish() == 3)

    def test_deleteTakenBlock(self):
        self.logicalMemory.allocTakenBlock(1,0,3)
        block1 = self.logicalMemory.getTakenBlocks()[1]
        assert(block1.getSize() == 3)
        assert(block1.getBase() == 0)
        assert(block1.getFinish() == 3)

        self.logicalMemory.deleteTakenBlock(1)
        block2 = self.logicalMemory.getFreeBlocks()[0]
        assert(block2.getSize() == 6)
        assert(block2.getBase() == 0)
        assert(block2.getFinish() == 6)

        keys = self.logicalMemory.getTakenBlocks().keys()
        
        assert(len(keys) == 0)
 
    def test_putData(self):
        instruction1 = Mock()
        instruction2 = Mock()
        instruction3 = Mock()
        instructionList = [instruction1, instruction2, instruction3]
        
        self.logicalMemory.putData(1, 0, instructionList)

        block1 = self.logicalMemory.getFreeBlocks()[0]
        block2 = self.logicalMemory.getTakenBlocks()[1]
        assert(block1.getSize() == 3)
        assert(block1.getBase() == 3)
        assert(block1.getFinish() == 6)

        assert(block2.getSize() == 3)
        assert(block2.getBase() == 0)
        assert(block2.getFinish() == 3)

        verify(self.mainMemory,times(1)).putDataInCell(instruction1,0)
        verify(self.mainMemory,times(1)).putDataInCell(instruction2,1)
        verify(self.mainMemory,times(1)).putDataInCell(instruction3,2)

    def test_putDataInPhysicalMemory(self):
        instruction1 = Mock()
        instruction2 = Mock()
        instruction3 = Mock()
        instructionList = [instruction1, instruction2, instruction3]
        self.logicalMemory.putDataInPhysicalMemory(0, instructionList)
        
        verify(self.mainMemory,times(1)).putDataInCell(instruction1,0)
        verify(self.mainMemory,times(1)).putDataInCell(instruction2,1)
        verify(self.mainMemory,times(1)).putDataInCell(instruction3,2)

    def test_deleteFreeBlockFor(self):
        self.logicalMemory.deleteFreeBlockFor(0,4)

        block = self.logicalMemory.getFreeBlocks()[0]
        assert(block.getSize() == 2)
        assert(block.getBase() == 4)
        assert(block.getFinish() == 6)

    def test_getInstruction(self):
        self.logicalMemory.allocTakenBlock(1,0,3)
        self.logicalMemory.getInstruction(1, 3)
        verify(self.mainMemory).getDataOfCell(3)

    def test_savePcbToDisc(self):
        pcb = Mock()
        kernel = Mock()
        disc = Mock()

        self.logicalMemory.allocTakenBlock(1,0,3)

        when(pcb).getPid().thenReturn(1)
        when(kernel).getMemory().thenReturn(self.mainMemory)
        when(kernel).getDisc().thenReturn(disc)

        self.logicalMemory.savePcbToDisc(pcb, kernel)

        verify(self.mainMemory).getDataOfCell(0)
        verify(self.mainMemory).getDataOfCell(1)
        verify(self.mainMemory).getDataOfCell(2)
        verify(disc,times(1)).saveIntructions(pcb, any(list))

    def removeDataPcb(self, aPid, aKernel, aTable):
        kernel = Mock()
        scheduler = Mock()
        pcb = Mock()
        table = {1 : pcb}
        self.logicalMemory.allocTakenBlock(1,0,3)

        when(kernel).getScheduler().thenReturn(scheduler)

        self.logicalMemory.removeDataPcb(1, kernel, table)

        keysTakenBlocks = self.logicalMemory.getTakenBlocks().keys()
        keysTable = table.keys()

        assert(len(keysTakenBlocks) == 0)
        assert(len(table) == 0)
        verify(scheduler).removePid(1)

    def test_compact(self):
        block1 = Mock()
        block2 = Mock()
        block3 = Mock()

        takenBlocks = {0:block1,1:block2,2:block3}
        when(self.logicalMemory).getFreeSize().thenReturn(10)
        when(self.logicalMemory).getTakenBlocks().thenReturn(takenBlocks)
        when(block3).getFinish().thenReturn(2)

        self.logicalMemory.compact()

        verify(block1).compact(takenBlocks,0)
        verify(block2).compact(takenBlocks,1)
        verify(block3).compact(takenBlocks,2)
        
        verify(block3,times(2)).getFinish()
        verify(self.mainMemory,times(2)).getSize()