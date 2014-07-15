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
          self.eventQueue.append(aIrq)

     def isNotEmpty(self):
          return (len(self.eventQueue) > 0)

     def popFirstEvent(self):
          event = self.eventQueue[0]
          self.eventQueue.remove(event)
          return event

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

     def toSwapIn(self, aPid, instructionsList):
          irq = Irq(instructionsList,Interruption.SWAPIN, aPid)
          self.handler(irq)  

     def toSwapOut(self):
          irq = Irq(None,Interruption.SWAPOUT, None)
          self.handler(irq)  

     def run(self):
          self.semaphore.acquire()
          self.interruptionProcessor.execute()
          self.semaphore.release()
