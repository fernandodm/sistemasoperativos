from fifoQueue import FifoQueue
from priorityQueue import PriorityQueue

class Scheduler():
    def __init__(self, aCpu):
        self.currentQueue = FifoQueue()
	self.cpu = aCpu

    def getNextPcb(self):
        return self.currentQueue.getMax()

    def addPcb(self, pcb):
	if(self.currentQueue.size()==0 and not(self.cpu.havePcb())):
		pcb.toRunning()
		self.cpu.assignPcb(pcb)
	else:
        	self.currentQueue.addPcb(pcb)

    def setFIFOMode(self):
        self.currentQueue = FifoQueue()

    def setPriorityMode(self):
        self.currentQueue = PriorityQueue()

    def removePid(self):
        #hay q hacer el remove para priority
        self.currentQueue.removePid()