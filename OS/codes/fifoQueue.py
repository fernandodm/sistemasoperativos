class FifoQueue():
    def __init__(self):
        self.queue = Queue()

    def addPcb(self, aPcb):
        self.queue.put(aPcb)

    def getMax(self):
        self.queue.get()
