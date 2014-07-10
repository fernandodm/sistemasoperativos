from pcb import Pcb

class NewRoutine():#Routine):

    def __init__(self, aKernel):
        self.kernel = aKernel


    def run(self, irq):
	print "entre en el run de new routine"
        #busca programa en disco
        prog = self.kernel.getDisc().getProgram(irq.getName())
        sizeProg = prog.getSize()

        #lo pone en memoria principal y agarra la direccion base
        print "ejecuta putData"
        self.kernel.getMemoryManager().putData(irq.getPid(), prog.getInstructions())

        #crea pcb con prioridad uno como default, despues se podra cambiar
        p = Pcb(irq.getPid(), sizeProg,1)

	self.kernel.addPcb(p)


        #pone pcb en estado ready y lo coloca en cola ready
        p.pasarAReady()
        self.kernel.getScheduler().addPcb(p)
