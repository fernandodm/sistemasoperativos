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

	def addIntructionsForTheDisc(self):
		pass

	#Agrega las instrucciones a memoria
	def putData(self, aPid, instructionsList):
		#Si hay espacio agrego las intrucciones a memoria
		if(self.thereIsSpace(len(instructionsList))):
			print "[MemoryManager] Hay espacio en memoria, agregando.."
			self.putDataCont(aPid, instructionsList)
			print "[MemoryManager] Se agrego a memoria, pid: " + str(aPid)
			return True
		else:
			#Si no hay espacio agrego en el handler un evento
			#de swapIn
			print "[MemoryManager] No hay espacio en memoria, swaping"
			handler = self.kernel.getHandler()
			handler.toSwapIn(aPid, instructionsList)
			pcb = self.kernel.getTable()[aPid]
			#Lo agrego a la cola de ready
			self.kernel.getScheduler().addPcb(pcb)
			return False

	def deleteDataForPcb(self, aPcb):
		self.logicalMemory.deleteTakenBlock(aPcb.getPid())

	def swapPcb(self,aPid,instructionList):
		self.logicalMemory.freeBlock(len(instructionList),self.kernel)
		self.putData(aPid,instructionList)
		

