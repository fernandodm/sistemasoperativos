class LastSetting():

	def getFreeCellWithSize(self,cells,size):
		return self.getLastFreeCellWithSize(cells,size)

	def getLastFreeCellWithSize(self,cells,size):
		adress = (len(cells)-1)
		cont = 0
		clavesDadasVuelta = list(reversed(sorted(cells.keys())))
		for key in clavesDadasVuelta:
			if(cells[key] == None):
				cont += 1
				if(cont>=size):
					return adress+size-1
			else:
				cont = 0
			adress -= 1
		return None