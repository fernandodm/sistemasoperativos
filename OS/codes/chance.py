class Chance():
    def __init__(self):
        self.elementos = []

    def addPcb(self,aPcb):
        self.elementos.append(aPcb)

    def getMax(self):
        return self.elementos.pop()

    def fusionarCon(self,otraChance):
        if(otraChance == None):
            return otraChance
        self.elementos = self.elementos + otraChance.elementos
        return self
