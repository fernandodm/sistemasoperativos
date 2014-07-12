class Instruction():

	def __init__(self, aMsj, boolIo, boolFinal):
		self.content = aMsj
		self.isIo = boolIo
		self.isFinal = boolFinal

	def isIOInstruction(self):
		return self.isIo

	def isFinal(self):
		return self.isFinal

	def execute(self):
		print("[Intruccion] "+ str(self.content))
		return self.isFinal
