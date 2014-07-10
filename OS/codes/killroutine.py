class KillRoutine():#Routine):

    def __init__(self, aKernel):
        self.kernel = aKernel

    def run(self, irq):
        #saca pcb de cpu
        self.kernel.getCpu().removePcb()
	#mata el pcb del kernel
	self.kernel.removePcb(irq.getPcb())
        #mata el pcb de memoria
        self.kernel.getMemoryManager().deleteDataForPcb(irq.getPcb())
        #le asigna un nuevo pcb a cpu
        pcb = self.kernel.getScheduler().getNextPcb()

        self.kernel.getCpu().assignPcb(pcb)
