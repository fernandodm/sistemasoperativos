from chance import Chance

class PriorityQueue():
    def __init__(self):
        self.table = {}
        self.chances = 3

    def addPcb(self,aPcb):
        adress = aPcb.getPriority() * self.chances
        if(self.table.get(adress) == None):
            ch = Chance()
            ch.addPcb(aPcb)
            self.table[adress] = ch
        else:
            self.table.get(adress).addPcb(aPcb)

    def getMax(self):

        self.cleanChances()
        tabla = self.table
        clavesDadasVuelta = list(reversed(sorted(tabla.keys())))
        ultimaChance = tabla.get(clavesDadasVuelta[0])
        
        for i in clavesDadasVuelta:
            if(i != 14):
                if(i == 13):
                    tabla[i+1] = tabla.get(i).fusionarCon(tabla.get(i+1))

                else:
                    tabla[i+1] = tabla.get(i)

                tabla.pop(i)

        return ultimaChance.getMax()
                    
        
    def cleanChances(self):
        tam = self.table.keys()
        for i in tam:
            chance = self.table[i]
            if(chance.isEmpty()):
                del self.table[i]
                
    
