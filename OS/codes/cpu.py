class Cpu(): 
    
    def __init__(self, aMemory, aHandler, aSem):
        self.currentPcb = None
        self.memory = aMemory
        self.handler = aHandler
        self.quantum = 0
        self.roundRobin = 3
        self.semaphore = aSem

    def changeRoundRobin(self, nro):
        self.roundRobin = nro
    
    def pcIncrease(self):
        self.currentPcb.pcIncrease()

    def assignPcb(self,pcb):
        self.currentPcb = pcb

    def removePcb(self):
        self.currentPcb = None

    def havePcb(self):
        return self.currentPcb != None

    def execute(self):
        
        #agarra instruccion de memoria por donde va
        instruction =self.memory.getCells()[self.currentPcb.programCounter()]
        #si expiro el quantum entonces..
        #WAIT/TIMEOUT           
        if(self.quantum == self.roundRobin):
            # le dice al handler que lo ponga en wait
            #el handler se ocupa de delegar el contentSwitching
            self.handler.toWait(self.currentPcb)
            #setea quantum en 0
            self.quantum = 0

        #si la instruccion es de IO entonces..
        #IO
        elif(instruction.isIOInstruction()):
            #le indica al hanlder que es de IO y le delega el contentSwitching
            self.handler.toIO(self.currentPcb)
            #setea quantum en 0
            self.quantum = 0
    
        #si la instruccion cuando se ejecuta nos da true
        #significa que es la ultima del proceso actual
        #por lo cual..
        #KILL
        elif(instruction.execute()):
            
            #le manda el pcb al handler para que lo mate
            #el handler se ocupa de delegar el contentSwitching
            self.handler.toKill(self.currentPcb)
            #setea quantum en 0
            self.quantum = 0
            
        else:
            #si es false incrementa el pc y el quantum en 1
            self.currentPcb.pcIncrease()
            self.quantum += 1

    def run(self):
        
        if(self.havePcb()):

            #LUCHA POR EL SEMAFORO
            self.semaphore.acquire()

            if(self.havePcb()):
                self.execute()

            #DEVUELVE EL SEMAFORO
            self.semaphore.release()   
