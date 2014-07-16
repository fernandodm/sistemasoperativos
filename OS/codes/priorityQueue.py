from chance import Chance

class PriorityQueue():
    def __init__(self, cantChances, cantPriority):
        self.table = {}
        self.chances = cantChances
        self.priority = cantPriority

    def addPcb(self,aPcb):
        adress = aPcb.getPriority() * self.chances
        if(self.table.get(adress) == None):
            ch = Chance()
            ch.addPcb(aPcb)
            self.table[adress] = ch
        else:
            self.table.get(adress).addPcb(aPcb)

    def size(self):
        return len(self.table)

    def isEmpty(self):
        self.cleanChances()
        return self.size() == 0

    def getMax(self):

        self.cleanChances()
        if(len(self.table)>0):
            tabla = self.table
            clavesDadasVuelta = list(reversed(sorted(tabla.keys())))
            ultimaChance = tabla.get(clavesDadasVuelta[0])
            
            nroUltimaChance = (self.chances * self.priority) - 1

            for i in clavesDadasVuelta:
                if(i != nroUltimaChance):
                    if(i == nroUltimaChance - 1):
                        tabla[i+1] = tabla.get(i).fusionarCon(tabla.get(i+1))

                    else:
                        tabla[i+1] = tabla.get(i)

                    tabla.pop(i)

            return ultimaChance.getMax()
        else:
            return None
                    
        
    def cleanChances(self):
        tam = self.table.keys()
        for i in tam:
            chance = self.table[i]
            if(chance.isEmpty()):
                del self.table[i]
                
    def removePid(self, aPid):

        tabla = self.table
        claves = list(tabla.keys())

        for clave in claves:
            if(tabla[clave].ifAppearDelete(aPid)):
                break
    
