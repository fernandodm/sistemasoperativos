from fifoQueue import FifoQueue
from priorityQueue import PriorityQueue

class Scheduler():
    def __init__(self):
        self.currentQueue = FifoQueue()

    def getNextPcb(self):
        return self.currentQueue.getMax()

    def addPcb(self, pcb):
        self.currentQueue.addPcb(pcb)

    def setFIFOMode(self):
        self.currentQueue = FifoQueue()

    def setPriorityMode(self):
        self.currentQueue = PriorityQueue()
