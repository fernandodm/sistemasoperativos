class Irq():
    def __init__(self, aPcbOrName, aType, aPid):
        #para tipo new esto va a ser un nombre
        self.pcbOrName = aPcbOrName
        self.type = aType
        #el pid solo lo va a precisar el tipo new
        self.pid = aPid

    def getPid(self):
        return self.pid

    def getPcb(self):
        return self.pcb

    def getName(self):
        return self.pcb

    def getType(self):
        return self.type
