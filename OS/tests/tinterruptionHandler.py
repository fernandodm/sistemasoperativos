from mockito import *

import os, sys, threading, time

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
            self.aPcb = Mock()
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
            self.aHandler.eventQueue.append(self.aPcb)
            assert (self.aHandler.popEvent()== self.aPcb)
            assert (len(self.aHandler.eventQueue)==0)

        def test_newIrq(self):
            self.aHandler.newIrq("aPcbName")
            assert(self.aHandler.eventQueue[0].pcbOrName == "aPcbName")
            assert(self.aHandler.eventQueue[0].type == Interruption.NEW)
            assert(self.aHandler.pid == 1)

        def test_toWait(self):
            self.aHandler.toWait(self.aPcb)
            assert(self.aHandler.eventQueue[0].pcbOrName == self.aPcb)
            assert(self.aHandler.eventQueue[0].type == Interruption.TIMEOUT)

        def test_toKill(self):
            self.aHandler.toKill(self.aPcb)
            assert(self.aHandler.eventQueue[0].pcbOrName == self.aPcb)
            assert(self.aHandler.eventQueue[0].type == Interruption.KILL)

        def test_toIOInput(self):
            self.aHandler.toIOInput(self.aPcb)
            assert(self.aHandler.eventQueue[0].pcbOrName == self.aPcb)
            assert(self.aHandler.eventQueue[0].type == Interruption.IOINPUT) 

        def test_toIOOutput(self):
            self.aHandler.toIOOutput(self.aPcb)
            assert(self.aHandler.eventQueue[0].pcbOrName == self.aPcb)
            assert(self.aHandler.eventQueue[0].type == Interruption.IOOUTPUT) 

        
        def test_run(self):
            self.aHandler.interruptionProcessor = Mock()
            self.aHandler.run()
            verify(self.aSem,times(1)).acquire()
            verify(self.aHandler.interruptionProcessor,times(1)).execute();
            verify(self.aSem,times(1)).release()


