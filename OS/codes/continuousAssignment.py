from memoryManager import MemoryManager
from firstsetting import FirstSetting
from block import Block

class ContinuousAssignment(MemoryManager):

	def __init__(self, aLogicalMemory):
		MemoryManager.__init__(self,aLogicalMemory)
		self.setting = FirstSetting()

	def putData(self, pid, instructionsList):
		cell = self.setting.getFreeCellWithSize(self.logicalMemory.getFreeBlocks(), len(instructionsList))
		self.logicalMemory.putData(pid, cell, instructionsList)
