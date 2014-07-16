class TimeOutRoutine():

    def __init__(self, aKernel):
        self.kernel = aKernel

    def run(self,irq):
        #sacar el pcb de cpu
        self.kernel.getCpu().removePcb()
        #pone el pcb en estado wait
        irq.getPcb().toWait()
        #poner el pcb en cola ready
        self.kernel.getScheduler().addPcb(irq.getPcb())
        #pide al scheduler un pcb
        aPcb = self.kernel.getScheduler().getNextPcb()
        print "PID salee" + str(irq.getPcb().getPid())
        if(aPcb != None):
            print "PID entraa" + str(aPcb.getPid())
            #asigna el pcb al cpu
            self.kernel.getCpu().assignPcb(aPcb)
