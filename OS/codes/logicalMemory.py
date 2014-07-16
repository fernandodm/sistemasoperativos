from block import Block

class LogicalMemory():

	def __init__(self, aMemory):
		self.freeBlocks = []
		self.takenBlocks = {}
		self.mainMemory = aMemory
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
		print self.takenBlocks

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
			print "entre al for del freeBlock en LogicalMemory"
			currentOld = table[pid].getOld()
			currentPid = pid
			if(old == None):
				old = currentOld
				aPid = currentPid
			else:
				if(old < currentOld or aKernel.getCpu().currentPcb.pid == aPid):
					old = currentOld
					aPid = currentPid

		self.savePcbToDisc(aPid, aKernel)
		self.removeDataPcb(aPid, aKernel, table)
		
	#Borra los datos del pcb
	def removeDataPcb(self, aPid, aKernel, aTable):
		self.deleteTakenBlock(aPid)
		del aTable[aPid]
		print "borre el pcb de la tabla"
		aKernel.getScheduler().removePid(aPid)

	#guarda las instrucciones del pcb al disco
	def savePcbToDisc(self, aPid, aKernel):
		instructions = []
		block = self.getTakenBlocks()[aPid]
		for cellInstr in range(block.getBase(),block.getFinish()):
			instructions.append(aKernel.getMemory().getDataOfCell(cellInstr))
		aKernel.getDisc().saveIntructions(aPid,instructions)