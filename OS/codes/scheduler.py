from fifoQueue import FifoQueue
from priorityQueue import PriorityQueue

class Scheduler():
    def __init__(self, aCpu):
        self.currentQueue = FifoQueue()
        self.cpu = aCpu

    def getNextPcb(self):
        return self.currentQueue.getMax()

    def addPcb(self, pcb):
        if(self.currentQueue.isEmpty() and not(self.cpu.havePcb())):
            pcb.toRunning()
            self.cpu.assignPcb(pcb)
            print "fui directamente a cpu"
        else:
            self.currentQueue.addPcb(pcb)
            print "puse en queue y quedo tamanio "+str(self.currentQueue.size())

    def setFIFOMode(self):
        self.currentQueue = FifoQueue()

    def setPriorityMode(self):
        self.currentQueue = PriorityQueue()

    def removePid(self):
        #hay q hacer el remove para priority
        self.currentQueue.removePid()