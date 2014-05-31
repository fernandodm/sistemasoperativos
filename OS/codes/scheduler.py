from Queue import Queue

class Scheduler():
    def __init__(self, aQueueReady, aFifoQueue):
    self.queueReady = aQueueReady
    self.queueFifo = aFifoQueue
    self.currentQueue = aFifoQueue

    def getNextPcb(self):
        return self.currentQueue.getMax()

    def setModeFIFO(self):
        self.currentQueue = Queue()

    def setModePriority(self):
        self.currentQueue = self.queueReady
