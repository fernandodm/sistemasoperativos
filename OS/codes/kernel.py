from interruption import Interruption
from mainmemory import MainMemory
from scheduler import Scheduler
from disc import Disc
from interruptionHandler import InterruptionHandler
from cpu import Cpu
from clock import Clock
from logicalMemory import LogicalMemory
from continuousAssignment import ContinuousAssignment
import io

class Kernel:
    def __init__(self, aSem, aSize):
        self.disc = Disc()
        self.memory = MainMemory(aSize)
        self.memoryManager = ContinuousAssignment(LogicalMemory(self.memory))
        self.handler = InterruptionHandler(aSem,self)
        self.cpu = Cpu(self.memoryManager,self.handler, aSem)
        self.scheduler = Scheduler(self.cpu)        
        self.clock = Clock()
        self.IO = io.IO(self,aSem)
        self.clock.addSuscribed(self.cpu)
        self.clock.addSuscribed(self.IO)
        self.clock.addSuscribed(self.handler)

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

    def getMemoryManager(self):
        return self.memoryManager

    def getHandler(self):
        return self.handler

    def getIO(self):
        return self.IO

    def getClock(self):
        return self.clock

    def getScheduler(self):
        return self.scheduler

    def startUp(self):
        self.getClock().startUp()
        
    def shutDown(self):
        self.getClock().shutDown()

    def run(self, name):
        self.handler.newIrq(name)
        
    def getProgramasDelDisco(self, name):
        return self.getDisc().getProgram(name)
