from status import Status

class Pcb():
    def __init__(self, aPid, aPc, aSize):
        self.pid = aPid
        self.basePointer = aPc
        self.programCounter = aPc
        self.size = aSize
        self.status = Status.NEW

    def pasarAReady(self):
        self.status = Status.READY

    def toExit(self):
        self.status = Status.EXIT

    def pcIncrease(self):
        self.programCounter = self.programCounter + 1
