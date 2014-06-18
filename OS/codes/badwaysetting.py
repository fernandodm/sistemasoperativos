class BadWaySetting():

	def getFreeCellWithSize(self,cells,size):
		return self.getBadWayWithSize(cells,size)

	def getBadWayWithSize(self,cells,size):
		adressActual = 0
		adressMayor = 0

		contActual = 0
		contMayor = 0

		for key in cells.keys():

			if(cells[key] == None):

				contActual += 1
				if((contActual>=contMayor) and (contActual>=size)):
					contMayor = contActual
					adressMayor = adressActual
			else:
				contActual = 0
			adressActual += 1
		if(adressMayor != 0):
			return adressMayor-contMayor+1

		return None