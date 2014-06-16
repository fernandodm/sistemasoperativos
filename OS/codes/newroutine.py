from pcb import Pcb

class NewRoutine():#Routine):

    def __init__(self, aKernel):
        self.kernel = aKernel


    def run(self, irq):
        #busca programa en disco
        prog = self.kernel.getDisc().getProgram(irq.getName())
        #pregunta a disco en donde poner el programa
        sizeProg = prog.getSize()
        cell = self.kernel.getMemory().getFirstCellWithSize(sizeProg)
        #crea pcb con prioridad uno como default, despues se podra cambiar
        p = Pcb(irq.getPid(),cell,sizeProg,1)
        #lo pone en memoria principal
        for instr in prog.getInstructions():
            self.kernel.getMemory().putDateInCell(instr,cell)
            cell += 1
        #pone pcb en estado ready y lo coloca en cola ready
        p.pasarAReady()
        self.kernel.getScheduler().addPcb(p)