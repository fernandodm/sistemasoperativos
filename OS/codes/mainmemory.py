class MainMemory():
    def __init__(self):
        self.cells = []

    def getCells(self):
        return self.cells


    def putDateInCell(self,date,cell):
        #aca se pregunta para saber si la celda existe
        #de ser asi la suscribe
        if(len(self.cells) > cell):
            self.cells[cell] = date
            
        #en el caso de que se quiera insertar un dato en una posicion
        #mayor o igual a la longitud de la lista, entonces se insertara
        #el dato en la proxima celda vacia, ignorando la posicion indicada
        #en el argumento (de todos modos no deberia pasar)
        else:
            self.getCells().append(date)

    def deleteDatesForPcb(self,pcb):
        
        for currCell in range(pcb.basePointer,(pcb.basePointer+pcb.size)):
            self.cells[currCell] = None
            
    def getFirstFreeCellWithSize(self,size):
        #despues se cambia
        #celdas vacias se reemplazan por None
        return len(self.getCells())
