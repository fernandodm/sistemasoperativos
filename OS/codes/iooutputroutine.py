from irq import Irq
from interruption import Interruption
class IOOutputRoutine():

        def __init__(self, aKernel):
                self.kernel = aKernel

        def run(self, aIrq):
                pcb = aIrq.getPcb()
                self.kernel.getScheduler().addPcb(pcb)  