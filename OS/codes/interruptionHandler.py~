from interruption import Interruption
from interruptionprocessor import InterruptionProcessor
from irq import Irq

class InterruptionHandler:

     def __init__(self, aSem, aKernel):    

          self.pid = 0
          self.eventQueue = []
          self.interruptionProcessor = InterruptionProcessor(self, aKernel)
          self.semaphore = aSem

     def getEventQueue(self):
          return self.eventQueue

     def lastInstrutionIsIO(self):
          return self.eventQueue[len(self.eventQueue)]

     def handler(self, aIrq):
          self.semaphore.acquire()
          self.eventQueue.append(aIrq)
          self.semaphore.release()

     def isNotEmpty(self):
          return (len(self.eventQueue) > 0)

     def popEvent(self):
          return self.eventQueue.pop()

     def newIrq(self, aName):
          irq = Irq(aName,Interruption.NEW, self.pid)
          self.handler(irq)
          self.pid += 1

     def toWait(self,aPcb):
          irq = Irq(aPcb,Interruption.TIMEOUT, None)
          self.handler(irq)

     def toKill(self,aPcb):
          irq = Irq(aPcb,Interruption.KILL, None)
          self.handler(irq)

     def toIOInput(self,aPcb):
          irq = Irq(aPcb,Interruption.IOINPUT, None)
          self.handler(irq)

     def toIOOutput(self,aPcb):
          irq = Irq(aPcb,Interruption.IOOUTPUT, None)
          self.handler(irq)

     def run(self):
          self.semaphore.acquire()
          self.interruptionProcessor.execute()
          self.semaphore.release()
