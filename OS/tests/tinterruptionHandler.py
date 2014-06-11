from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from interruptionHandler import InterruptionHandler
from kernel import Kernel
from irq import Irq
from interruption import Interruption
import unittest

class InterruptionHandlerTest(unittest.TestCase):

        def setUp(self):
            self.aSem = Mock()
            #self.iO = Mock()
            #self.aKernel = Kernel(self.iO,self.aSem)
            self.aKernel = Mock()
            self.aHandler = InterruptionHandler(self.aSem, self.aKernel)

        def test_handler(self):
            irq = Irq("name",0,15)
            self.aHandler.eventQueue = Mock()
            self.aHandler.handler(irq)
            verify(self.aSem,times(1)).acquire()
            verify(self.aHandler.eventQueue,times(1)).append(irq)
            verify(self.aSem,times(1)).release()

        def test_isNotEmpty_withElements(self):
            self.aHandler.eventQueue.append(Mock())
            assert(self.aHandler.isNotEmpty())

        def test_isNotEmpty_withoutElements(self):
            assert(not self.aHandler.isNotEmpty())

        def test_popEvent(self):
            aPcb = Mock()
            self.aHandler.eventQueue.append(aPcb)
            assert (self.aHandler.popEvent()== aPcb)
            assert (len(self.aHandler.eventQueue)==0)

        def test_newIrq(self):
            self.aHandler.newIrq("cross")
            assert(self.aHandler.eventQueue[0].pcbOrName == "cross")
            assert(self.aHandler.eventQueue[0].type == Interruption.NEW)
            assert(self.aHandler.pid == 1)

        def test_toWait(self):
            self.aHandler.toWait("waiting")
            assert(self.aHandler.eventQueue[0].pcbOrName == "waiting")
            assert(self.aHandler.eventQueue[0].type == Interruption.READY)

        def test_toKill(self):
            self.aHandler.toKill("kill")
            assert(self.aHandler.eventQueue[0].pcbOrName == "kill")
            assert(self.aHandler.eventQueue[0].type == Interruption.KILL)

        def test_toIOInput(self):
            self.aHandler.toIOInput("input")
            assert(self.aHandler.eventQueue[0].pcbOrName == "input")
            assert(self.aHandler.eventQueue[0].type == Interruption.IOINPUT) 

        def test_toIOOutput(self):
            self.aHandler.toIOOUTPUT("output")
            assert(self.aHandler.eventQueue[0].pcbOrName == "output")
            assert(self.aHandler.eventQueue[0].type == Interruption.IOOUTPUT) 

        
        def test_run(self):
            self.run()
            verify(self.aHandler.semaphore,times(1)).acquire()
            verify(self.aHandler.interruptionProcessor,times(1)).execute()
            verify(self.aHandler.semaphore,times(1)).release()

        
suite = unittest.TestLoader().loadTestsFromTestCase(InterruptionHandlerTest)
unittest.TextTestRunner(verbosity=2).run(suite)    
