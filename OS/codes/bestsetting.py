class BestSetting():

	#Devuelve la celda que tiene menos celdas libres consecutivamente y cumplen con el tamano pedido
	def getFreeCellWithSize(self,freeBlocks,size):

		best = None

		for block in freeBlocks:
			if(block.getSize() > size):
				if(best != None):
					if(best.size() >= block.size()):
						best = block
				else:
					best = block
			elif(block.getSize() == size):
				return block

		if(best != None):
			return best.getBase()
		else:
			return None