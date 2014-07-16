from block import Block

class LogicalMemory():

	def __init__(self, aMemory):
		self.freeBlocks = []
		self.takenBlocks = {}
		self.mainMemory = aMemory
		#Se genera un bloque libre
		self.allocFreeBlock(0,aMemory.getSize())

	def allocFreeBlock(self,aBase,aSize):
		newBlock = Block(aBase,aSize)
		if(len(self.getFreeBlocks())==0):
			self.freeBlocks.append(newBlock)
		else:
			for block in self.getFreeBlocks():
				if(block.getBase() == (aBase+aSize)):
					block.fusion(newBlock)
				elif(block.getFinish() == aBase):
					newBlock.fusion(block)
					adressOfBlock = self.freeBlocks.index(block)
					self.freeBlocks[adressOfBlock] = newBlock

	#PRECOND:
	#El alocamiento de bloques no maneja colisiones
	#eso se debe controlar desde el manejador
	def allocTakenBlock(self,aPid,aBase,aSize):
		newBlock = Block(aBase,aSize)
		self.getTakenBlocks()[aPid] = newBlock

	#PRECOND:
	#el bloque a borrar debe existir
	def deleteTakenBlock(self,aPid):
		block = self.getTakenBlocks()[aPid]
		self.allocFreeBlock(block.getBase(),block.getSize())
		del self.getTakenBlocks()[aPid]

	#PRECOND:
	#Se le pasa una base que acierte con un bloque libre y que entre el tamano en dicho bloque
	#eso se debe controlar desde el manejador
	#Se debe usar este metodo sii voy a asignar un bloque usado posteriormente, caso contrario
	#se pierde un bloque de memoria libre o parte de ella
	def deleteFreeBlockFor(self, aBase, aSize):
		for freeBlock in self.getFreeBlocks():
			cont = 0
			if(freeBlock.getBase() == aBase):
				if(freeBlock.getBase() == aBase & freeBlock.getSize() == aSize):
					del self.getFreeBlocks()[cont]
				else:
					newBlock = Block((aBase+aSize),(freeBlock.getFinish()-(aBase+aSize)))
					self.getFreeBlocks()[cont] = newBlock
				break
			cont += 1

	def putData(self, pid, base, instructionList):
		size = len(instructionList)
		self.deleteFreeBlockFor(base,size)
		self.allocTakenBlock(pid, base, size)
		self.putDataInPhysicalMemory(base,instructionList)
		print "[LogicalMemory] Se agrego el bloque: (pid " + str(pid) + ", base " + str(base) + ", size " + str(size) +")"

	def putDataInPhysicalMemory(self, base, instructionList):
		cell = base

		for instr in instructionList:
			self.mainMemory.putDataInCell(instr,cell)
			cell += 1

	def getInstruction(self,aPid,aDisplazament):
		block = self.getTakenBlocks()[aPid]
		adress = block.getBase()+aDisplazament
		return self.mainMemory.getDataOfCell(adress)
			

	def getFreeBlocks(self):
		return self.freeBlocks

	def getTakenBlocks(self):
		return self.takenBlocks

	#Libera el bloque del pcb menos recientemente utilizado
	#para que pueda ser reemplazado por el nuevo
	def freeBlock(self, aSize,aKernel):
		old = None
		aPid = None
		table = aKernel.getTable()
		for pid in list(table.keys()):
			currentOld = table[pid].getOld()
			currentPid = pid
			if(old == None):
				old = currentOld
				aPid = currentPid
			else:
				if(old < currentOld or aKernel.getCpu().currentPcb.pid == aPid):
					old = currentOld
					aPid = currentPid
		pcb = aKernel.getTable()[aPid]
		self.savePcbToDisc(pcb, aKernel)
		print "[LogicalMemory] Se guardo el proceso con id " + str(pcb.getPid()) + " al disco"
		self.removeDataPcb(aPid, aKernel, table)
		print "[LogicalMemory] Se elimino de memoria"
		
	#Borra los datos del pcb
	def removeDataPcb(self, aPid, aKernel, aTable):
		#Borra el cloque usado que pertenece al pid
		self.deleteTakenBlock(aPid) 
		#Borra de la tabla del kernel el pcb
		del aTable[aPid]
		#Borra de la cola de ready el pcb
		aKernel.getScheduler().removePid(aPid)

	#Guarda las instrucciones del pcb al disco
	def savePcbToDisc(self, aPcb, aKernel):
		instructions = []
		#Obtengo el bloque al que pertenece el pcb
		block = self.getTakenBlocks()[aPcb.getPid()]
		#Agrego las isntrucciones del pcb en la variable instructions
		for cellInstr in range(block.getBase(),block.getFinish()):
			instructions.append(aKernel.getMemory().getDataOfCell(cellInstr))
		#Finalmente guardo el pcb y las instrucciones al disco
		aKernel.getDisc().saveIntructions(aPcb,instructions)