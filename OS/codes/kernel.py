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
    def __init__(self, aSize):
        self.disc = Disc()
        self.memory = MainMemory(aSize)
        self.memoryManager = ContinuousAssignment(LogicalMemory(self.memory),self)
        self.handler = InterruptionHandler(self)
        self.cpu = Cpu(self.memoryManager,self.handler)
        self.scheduler = Scheduler(self.cpu)        
        self.clock = Clock()
        self.IO = io.IO(self)
        self.clock.addSuscribed(self.cpu)
        self.clock.addSuscribed(self.IO)
        self.clock.addSuscribed(self.handler)
        #tabla que contiene todos los pcb (k,v) => (pid,pcb)
        self.table = {}

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

    def getTable(self):
        return self.table

    #Comienza con la ejecucion del clock
    def startUp(self):
        self.getClock().startUp()

    #Corta la ejecucion del clock
    def shutDown(self):
        self.getClock().shutDown()

    def run(self, name):
        print "[Kernel] Ejecutar programa: " + str(name)
        self.handler.newIrq(name)

    #Obtiene todos los programas del disco
    def getProgramasDelDisco(self, name):
        return self.getDisc().getProgram(name)

    #Agrega el pcb en la table
    def addPcb(self,aPcb):
        self.table[aPcb.getPid()] = aPcb

    #Borra el pcb en la table
    def removePcb(self,aPcb):
        #guardo las keys para tener una lista
        #y ver si la tabla de pcb esta vacia o no
        keys = self.table.keys()
        if(len(keys) != 0):
            del self.table[aPcb.getPid()]