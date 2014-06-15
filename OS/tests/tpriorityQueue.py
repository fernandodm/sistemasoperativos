from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from priorityQueue import PriorityQueue
from pcb import Pcb
from chance import Chance
import unittest

class PriorityQueueTest(unittest.TestCase):

    def setUp(self):
        self.priority = PriorityQueue(3,5)
        self.aPcb1 = Mock()
        when(self.aPcb1).getPriority().thenReturn(2)
        self.aPcb2 = Mock()
        when(self.aPcb2).getPriority().thenReturn(2)

    def test_addPcb_initialAdd(self):
        self.priority.addPcb(self.aPcb1)
        chance = self.priority.table.get(6)
        assert (chance.elementos[0] == self.aPcb1)

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

    def test_cleanChances(self):
        chan1 = Chance()
        chan2 = Chance()
        chan3 = Chance()
        aPcb = Mock()
        chan2.elementos = [aPcb]
        self.priority.table = {1:chan1,2:chan2,3:chan3}
        assert(self.priority.table[1] == chan1)
        assert(self.priority.table[2] == chan2)
        assert(self.priority.table[3] == chan3)
        assert(len(self.priority.table) == 3)
        self.priority.cleanChances()
        assert(len(self.priority.table) == 1)
        assert(self.priority.table[2] == chan2)
