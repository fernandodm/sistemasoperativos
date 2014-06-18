from irq import Irq

class IOOutputRoutine():

	def __init__(self, aKernel):
                self.kernel = aKernel

        def run(self, aIrq):
        	pcb = aIrq.getNameOrPcb()
        	instruction = self.kernel.getMemory().getCells()[pcb.programCounter()]
        	if(instruction.isFinal()):
        		irq = Irq(pcb,Interruption.KILL, pcb.getPid())
        		self.kernel.getHandler().handler(irq)
        	else:
        		pcb.pcIncrease()
        		self.kernel.getScheduler().addPcb(pcb)    	