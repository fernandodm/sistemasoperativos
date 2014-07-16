class KillRoutine():#Routine):

    def __init__(self, aKernel):
        self.kernel = aKernel

    def run(self, irq):
        #saca pcb de cpu
        self.kernel.getCpu().removePcb()
        #mata el pcb del kernel
        self.kernel.removePcb(irq.getPcb())
        #pone el pcb en estado EXIT
        irq.getPcb().toExit()
        #mata el pcb de memoria
        self.kernel.getMemoryManager().deleteDataForPcb(irq.getPcb())
        #verifico si hay instrucciones en disco
        #si hay, se lanzara una interrupcion de SwapOut
        pids = self.kernel.getDisc().getInstructions().keys()
        if(len(pids) > 0):
            handler = self.kernel.getHandler()
            handler.toSwapOut()
        
        pcb = self.kernel.getScheduler().getNextPcb()
        #le asigna un nuevo pcb a cpu
        self.kernel.getCpu().assignPcb(pcb)
