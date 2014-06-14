from interruption import Interruption
from mainmemory import MainMemory
from scheduler import Scheduler
from disc import Disc
from interruptionHandler import InterruptionHandler
from cpu import Cpu
from clock import Clock

class Kernel:
    def __init__(self, aIO, aSem):
        self.disc = Disc()
        self.memory = MainMemory()
        self.scheduler = Scheduler()
        self.handler = InterruptionHandler(aSem,self)
        self.cpu = Cpu(self.memory,self.handler, aSem)
        self.IO = aIO
        self.clock = Clock()

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
        return 0
        
    def getProgramasDelDisco(self, name):
        return self.getDisc().getProgram(name)
