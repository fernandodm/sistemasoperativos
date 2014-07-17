from mockito import *

import os, sys

def _rel2abspath(fname):
    appdir=os.path.abspath(os.path.dirname(sys.argv[0]))
    return os.path.join(appdir,fname)

sys.path.insert(0,_rel2abspath("../codes"))

from continuousAssignment import ContinuousAssignment

import unittest

class ContinuousAssignmentTest(unittest.TestCase):

	def setUp(self):
		self.logical = Mock()
		self.kernel = Mock()
		self.cont = ContinuousAssignment(self.logical,self.kernel)
		self.cont.setting  = Mock()
		
		self.block1 = Mock()
		self.block2 = Mock()
		self.block3 = Mock()

		self.freeBlocks = [self.block1,self.block2,self.block3]

	def test_putDataCont(self):

		when(self.logical).getFreeBlocks().thenReturn(self.freeBlocks)
		when(self.cont.setting).getFreeCellWithSize(self.freeBlocks,3).thenReturn(20)

		instructionsList = ["instruction1","instruction2","instruction3"]

		self.cont.putDataCont(23,instructionsList)

		verify(self.logical, times(1)).putData(23,20,instructionsList)


	def test_thereIsSpace_withSpace(self):

		when(self.block1).getSize().thenReturn(3)

		when(self.block2).getSize().thenReturn(4)

		when(self.block3).getSize().thenReturn(3)

		when(self.logical).getFreeBlocks().thenReturn(self.freeBlocks)

		assert self.cont.thereIsSpace(4)

	def test_thereIsSpace_withOutSpace(self):

		when(self.block1).getSize().thenReturn(3)

		when(self.block2).getSize().thenReturn(2)

		when(self.block3).getSize().thenReturn(3)

		when(self.logical).getFreeBlocks().thenReturn(self.freeBlocks)

		assert not self.cont.thereIsSpace(9)

	def addIntructionsForTheDisc(self):
		#Obtnego la tabla de de instrucciones
		pcb1 = Mock()
		pcb2 = Mock()
		pcb3 = Mock()

		when(pcb3).getPid().thenReturn(3)

		instructions = {pcb1: ["instruction1","instruction2","instruction3"],
					    pcb2: ["instruction1","instruction2","instruction3"],
					    pcb3: ["instruction1","instruction2"]}

		disc = Mock()
		sch = Mock() 

		when(self.kernel).getDisc().thenReturn(disc)
		when(disc).getInstructions().thenReturn(instructions)

		when(self.cont).thereIsSpace(2).thenReturn(True)
		when(self.cont).thereIsSpace(3).thenReturn(False)

		when(self.kernel).getScheduler().thenReturn(sch)

		verify(sch,times(1)).addPcb(pcb3)
		verify(self.cont,times(1)).putData(pcb3.getPid(),instructions)
