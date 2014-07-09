from kernel import Kernel
from Queue import Queue
from interruption import Interruption

class IO():

	def __init__(self,aKernel, aSem):
		self.semaphore = aSem
		self.kernel = aKernel
		self.queue = Queue()

	def getQueue(self):
		return self.queue

	def queueisEmpty(self):
		return (self.getQueue().qsize() == 0)

	def receivePcb(self, aPcb):
		self.queue.put(aPcb)

	def fetch(self):
		return self.getQueue().pop()
 
	def run(self):
		self.semaphore.acquire()
		#pregunta si hay elementos en su cola
		if(not(self.queueisEmpty())):
			#agarra el proximo pcb
			pcb = self.fetch()
			#encuentra la intruccion actual
			instruction = self.kernel.getMemory().getCells()[pcb.programCounter()]
			#la executa
			instruction.execute()
			#crea la irq con el tipo iooutput
			irq = Irq(pcb,Interruption.IOOUTPUT,pcb.getPid())
			#le manda la irq al handler
			self.kernel.getHandler().handler(irq)
		self.semaphore.release()