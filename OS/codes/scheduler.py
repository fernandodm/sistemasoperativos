from fifoQueue import FifoQueue
from priorityQueue import PriorityQueue

class Scheduler():
    def __init__(self, aCpu):
        self.currentQueue = FifoQueue()
	self.cpu = aCpu

    def getNextPcb(self):
        return self.currentQueue.getMax()

    def addPcb(self, pcb):
	if(self.currentQueue.size()>0 and not(aCpu.havePcb())):
		pcb.toRunning()
		aCpu.assignPcb(pcb)
	else:
        	self.currentQueue.addPcb(pcb)

    def setFIFOMode(self):
        self.currentQueue = FifoQueue()

    def setPriorityMode(self):
        self.currentQueue = PriorityQueue()
