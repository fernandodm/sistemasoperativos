class SwapInRoutine():

    def __init__(self, aKernel):
        self.kernel = aKernel


    def run(self, irq):
    	memoryManager = self.kernel.getMemoryManager()
    	print "se quiere sacar de memoria el pid "+str(irq.getPid())
    	memoryManager.swapPcb(irq.getPid(),irq.getInstructions())
