class BadWaySetting():

	#Devuelve la celda que tiene mas celdas libres consecutivamente
	def getFreeCellWithSize(self,freeBlocks,size):

		bad = None

		for block in freeBlocks:
			if(block.getSize() >= size):
				if(bad != None):
					if(bad.getSize() < block.getSize()):
						bad = block
				else:
					bad = block

		if(bad != None):
			return bad.getBase()
		else:
			return None
