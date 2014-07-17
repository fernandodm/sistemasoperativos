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