from interruption import Interruption

class Kernel:
    def __init__(self, aCpu, aDisc, aMem, aHand, aQueue):
        self.disc = aDisc
        self.cpu = aCpu
        self.memory = aMem
        self.handler = aHand
        self.qReady = aQueue
        self.semaphoreMKernel = Semaphore(0)
        self.semaphoreMCPU = Semaphore(0)
        self.semaphoreIO = Semaphore(0)

    def getQReady(self):
        return self.qReady

    def getDisc(self):
        return self.disc

    def getCpu(self):
        return self.cpu
    
    def getMemory(self):
        return self.memory

    def getHandle(self):
        return self.handler

    def startUp(self):
        #crearia los hilos de los threads de I/O, CPU y Kernel
        #ESTEBAN        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def run(self, name):
        #busca programa en disco
        prog = self.getProgramasDelDisco(name)
        #pregunta a disco en donde poner el programa
        cell = self.getMemory().getFirstCellWithSize(prog.getSize())
        #le indica a su handle que cree el pcb
        pcb = self.getHandle().execute(Interrupcion.NEW, prog)
        #lo pone en memoria principal
        for instr in prog.getInstructions():
            self.mainMemory.putDateInCell(instr,cell)
            cell = cell + 1
        pcb.pasarAReady()
        self.getQReady().addPcb(pcb)
        

    def getProgramasDelDisco(self, name):
        return self.getDisc().getProgram(name)
