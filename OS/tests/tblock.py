from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from block import Block

import unittest

class BlockTest(unittest.TestCase):

    def setUp(self):
        self.block = Block(1,4)

    def getBase(self):
        assert(self.block.getBase() == 1)


    def test_getFinish(self):
        assert(self.block.getFinish() == 5)

    def test_getSize(self):
        assert(self.block.getSize() == 4)

    def test_isFree(self):
        assert(self.block.isFree())

    def test_setBase(self):
        self.block.setBase(5)
        assert(self.block.getBase() == 5)

    def test_take(self):
        self.block.take()
        assert(not self.block.isFree())

    def test_fusion(self):
        block2 = Block(5, 3)
        self.block.fusion(block2)
        assert(self.block.getSize() == 7)
        assert(self.block.getFinish() == 8)