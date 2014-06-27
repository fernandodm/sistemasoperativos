from interruption import Interruption
from mainmemory import MainMemory
from scheduler import Scheduler
from disc import Disc
from interruptionHandler import InterruptionHandler
from cpu import Cpu
from clock import Clock
from logicalMemory import LogicalMemory
from continuousAssignment import ContinuousAssignment

class Kernel:
    def __init__(self, aIO, aSem, aSize):
        self.disc = Disc()
        self.memory = MainMemory(aSize)
        self.memoryManager = ContinuousAssignment(LogicalMemory(self.memory))
        self.scheduler = Scheduler()
        self.handler = InterruptionHandler(aSem,self)
        self.cpu = Cpu(self.memory,self.handler, aSem)
        self.IO = aIO
        self.clock = Clock()

    def getLogicalMemory(self):
        return self.logicalMemory

    def getMemoryManager(self):
        return self.memoryManager

    def getDisc(self):
        return self.disc

    def getCpu(self):
        return self.cpu
    
    def getMemory(self):
        return self.memory

    def getHandler(self):
        return self.handler

    def getIO(self):
        return self.IO

    def getClock(self):
        return self.clock

    def getScheduler(self):
        return self.scheduler

    def startUp(self):
        self.getCpu().start()
        self.getClock().start()
        

    def run(self, name):
        self.handler.newIrq(name)
        
    def getProgramasDelDisco(self, name):
        return self.getDisc().getProgram(name)
