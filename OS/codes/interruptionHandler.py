from interruption import Interruption
from interruptionprocessor import InterruptionProcessor
from irq import Irq

class InterruptionHandler:

     def __init__(self, aKernel):
          #Contador de pid    
          self.pid = 0
          self.eventQueue = []
          self.interruptionProcessor = InterruptionProcessor(self, aKernel)

     def getEventQueue(self):
          return self.eventQueue

     def lastInstrutionIsIO(self):
          return self.eventQueue[len(self.eventQueue)]

     #Agrega el evento a la cola
     def handler(self, aIrq):
          self.eventQueue.append(aIrq)

     def isNotEmpty(self):
          return (len(self.eventQueue) > 0)

     #Obtiene el primer evento de la cola y lo elimina
     def popFirstEvent(self):
          event = self.eventQueue[0]
          self.eventQueue.remove(event)
          return event

     #Agrega un evento de newIrq a la eventQueue
     #y actualiza el contador de pid
     def newIrq(self, aName):
          irq = Irq(aName,Interruption.NEW, self.pid)
          self.handler(irq)
          self.pid += 1

     #Agrega un evento de wait a la eventQueue
     def toWait(self,aPcb):
          irq = Irq(aPcb,Interruption.TIMEOUT, None)
          self.handler(irq)

     #Agrega un evento de kill a la eventQueue
     def toKill(self,aPcb):
          irq = Irq(aPcb,Interruption.KILL, None)
          self.handler(irq)

     #Agrega un evento de IOInput a la eventQueue
     def toIOInput(self,aPcb):
          irq = Irq(aPcb,Interruption.IOINPUT, None)
          self.handler(irq)

     #Agrega un evento de IOOutput a la eventQueue
     def toIOOutput(self,aPcb):
          irq = Irq(aPcb,Interruption.IOOUTPUT, None)
          self.handler(irq)

     #Agrega un evento de swapIn a la eventQueue
     def toSwapIn(self, aPid, instructionsList):
          irq = Irq(instructionsList,Interruption.SWAPIN, aPid)
          self.handler(irq)  

     #Agrega un evento de swapOut a la eventQueue
     def toSwapOut(self):
          irq = Irq(None,Interruption.SWAPOUT, None)
          self.handler(irq)  

     #Ejecuta los eventos
     def run(self):
          self.interruptionProcessor.execute()

