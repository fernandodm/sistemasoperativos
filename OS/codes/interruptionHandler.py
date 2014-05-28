class InterruptionHandler:

     def __init__(self, aKernel, aSem, aRoutines):    

        self.routines = aRoutines
        #self.kernel = aKernel
        self.eventQueue = []
        self.semaphore = aSem

    def handler(self, aIrq):
        self.semaphore.acquire()
        self.eventQueue.append(aIrq)
        self.semaphore.release()

    def isNotEmpty(self):
        return len(self.eventQueue) > 0

    def popEvent(self):
        return self.eventQueue.pop()

    def run(self):
        self.semaphore.acquire()
        #mientras la cola de eventos tenga elementos
        while(self.eventQueue.isNotEmpty()):
            #saca un evento
            event = self.eventQueue.popEvent()
            self.routines.execute(event)
        self.semaphore.release()

    
