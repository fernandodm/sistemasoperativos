from interruption import Interruption
from irq import Irq

class InterruptionHandler:

     def __init__(self, aSem, aRoutines, aKernel, aInterruptionProcessor):    

          self.pid = 0
          self.eventQueue = []
          self.interruptionProcessor = InterruptionProcessor(aRoutines,self, aKernel)
          self.semaphore = aSem

     def handler(self, aIrq):
          self.semaphore.acquire()
          self.eventQueue.append(aIrq)
          self.semaphore.release()

     def isNotEmpty(self):
          return len(self.eventQueue) > 0

     def popEvent(self):
          return self.eventQueue.pop()

     def newIrq(self, aName):
          irq = Irq(aName,interruption.NEW)
          self.handler(irq)
          self.pid += 1

     def toWait(self,aPcb):
          irq = Irq(aPcb,interruption.TIMEOUT)
          self.handler(irq)

     def toKill(self,aPcb):
          irq = Irq(aPcb,interruption.KILL)
          self.handler(irq)

     def toIOInput(self,aPcb):
          irq = Irq(aPcb,interruption.IOINPUT)
          self.handler(irq)

     def toIOOutput(self,aPcb):
          irq = Irq(aPcb,interruption.IOOUTPUT)
          self.handler(irq)

     def run(self):
          self.semaphore.acquire()
          self.interruptionProcessor.execute()
          self.semaphore.release()
