from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from swapInRoutine import SwapInRoutine

import unittest

class SwapInRoutineTest(unittest.TestCase):

    def setUp(self):
    	self.kernel = Mock()
        self.swapInRoutine = SwapInRoutine(self.kernel)

    def test_run(self):
    	memManager = Mock()
    	irq = Mock()

    	when(self.kernel).getMemoryManager().thenReturn(memManager)
    	when(irq).getPid().thenReturn(1)
    	instructions = [Mock(), Mock()]
    	when(irq).getInstructions().thenReturn(instructions)
    	
    	self.swapInRoutine.run(irq)
    	
    	verify(memManager,times(1)).swapPcb(1, instructions)

suite = unittest.TestLoader().loadTestsFromTestCase(SwapInRoutineTest)
unittest.TextTestRunner(verbosity=2).run(suite) 