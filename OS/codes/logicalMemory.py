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
		block = self.getFreeBlocks()[aPid]
		self.allocFreeBlock(block.getBase(),block.getSize())
		del self.getFreeBlocks()[aPid]

	#PRECOND:
	#Se le pasa una base que acierte con un bloque libre y que entre el tamano en dicho bloque
	#eso se debe controlar desde el manejador
	#Se debe usar este metodo sii voy a asignar un bloque usado posteriormente, caso contrario
	#se pierde un bloque de memoria libre o parte de ella
	def deleteFreeBlockFor(self, aBase, aSize):
		for freeBlock in self.getFreeBlocks():
			cont = 0
			if(freeBlock.getBase() == aBase):
				if(freeBlock.getBase() == aBase && freeBlock.getSize() == aSize):
					del self.getFreeBlocks()[cont]
				else:
					newBlock = Block((aBase+aSize+1),freeBlock.getFinish())
					self.getFreeBlocks()[cont] = newBlock
				break
			cont += 1


	def getFreeBlocks(self):
		return self.freeBlocks

	def getTakenBlocks(self):
		return self.takenBlocks