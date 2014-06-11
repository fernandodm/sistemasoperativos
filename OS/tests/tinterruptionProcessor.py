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
            
            self.aHandler = Mock()
            self.aKernel = Mock()
            self.aRoutines = Mock()
            self.aProcessor = InterruptionProcessor(aHandler, aKernel)
            self.aProcessor.routines = aRoutines
            
        def test_execute_emptyHandler(self):
            self.aProcessor.execute()
            when(self.aHandler).isNotEmpty().thenReturn(False)
            verify(self.aHandler,times(0)).popEvent()

        def test_execute_NotEmptyHandler(self):
            self.aProcessor.execute()
            self.event = Mock()
            when(self.aHandler).isNotEmpty().thenReturn(True)
            when(self.aHandler).popEvent().thenReturn(self.event)
            verify(self.aHandler,times(1)).popEvent()
            verify(self.aProcessor.routines,times(1)).execute(self.event)
            
               
suite = unittest.TestLoader().loadTestsFromTestCase(InterruptionProcessorTest)
unittest.TextTestRunner(verbosity=2).run(suite)    

