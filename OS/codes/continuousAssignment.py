from memoryManager import MemoryManager
from firstsetting import FirstSetting
from block import Block
from pcb import Pcb

class ContinuousAssignment(MemoryManager):

	def __init__(self, aLogicalMemory, aKernel):
		MemoryManager.__init__(self,aLogicalMemory, aKernel)
		self.setting = FirstSetting()

	def putDataCont(self, pid, instructionsList):
		cell = self.setting.getFreeCellWithSize(self.logicalMemory.getFreeBlocks(), len(instructionsList))
		self.logicalMemory.putData(pid, cell, instructionsList)

	def thereIsSpace(self, aSize):
		#si hay bloques libres
		freeBlocks = self.logicalMemory.getFreeBlocks()
		if(len(freeBlocks) > 0):
			#busco si hay un bloque con tamanho >= a aSize
			for block in freeBlocks:
				if(block.getSize() >= aSize):
					return True
		return False

	#Agrega instrucciones del disco a la memoria y
	#se vuelve a poner el pcb en la cola
	def addIntructionsForTheDisc(self):
		#Obtnego la tabla de de instrucciones 
		tableSwap = self.kernel.getDisc().getInstructions()
		pids = tableSwap.keys()
		#pid = pids[0]
		#Obtengo las instrucciones del proceso
		for pid in pids:
			instructions = tableSwap[pid]
			sizeInstructions = len(instructions)
			#si hay espacio vuelve a memoria
			if(self.thereIsSpace(sizeInstructions)):
				p = Pcb(pid, sizeInstructions,1)
				self.kernel.addPcb(p)
				p.pasarAReady()
				self.kernel.getScheduler().addPcb(p)
				self.putDataCont(pid, instructions)
				#elimino las isntrucciones del disco
				del self.kernel.getDisc().getInstructions()[pid]