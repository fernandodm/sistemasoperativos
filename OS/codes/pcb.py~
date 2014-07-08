from status import Status

class Pcb():
    def __init__(self, aPid, aSize, aPriority):
        self.pid = aPid
        self.displacement = 0
        self.size = aSize
        self.status = Status.NEW
        self.priority = aPriority

    def getSize(self):
        return self.size    

    def pasarAReady(self):
        self.status = Status.READY

    def toExit(self):
        self.status = Status.EXIT

    def pcIncrease(self):
        self.displacement = self.displacement + 1

    def getPriority(self):
        return self.priority
