class TimeOutRoutine():#Routine):

    def __init__(self, aKernel):
        self.kernel = aKernel

    def run(self,irq):
        #sacar el pcb de cpu
        self.kernel.getCpu().removePcb(irq.getPcb())
        #poner el pcb en cola ready
        self.kernel.getScheduler().addPcb(irq.getPcb())
        #pide al scheduler un pcb
        aPcb = self.kernel.getScheduler().getMax()
        #asigna el pcb al cpu
        self.kernel.getCpu().assignPcb(aPcb)