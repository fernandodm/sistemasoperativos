class MainMemory():
    def __init__(self, aSize):
        self.cells = range(0,aSize)

    def getCells(self):
        return self.cells

    def getSize(self):
        return len(self.cells)

    #PRECOND: 
    #el numero cell no debe excederse del tamano de la memoria
    def putDataInCell(self,data,cell):
        #si la celda existe la suscribe
        self.cells[cell] = data

    #PRECOND: 
    #el numero cell no debe excederse del tamano de la memoria
    def getDataOfCell(self,cell):
        return self.cells[cell]