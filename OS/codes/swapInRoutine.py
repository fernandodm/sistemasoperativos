class SwapInRoutine():

    def __init__(self, aKernel):
        self.kernel = aKernel


    def run(self, irq):
    	memoryManager = self.kernel.getMemoryManager()
    	memoryManager.swapPcb(irq.getPid(),irq.getInstructions())
