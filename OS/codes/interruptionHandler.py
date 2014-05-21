class InterruptionHandler:
    def __init__(self, aKernel):    
        self.interrupciones = {Interrupcion.NEW:executeNew(name),Interrupcion.KILL:executeKill(name),Interrupcion.TIMEOUT:executeTimeOut(name),Interrupcion.IOINPUT:executeIOInput(name), Interrupcion.IOOutput:executeIOOutput(name)}
        self.currentPid = 0
        self.kernel = aKernel
        self.eventQueue = []
    
    def getPid(self):
        self.currentPid +=1
        return self.currentPid-1


   def execute(self, interrupcion, name):
        self.getKernel().setModeKernel()
        self.getInterrupciones().get(interrupcion)(name) 
        self.getKernel().setModeUser()

    def toKill(self,aPcb):
        #SEMAFORO
        #ponerlo en eventQueue
        self.eventQueue.append(aPcb)

    def executeNew(self, name):
        #busco programa y lo cargo en memoria principal
        prog = self.getKernel().getProgramasDelDisco(name)
        #retorna la celda en donde se puso y lo guardo en cell
        cell = self.getKernel().cargarProgramaEnMemoria()
        #creo Pcb
        pcb = Pcb(self.getPid(),cell,prog.getSize())
        #lo pongo en cola de ready
        self.getKernel().pedirleAlSchedulerQuePongaPcbEnCola(pcb)

    def executeKill(self):
        #sacar las intrucciones del pcb de memoria
        #sacar el pcb de la cola de eventos

    def run(self):
        #SEMAFORO - self.getKernel().setModeKernel()
        #agarra evento de la cola
        #pregunta que tipo de evento
        #procesa
        #SEMAFORO - self.getKernel().setModeUser()
