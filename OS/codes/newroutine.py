from pcb import Pcb

class NewRoutine():

    def __init__(self, aKernel):
        self.kernel = aKernel

    def run(self, irq):
        print "[NewRoutine] Buscando programa en disco.."
        #busca programa en disco
        prog = self.kernel.getDisc().getProgram(irq.getName())
        sizeProg = prog.getSize()
        print "[NewRoutine] Se encontro el programa: " + str(irq.getName())
        #crea pcb con prioridad uno como default, despues se podra cambiar
        pcb = Pcb(irq.getPid(), sizeProg,1)

        self.kernel.addPcb(pcb)
        #lo pone en memoria principal y agarra la direccion base
        if(self.kernel.getMemoryManager().putData(irq.getPid(), prog.getInstructions())):
            #pone pcb en estado ready y lo coloca en cola ready
            pcb.pasarAReady()
            self.kernel.getScheduler().addPcb(pcb)
            print "[NewRoutine] Se agrego el pcb a la cola ready"
