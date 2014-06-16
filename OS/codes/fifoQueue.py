from Queue import Queue

class FifoQueue():
    def __init__(self):
        self.queue = Queue()

    def size(self):
    	return self.queue.qsize()

    def addPcb(self, aPcb):
        self.queue.put(aPcb)

    def getMax(self):
        return self.queue.get()
