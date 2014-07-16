from pcb import Pcb

class SwapOutRoutine():

    def __init__(self, aKernel):
        self.kernel = aKernel

    def run(self, irq):
    	memoryManager = self.kernel.getMemoryManager()
    	memoryManager.addIntructionsForTheDisc()
