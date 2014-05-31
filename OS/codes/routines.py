class Routines:

    def __init__(self, aKernel):
        self.routines = {Interruption.NEW: NewRoutine(aKernel), Interruption.KILL: KillRoutine(aKernel), Interruption.}

    def execute(irq):
        routine= self.routines.get(irq.getType())
        if(irq.getType() == Interruption.NEW):
            routine.run(irq.pid)
        else:
            routine.run(irq.pcb)

class NewRoutine():

    def __init__(self,aKernel).
        self.kernel = aKernel

    def run(self, pid):
        #busca programa en disco
        prog = self.kernel.getDisc().getProgram(name)
        #pregunta a disco en donde poner el programa
        cell = self.kernel.getMemory().getFirstCellWithSize(prog.getSize())
        #crea pcb
        p = Pcb(pid,cell,prog.getSize())
        #lo pone en memoria principal
        for instr in prog.getInstructions():
            self.kernel.getMemory().putDateInCell(instr,cell)
            cell += 1
        #pone pcb en estado ready y lo coloca en cola ready
        p.pasarAReady()
        self.readyQueue.adPcb(p)

class KillRoutine()

    def __init__(self,aKernel).
        self.kernel = aKernel

    def run(self, aPcb):
        #saca pcb de cpu
        self.kernel.removePcb()
        #mata el pcb de memoria
        self.kernel.getMemory().deleteDatesForPcb(aPcb)
        #le asigna un nuevo pcb a cpu
        pcb = self.kernel.getScheduler().getNextPcb()
        self.kernel.getCpu().assignPcb(pcb)
