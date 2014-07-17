class Block():

	def __init__(self, aBase, aSize):
		self.base = aBase
		self.size = aSize
		self.free = True
		self.finish = aBase + aSize

	def getFinish(self):
		return self.finish

	def getBase(self):
		return self.base

	def getSize(self):
		return self.size

	def isFree(self):
		return self.free

	def setBase(self, newBase):
		self.base = newBase

	def take(self):
		self.free = False

	def fusion(self,otherBlock):
		self.size += otherBlock.getSize()
		self.finish = self.getBase()+self.getSize()

	def updateFinish(self):
		#Actualiza la direccion de la finalizacion del bloque
		self.finish = self.base + self.size

	def compact(self,blocks,index):
		#Si es el primer bloque lo ubico al principio de los bloques
		pids = list(blocks.keys())
		if(index == 0):
			self.base = 0
			self.updateFinish()
		# Si no lo es, los voy apilando "a la izquierda"
		else:
			newBase = blocks[pids[index-1]].getFinish()
			self.base = newBase
			self.updateFinish()