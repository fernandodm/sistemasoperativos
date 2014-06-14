from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from interruptionprocessor import InterruptionProcessor
from interruptionHandler import InterruptionHandler
from kernel import Kernel
from irq import Irq
from interruption import Interruption
import unittest

class InterruptionProcessorTest(unittest.TestCase):

        def setUp(self):
            
            self.aHandler = InterruptionHandler(Mock(),Mock())
            self.aRoutines = Mock()
            self.aProcessor = self.aHandler.interruptionProcessor
            self.aProcessor.routines = self.aRoutines
            
        def test_execute_emptyHandler(self):
            when(self.aHandler).isNotEmpty().thenReturn(False)
            self.aProcessor.execute()
            verify(self.aHandler,times(0)).popEvent()

        def test_execute_NotEmptyHandler(self):
            event = Mock()
            self.aProcessor.handler.eventQueue.append(event)
            self.aProcessor.handler.eventQueue.append(event)
            self.aProcessor.handler.eventQueue.append(event)
            self.aProcessor.execute()
            verify(self.aProcessor.routines,times(3)).execute(event)
            
               
suite = unittest.TestLoader().loadTestsFromTestCase(InterruptionProcessorTest)
unittest.TextTestRunner(verbosity=2).run(suite)    

