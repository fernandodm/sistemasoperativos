class IOInputRoutine():

	    def __init__(self, aKernel):
        self.kernel = aKernel

        def run(self, aIrq):
        	#le saca el pcb al irq
        	pcb = aIrq.getNameOrPcb()
        	#le dice le pide al kernel el IO y le encola el pcb
        	self.kernel.getIO().receive(pcb)