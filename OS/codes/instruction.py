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
		if(self.isIOInstruction()):
			print("[Intruccion] De IO "+ str(self.content))
		else:
			print("[Intruccion] De CPU "+ str(self.content))
		return self.isFinal
