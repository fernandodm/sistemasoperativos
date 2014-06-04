from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from disc import Disc
import unittest

class DiscTest(unittest.TestCase):

    def setUp(self):
        self.disc = Disc()
        self.prog = Mock()
        self.prog2 = Mock()
        when(self.prog).getName().thenReturn("Programa1")
        when(self.prog2).getName().thenReturn("Programa2")

    def test_getCellsEmpty(self):
        assert self.disc.getCells() == []

    def test_getCellsWithElements(self):
        self.disc.cells = [self.prog]
        assert self.disc.getCells() == [self.prog]

    def test_addProgram(self):
        self.disc.addProgram(self.prog)
        assert self.disc.cells == [self.prog]

    def test_getProgram(self):
        self.disc.cells = [self.prog,self.prog2]
        assert self.disc.getProgram("Programa2") == self.prog2

suite = unittest.TestLoader().loadTestsFromTestCase(DiscTest)
unittest.TextTestRunner(verbosity=2).run(suite)    
