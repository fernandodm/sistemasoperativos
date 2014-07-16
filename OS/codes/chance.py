class Chance():
    def __init__(self):
        self.elementos = []

    def addPcb(self,aPcb):
        self.elementos.insert(0,aPcb)

    def getMax(self):
        return self.elementos.pop()

    def fusionarCon(self,otraChance):
        if(otraChance == None):
            return otraChance
        self.elementos = self.elementos + otraChance.elementos
        return self

    def isEmpty(self):
        return len(self.elementos) == 0

    def ifAppearDelete(self, pid):
        for nro in range(len(self.elementos)):
            if(self.elementos[nro].getPid() == pid):
                del self.elementos[nro]
                return True
        return False
