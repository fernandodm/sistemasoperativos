from status import Status

class Pcb():
    def __init__(self, aPid, aPc, aSize, aPriority):
        self.pid = aPid
        self.basePointer = aPc
        self.programCounter = aPc
        self.size = aSize
        self.status = Status.NEW
        self.priority = aPriority

    def getBasePointer(self):
        return self.basePointer

    def getSize(self):
        return self.size    

    def pasarAReady(self):
        self.status = Status.READY

    def toExit(self):
        self.status = Status.EXIT

    def pcIncrease(self):
        self.programCounter = self.programCounter + 1

    def getPriority(self):
        return self.priority
