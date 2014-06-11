from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from priorityQueue import PriorityQueue
from pcb import Pcb
import unittest

class PriorityQueueTest(unittest.TestCase):

    def setUp(self):
        self.priority = PriorityQueue()
        self.aPcb1 = Mock()
        when(self.aPcb1).getPriority().thenReturn(2)
        self.aPcb2 = Mock()
        when(self.aPcb2).getPriority().thenReturn(2)

    #prueba del caso que no hay pcb
    def test_addPcb_initialAdd(self):
        self.priority.addPcb(self.aPcb1)
        chance = self.priority.table.get(6)
        assert (chance.elementos[0] == self.aPcb1)

    #prueba del caso que exista un pcb de la misma prioridad
    def test_addPcb_withPcb(self):
        self.priority.addPcb(self.aPcb1)
        self.priority.addPcb(self.aPcb2)
        chance = self.priority.table.get(6)
        assert (chance.elementos[0] == self.aPcb2)
        assert (chance.elementos[1] == self.aPcb1)
        
    def test_getMax(self):
        self.priority.addPcb(self.aPcb1)
        self.priority.addPcb(self.aPcb2)
        aPcb3 = Mock()
        when(aPcb3).getPriority().thenReturn(4)
        self.priority.addPcb(aPcb3)
        assert (self.priority.getMax() == aPcb3)
        assert (self.priority.getMax() == self.aPcb1)


suite = unittest.TestLoader().loadTestsFromTestCase(PriorityQueueTest)
unittest.TextTestRunner(verbosity=2).run(suite)    
