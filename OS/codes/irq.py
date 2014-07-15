class Irq():
    def __init__(self, aDataPcb, aType, aPid):
        #para tipo new esto va a ser un nombre
        self.dataPcb = aDataPcb
        self.type = aType
        #el pid solo lo va a precisar el tipo new
        self.pid = aPid

    def getPid(self):
        return self.pid

    def getPcb(self):
        return self.dataPcb

    def getName(self):
        return self.dataPcb

    def getInstructions(self):
        return self.dataPcb

    def getType(self):
        return self.type
