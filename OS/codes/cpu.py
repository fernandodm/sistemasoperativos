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
            #SHEDULERRRR !!!!!!!!!!
            self.currentPcb = self.queue.getMax()
        #agarra instruccion de memoria por donde va
        instruction =self.memory.getCells()[self.currentPcb.programCounter]
        #if(se ejecuta una instruccion)
        #sumar el quantum
        #if(preguntar si expiro el quantum)
        # le dice al handler que lo ponga en wait
        # me saco el pcb
        if(self.quantum == 3):
            self.handler.toWait(self.pcb)
            self.currentPcb = None
            self.quantum = 0
            
        elif(instruction.execute()):
            
            #si es true le da kill y se lo manda al handler
            #decir a handler que mate el pcb
            self.handler.toKill(self.pcb)
            #me saco el pcb
            self.currentPcb = None
            #quantum en 0
            self.quantum = 0
        else:
            #si es false incrementa el pc
            self.currentPcb.pcIncrease()
            self.quantum += 1 
        #le dice a su handler que ejecute los eventos
        self.handler.run()
