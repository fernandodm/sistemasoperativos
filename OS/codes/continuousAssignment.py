from memoryManager import MemoryManager
from firstsetting import FirstSetting
from block import Block

class ContinuousAssignment(MemoryManager):

	def __init__(self, aLogicalMemory, aKernel):
		MemoryManager.__init__(self,aLogicalMemory, aKernel)
		self.setting = FirstSetting()

	def putDataCont(self, pid, instructionsList):
		cell = self.setting.getFreeCellWithSize(self.logicalMemory.getFreeBlocks(), len(instructionsList))
		self.logicalMemory.putData(pid, cell, instructionsList)

	def thereIsSpace(self, aSize):
		#si hay bloques libres
		freeBlocks = self.logicalMemory.getFreeBlocks()
		if(len(freeBlocks) > 0):
			#busco si hay un bloque con tamanho >= a aSize
			for block in freeBlocks:
				if(block.getSize() >= aSize):
					print("taaaaaammmm"+str(block.getSize()))
					return True
		return False
