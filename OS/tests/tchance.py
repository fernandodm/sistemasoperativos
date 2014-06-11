from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from chance import Chance

import unittest

class ChanceTest(unittest.TestCase):

    def setUp(self):
        self.chance = Chance()
        

    def test_addPcb(self):
        aPcb = Mock()
        self.chance.addPcb(aPcb)
        assert (self.chance.elementos == [aPcb])

    def test_getMax(self):
        aPcb = Mock()
        otherPcb = Mock()
        self.chance.elementos = [aPcb,otherPcb]
        assert (self.chance.getMax() == otherPcb)

    def test_fusionarCon(self):
        aPcb = Mock()
        other = Mock()
        otherP = Mock()
        otraChance = Chance()
        aPbc2 = Mock()
        other3 = Mock()
        otherP4 = Mock()
        self.chance.elementos = [aPcb,other,otherP]
        otraChance.elementos = [aPbc2,other3,otherP4]
        self.chance.fusionarCon(otraChance)
        assert(self.chance.elementos == [aPcb,other,otherP,aPbc2,other3,otherP4])

    def test_isEmpty_withElements(self):
        self.chance.elementos = [Mock(), Mock()]
        assert (not self.chance.isEmpty())

    def test_isEmpty_whithOutElements(self):
        assert (self.chance.isEmpty())


suite = unittest.TestLoader().loadTestsFromTestCase(ChanceTest)
unittest.TextTestRunner(verbosity=2).run(suite) 