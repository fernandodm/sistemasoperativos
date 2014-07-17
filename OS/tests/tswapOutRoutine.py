from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from swapOutRoutine import SwapOutRoutine

import unittest

class SwapOutRoutineTest(unittest.TestCase):

    def setUp(self):
    	self.kernel = Mock()
        self.swapOutRoutine = SwapOutRoutine(self.kernel)

    def test_run(self):
    	memManager = Mock()
        irq = Mock()
    	when(self.kernel).getMemoryManager().thenReturn(memManager)
    	
    	self.swapOutRoutine.run(irq)
    	
    	verify(memManager,times(1)).addIntructionsForTheDisc() 