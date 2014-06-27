class BadWaySetting():

	#Devuelve la celda que tiene mas celdas libres consecutivamente
	def getFreeCellWithSize(self,freeBlocks,size):

		bad = None

		for block in freeBlocks:
			if(block.getSize() >= size):
				if(bad != None):
					if(bad.size() <= block.size()):
						bad = block
				else:
					bad = block

		if(best != None):
			return bad.getBase()
		else:
			return None