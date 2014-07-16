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

	#Devuelve True si hay espacio en memoria
	def thereIsSpace(self, aSize):
		cont = 0
		freeBlocks = self.logicalMemory.getFreeBlocks()
		#Si hay bloques libres
		if(len(freeBlocks) > 0):
			#Sumo el tamanho total de los bloques libres
			for block in freeBlocks:
				cont += block.getSize()

		if(cont >= aSize):
			return True
		return False

	#Agrega instrucciones del disco a la memoria y
	#se vuelve a poner el pcb en la cola
	def addIntructionsForTheDisc(self):
		#Obtnego la tabla de de instrucciones 
		tableSwap = self.kernel.getDisc().getInstructions()
		listPcb = tableSwap.keys()
		#Obtengo las instrucciones del proceso
		for pcb in listPcb:
			instructions = tableSwap[pcb]
			sizeInstructions = len(instructions)
			#si hay espacio vuelve a memoria
			if(self.thereIsSpace(sizeInstructions)):
				print "[ContinuousAssignment] Agregando instrucciones del disco"
				self.kernel.getScheduler().addPcb(pcb)
				self.putData(pcb.getPid(), instructions)
				#elimino las isntrucciones del disco
				del self.kernel.getDisc().getInstructions()[pcb]
				print "[ContinuousAssignment] Se elimino el proceso " + str(pcb.getPid()) + " del disco"