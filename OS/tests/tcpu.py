from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from cpu import Cpu
from pcb import Pcb
import unittest

class CpuTest(unittest.TestCase):

    def setUp(self):
        mMemory = Mock()
        mHandler = Mock()
        self.cpu = Cpu(mMemory,mHandler,0)
        self.aPcb = Pcb(0,0,0)
        self.instruction = Mock()

    def test_changeRoundRobin(self):
        self.cpu.changeRoundRobin(8)
        assert (self.cpu.roundRobin == 8)

    def test_pcIncrease(self):
        self.cpu.currentPcb = self.aPcb
        self.cpu.pcIncrease()
        assert (self.cpu.currentPcb.programCounter == 1)

    def test_assignPcb(self):
        self.cpu.assignPcb(self.aPcb)
        assert (self.cpu.currentPcb == self.aPcb)

    def test_removePcb(self):
        self.cpu.currentPcb = self.aPcb
        self.cpu.removePcb()
        assert (self.cpu.currentPcb == None)

    def test_havePcbWithPcb(self):
        self.cpu.currentPcb = self.aPcb
        assert (self.cpu.havePcb())

    def test_havePcbWithOutPcb(self):
        self.assertFalse(self.cpu.havePcb())


    def test_executeWithFullQuantum(self):
        when(self.cpu.memory).getCells().thenReturn([self.instruction])
        when(self.instruction).execute().thenReturn(False)
        when(self.instruction).isIOInstruction().thenReturn(False)
        self.cpu.currentPcb = self.aPcb
        self.cpu.quantum = 3
        self.cpu.execute()
        verify(self.cpu.handler,times(1)).toWait(self.aPcb);
        verify(self.cpu.handler,times(0)).toKill(self.aPcb)
        verify(self.cpu.handler,times(0)).toIO(self.aPcb)
        assert self.cpu.quantum == 0

    def test_executeWithOutFullQuantum(self):
        when(self.cpu.memory).getCells().thenReturn([self.instruction])
        when(self.instruction).execute().thenReturn(False)
        when(self.instruction).isIOInstruction().thenReturn(False)
        self.cpu.currentPcb = self.aPcb
        self.cpu.execute()
        verify(self.cpu.handler,times(0)).toWait(self.aPcb);
        verify(self.cpu.handler,times(0)).toKill(self.aPcb)
        verify(self.cpu.handler,times(0)).toIO(self.aPcb)
        assert self.cpu.quantum == 1

    def test_executeWithKillIntruction(self):
        when(self.cpu.memory).getCells().thenReturn([self.instruction])
        when(self.instruction).execute().thenReturn(True)
        when(self.instruction).isIOInstruction().thenReturn(False)
        self.cpu.currentPcb = self.aPcb
        self.cpu.execute()
        verify(self.cpu.handler,times(0)).toWait(self.aPcb);
        verify(self.cpu.handler,times(1)).toKill(self.aPcb)
        verify(self.cpu.handler,times(0)).toIO(self.aPcb)
        assert self.cpu.quantum == 0

    def test_executeWithIOIntruction(self):
        when(self.cpu.memory).getCells().thenReturn([self.instruction])
        when(self.instruction).execute().thenReturn(False)
        when(self.instruction).isIOInstruction().thenReturn(True)
        self.cpu.currentPcb = self.aPcb
        self.cpu.execute()
        verify(self.cpu.handler,times(0)).toWait(self.aPcb);
        verify(self.cpu.handler,times(0)).toKill(self.aPcb)
        verify(self.cpu.handler,times(1)).toIO(self.aPcb)
        assert self.cpu.quantum == 0
        
        
suite = unittest.TestLoader().loadTestsFromTestCase(CpuTest)
unittest.TextTestRunner(verbosity=2).run(suite)    
