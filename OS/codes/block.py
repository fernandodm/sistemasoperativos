class Block():

	def __init__(self, aBase, aSize):
		self.base = aBase
		self.size = aSize
		self.free = True
		self.finish = aBase + aSize

	def getFinish(self):
		self.finish

	def getBase(self):
		return self.base

	def getSize(self):
		return self.size

	def isFree(self):
		return self.free

	def setBase(self, newBase):
		this.base = newBase

	def take(self):
		self.free = False