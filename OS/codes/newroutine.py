class NewRoutine():#Routine):

    def __init__(self, aKernel):
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