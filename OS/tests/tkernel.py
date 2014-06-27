from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from cpu import Cpu
from pcb import Pcb
from disc import Disc
from clock import Clock
from kernel import Kernel

import unittest

class KernelTest(unittest.TestCase):

    def setUp(self):
        self.IO = Mock()
        self.clock = Mock()
        self.sem = Mock()
        self.kernel = Kernel(self.IO,self.sem,1000)
        self.kernel.disc = Mock()
        self.kernel.memory = Mock()
        self.kernel.scheduler = Mock()
        self.kernel.handler = Mock()
        self.kernel.cpu = Mock()
        self.kernel.clock = Mock()
        
    def test_startUp(self):
        self.kernel.startUp()
        verify(self.kernel.cpu,times(1)).start()
        verify(self.kernel.clock,times(1)).start()

    def test_getProgramaDelDisco(self):
        self.program = Mock()
        when(self.kernel.disc).getProgram("program").thenReturn(self.program)
        self.kernel.getProgramasDelDisco("program")
        verify(self.kernel.disc,times(1)).getProgram("program")
        assert (self.kernel.getProgramasDelDisco("program") == self.program)

    def test_run(self):
        self.kernel.run("program")
        verify(self.kernel.handler,times(1)).newIrq("program")     
