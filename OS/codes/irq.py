class Irq():
    def __init__(self, aPcb, aType, aPid):
        #para tipo new esto va a ser un nombre
        self.pcb = aPcb
        self.type = aType
        #el pid solo lo va a precisar el tipo new
        self.pid = aPid

    def getPcb(self):
        return self.pcb

    def getType(self):
        return self.type
