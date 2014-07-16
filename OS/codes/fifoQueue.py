from Queue import Queue

class FifoQueue():
    def __init__(self):
        self.queue = Queue()

    def isEmpty(self):
        return self.queue.empty()

    def size(self):
    	return self.queue.qsize()

    def addPcb(self, aPcb):
        self.queue.put(aPcb)

    def getMax(self):
    	if not(self.queue.empty()):
            return self.queue.get()
        else:
        	return None

    def fillTo(self,queue2):
        while(not(queue2.empty())):
            self.queue.put(queue2.get())

    def removePid(self, aPid):
        queue = Queue()
        pcbNotFound = True
        while(not self.isEmpty()):
            currentPcb = self.getMax()
            if(currentPcb.getPid() != aPid):
                queue.put(currentPcb)
        self.fillTo(queue)