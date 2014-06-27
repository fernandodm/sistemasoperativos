from memoryManager import MemoryManager
from block import Block

class ContinuousAssignment(MemoryManager):

	def __init__(self, aLogicalMemory):
		MemoryManager.__init__(aLogicalMemory)
		self.setting = FirstSetting()

	def initialize(self):
		block = Block(0, self.logicalMemory.getTotalSize())
		#agrego un bloque libre
		self.logicalMemory.addFreeBlock(block)

	def addFreeBlock(self,aBlock):
		self.setting.addBlock(aBlock)