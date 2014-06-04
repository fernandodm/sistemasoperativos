class Routines():

    def __init__(self, aKernel):
        self.routines = {Interruption.NEW: NewRoutine(aKernel), Interruption.KILL: KillRoutine(aKernel), Interruption.TIMEOUT: TimeOutRoutine(aKernel)}

    def execute(irq):
        routine= self.routines.get(irq.getType())
        routine.run(irq)

class NewRoutine():

    def __init__(self,aKernel):
        self.kernel = aKernel

    def run(self, irq):
        #busca programa en disco
        prog = self.kernel.getDisc().getProgram(irq.getName())
        #pregunta a disco en donde poner el programa
        cell = self.kernel.getMemory().getFirstCellWithSize(prog.getSize())
        #crea pcb
        p = Pcb(irq.getPid(),cell,prog.getSize())
        #lo pone en memoria principal
        for instr in prog.getInstructions():
            self.kernel.getMemory().putDateInCell(instr,cell)
            cell += 1
        #pone pcb en estado ready y lo coloca en cola ready
        p.pasarAReady()
        self.kernel.scheduler.addPcb(p)

class KillRoutine():

    def __init__(self,aKernel):
        self.kernel = aKernel

    def run(self, irq):
        #saca pcb de cpu
        self.kernel.cpu.removePcb()
        #mata el pcb de memoria
        self.kernel.getMemory().deleteDatesForPcb(irq.getPcb())
        #le asigna un nuevo pcb a cpu
        pcb = self.kernel.getScheduler().getNextPcb()
        self.kernel.getCpu().assignPcb(pcb)

class TimeOutRoutine():

    def __init__(self,aKernel):
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
        
