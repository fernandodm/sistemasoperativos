class MemoryManager:

	def __init__(self, aLogicalMemory):
		self.logicalMemory = aLogicalMemory

	def compact(self):
		return 0

	def getInstruction(self, aPid, aDisplazament):
		return self.logicalMemory.getInstruction(aPid,aDisplazament)

	def putData(self, aPid, instructionsList):
		pass

	def deleteDataForPcb(self, aPcb):
		self.logicalMemory.deleteTakenBlock(aPcb.getPid())
