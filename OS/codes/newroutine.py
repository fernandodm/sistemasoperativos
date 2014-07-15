from pcb import Pcb

class NewRoutine():

    def __init__(self, aKernel):
        self.kernel = aKernel


    def run(self, irq):
        print "[NewRoutine] Buscando programa en disco"
        #busca programa en disco
        prog = self.kernel.getDisc().getProgram(irq.getName())
        sizeProg = prog.getSize()

        #lo pone en memoria principal y agarra la direccion base
        print "[NewRoutine] Agregando instrucciones a memoria"
        #crea pcb con prioridad uno como default, despues se podra cambiar
        p = Pcb(irq.getPid(), sizeProg,1)

        self.kernel.addPcb(p)
        if(self.kernel.getMemoryManager().putData(irq.getPid(), prog.getInstructions())):



            #pone pcb en estado ready y lo coloca en cola ready
            p.pasarAReady()
            print "[NewRoutine] Agregando pcb a la cola ready"
            self.kernel.getScheduler().addPcb(p)
