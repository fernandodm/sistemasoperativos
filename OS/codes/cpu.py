class Cpu(): 
    
    def __init__(self, aMemory, aWaitingIO, aHandler, aQueue):
        self.currentPcb = None
        self.memory = aMemory
        self.handler = aHandler
        self.waitingIO = aWaitingIO
        self.queue = aQueue
        self.quantum = 0
        
    def getInstructionFetch(self):
        fetch = self.currentPcb.programCounter
        instruction = self.memory.getCells()[fetch]
    
    def pcIncrease(self):
        self.currentPcb.pcIncrease()
        
    def finishPcb(self):
        self.currentPcb.toExit()
        
    def sendPcbTOWaitingIO(self)
        self.waitingIO.queueInstruction(currentPcb)

    def run(self):
        #agarra el pcb de la cola
        if(self.currentPcb == None):
            self.currentPcb = self.queue.getMax()
        #agarra instruccion de memoria
        instruction =self.memory.getCells()[self.currentPcb.basePointer]
        #if(se ejecuta una instruccion)
        #sumar el quantum
        #if(preguntar si expiro el quantum)
        # le dice al handler que lo ponga en wait
        # me saco el pcb
        if(instruction.execute()):
            
            #si es true le da kill y se lo manda al handler
            #decir a handler que mate el pcb
            self.handler.toKill(self.pcb)
            #me saco el pcb
            self.currentPcb = None
        else:
            #si es false incrementa el pc
            self.currentPcb.pcIncrease()
        #le dice a su handler que ejecute los eventos
        self.handler.run()
