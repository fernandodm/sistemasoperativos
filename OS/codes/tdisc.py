from mockito import *
from disc import Disc
import unittest

class DiscTest(unittest.TestCase):

    def testGetCells(self):
        dis = Disc()
        assert (dis.getCells() == dis.cells)

    def testAddProgram(self):
        dis = Disc()
        pr = mock()
        pr2 = mock()
        pr3 = mock()
        dis.addProgram(pr)
        dis.addProgram(pr2)
        dis.addProgram(pr3)
        assert (dis.getCells()==[pr,pr2,pr3])

    def testGetProgram(self):
        dis = Disc()
        pr = mock()
        pr2 = mock()
        pr3 = mock()
        when(pr).getName().thenReturn("prog1")
        when(pr2).getName().thenReturn("prog2")
        when(pr3).getName().thenReturn("prog3")
        dis.addProgram(pr)
        dis.addProgram(pr2)
        dis.addProgram(pr3)
        assert (dis.getProgram("prog2")==pr2)

suite = unittest.TestLoader().loadTestsFromTestCase(DiscTest)
unittest.TextTestRunner(verbosity=2).run(suite)
