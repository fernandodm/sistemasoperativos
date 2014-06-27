class FirstSetting():

	#Devuelve la primer celda libre con tamano dado
	def getFreeCellWithSize(self,freeBlocks,size):

		for block in freeBlocks:
			if(block.getSize() >= size):
				return block.getBase()

		return None
