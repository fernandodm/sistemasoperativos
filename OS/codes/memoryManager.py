class MemoryManager:

	def __init__(self, aLogicalMemory, aKernel):
		self.logicalMemory = aLogicalMemory
		self.kernel = aKernel

	def compact(self):
		return 0

	def thereIsSpace(self,size):
		pass

	def getInstruction(self, aPid, aDisplazament):
		return self.logicalMemory.getInstruction(aPid,aDisplazament)

	def putDataCont(self, aPid, instructionsList):
		pass

	def putData(self, aPid, instructionsList):
		print "estoy en putData"
		if(self.thereIsSpace(len(instructionsList))):
			print "tengo espacio"
			self.putDataCont(aPid, instructionsList)
		else:
			print "no tngo espacio"
			#self.swapPcb(aPid,instructionsList)

	def deleteDataForPcb(self, aPcb):
		self.logicalMemory.deleteTakenBlock(aPcb.getPid())

	def swapPcb(self,aPid,instructionList):
		self.logicalMemory.freeBlock(len(instructionList),self.kernel)
		self.putData(aPid,instructionList)
		

