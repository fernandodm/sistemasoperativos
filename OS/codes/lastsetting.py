class LastSetting():

	def getFreeCellWithSize(self,cells,size):
		return self.getLastFreeCellWithSize(cells,size)

	def getLastFreeCellWithSize(self,cells,size):

		cont = 0

		clavesDadasVuelta = list(reversed(sorted(cells.keys())))

		for key in clavesDadasVuelta:

			if(cells[key] == None):
				cont += 1
				if(cont>=size and ((cells[key-1])!=None)):
					return (len(cells)-cont)


		return None