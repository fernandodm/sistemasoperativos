from interruption import Interruption

class Kernel:
    def __init__(self, aCpu, aDisc, aMem, aHand, aQueue, aIO, aClock):
        self.disc = aDisc
        self.cpu = aCpu
        self.memory = aMem
        self.handler = aHand
        self.qReady = aQueue
        self.IO = aIO
        self.clock = aClock

    def getQReady(self):
        return self.qReady

    def getDisc(self):
        return self.disc

    def getCpu(self):
        return self.cpu
    
    def getMemory(self):
        return self.memory

    def getHandle(self):
        return self.handler

    def getIO(self):
        return self.IO

    def getClock(self):
        return self.clock

    def startUp(self):
        self.getCpu().start()
        self.getClock().start()
        

    def run(self, name):
        #QUE HACE
        

    def getProgramasDelDisco(self, name):
        return self.getDisc().getProgram(name)
