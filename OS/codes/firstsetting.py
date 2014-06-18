class FirstSetting():

	def getFreeCellWithSize(self,cells,size):
		return self.getFirstFreeCellWithSize(cells,size)

	def getFirstFreeCellWithSize(self,cells,size):
		#direccion de la celda actual
		adress = 0
		#acumulador de celdas vacias
		cont = 0
		#recorro por claves acumulando vacias en cont
		for key in cells.keys():
			#si la celda esta vacia entonces..
			if(cells[key] == None):
				#sumo una celda de espacio libre
				cont += 1
				#si el espacio libre es el que necesito entonces..
				if(cont>=size):
					#retorno la posicion de esa celda restado el tamano requerido
					#para retornar la direccion de la primer celda libre
					return adress-size+1 #+1 porque se cuenta el cero
			#si la celda no esta vacia entonces..
			else:
				#seteo el contador el cero para volver a contar
				cont = 0
			#por ultimo sumo a la direccion siguiente
			adress += 1
		#si no se encontro un slot consecutivo de celdas vacias con el tamano requerido
		#entonces retorna None
		return None	