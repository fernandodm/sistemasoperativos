class MainMemory():
    def __init__(self):
        self.cells = {}

    def getCells(self):
        return self.cells


    def putDateInCell(self,date,cell):
        #si la celda existe la suscribe
        self.cells[cell] = date

    def deleteDatesForPcb(self,pcb):
        
        for currCell in range(pcb.getBasePointer(),(pcb.getBasePointer()+pcb.getSize())):
            self.cells[currCell] = None
            
    def getFirstFreeCellWithSize(self,size):
        #direccion de la celda actual
        adress = 0
        #acumulador de celdas vacias
        cont = 0
        #recorro por claves acumulando vacias en cont
        for key in self.getCells().keys():
            #si la celda esta vacia entonces..
            if(self.getCells()[key] == None):
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
        #entonces retorna la ultima posicion de memoria siendo esta implementacion dinamica
        return len(self.getCells())
