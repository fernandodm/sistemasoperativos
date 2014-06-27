class LogicalMemory():

	def __init__(self, aMemory,aMemoryManager):
		self.freeBlocks = []
		self.takenBlocks = []
		self.mainMemory = aMemory
		self.memoryManager = aMemoryManager
		self.memoryManager.initialize()


	def getMainMemory(self):
		return self.mainMemory


	def getTotalSize(self):
		#REALIZAR EL METODO GETSIZE EN MAINMEMORY JUANMA TIRA GENTE
		return self.mainMemory.getSize()