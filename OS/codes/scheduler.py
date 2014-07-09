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
		print "se lo pase directamente al cpu"
		pcb.toRunning()
		self.cpu.assignPcb(pcb)
	else:
		print "lo puse en cola de ready"
        	self.currentQueue.addPcb(pcb)

    def setFIFOMode(self):
        self.currentQueue = FifoQueue()

    def setPriorityMode(self):
        self.currentQueue = PriorityQueue()
