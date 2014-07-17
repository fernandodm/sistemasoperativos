from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from instruction import Instruction

import unittest

class InstructionTest(unittest.TestCase):

	def setUp(self):
		self.instruction = Instruction("instruction inicial",False,False)
		self.instructionFinal = Instruction("instruction final y de io",True,True)

	def test_execute_noFinal(self):
		assert not self.instruction.execute()

	def test_execute_final(self):
		assert self.instructionFinal.execute()