from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from interruptionHandler import InterruptionHandler
from kernel import Kernel
from irq import Irq
import unittest

class InterruptionHandlerTest(unittest.TestCase):

    def setUp(self):
    	self.aSem = Mock()
        self.iO = Mock()
    	self.aKernel = (self.iO,self.aSem)
        self.aHandler = InterruptionHandler(self.aSem, self.aKernel)

    def test_handler(self):
    	irq = Irq("name",0,15)
    	self.aHandler.handler(irq)
        verify(self.aSem,times(1)).acquire()
        verify(self.aHandler.eventQueue,times(1)).append(irq)
        verify(self.aSem,times(1)).release()

suite = unittest.TestLoader().loadTestsFromTestCase(InterruptionHandlerTest)
unittest.TextTestRunner(verbosity=2).run(suite)    