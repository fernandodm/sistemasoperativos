class Cpu(): 
    
    def __init__(self, aMemoryManager, aHandler, aSem):
        self.currentPcb = None
        self.memoryManager = aMemoryManager
        self.handler = aHandler
        self.quantum = 0
        self.roundRobin = 2
        self.semaphore = aSem

    def changeRoundRobin(self, nro):
        self.roundRobin = nro
    
    def pcIncrease(self):
        self.currentPcb.pcIncrease()

    def assignPcb(self,pcb):
        print "assignPcb "+ str(pcb.getPid())
        self.currentPcb = pcb

    def removePcb(self):
        self.currentPcb = None

    def havePcb(self):
        return self.currentPcb != None

    def execute(self):
        
        #agarra instruccion de memoria por donde va
        instruction =self.memoryManager.getInstruction(self.currentPcb.getPid(),self.currentPcb.displacement)
        #si expiro el quantum entonces..
        #WAIT/TIMEOUT  
        print "[CPU] Ejecutar instruccion.."         
        if(self.quantum == self.roundRobin):
            #setea quantum en 0
            self.quantum = 0
            # le dice al handler que lo ponga en wait
            #el handler se ocupa de delegar el contentSwitching
            self.handler.toWait(self.currentPcb)

        #si la instruccion es de IO entonces..
        #IO
        elif(instruction.isIOInstruction()):
            #setea quantum en 0
            self.quantum = 0
            #le indica al hanlder que es de IO y le delega el contentSwitching
            self.handler.toIO(self.currentPcb)
    
        #si la instruccion cuando se ejecuta nos da true
        #significa que es la ultima del proceso actual
        #por lo cual..
        #KILL
        elif(instruction.execute()):
            #setea quantum en 0
            self.quantum = 0
            #le manda el pcb al handler para que lo mate
            #el handler se ocupa de delegar el contentSwitching
            self.handler.toKill(self.currentPcb)
            
        else:
            #si es false incrementa el pc y el quantum en 1
            self.currentPcb.pcIncrease()
            self.quantum += 1

    def run(self):
        
        if(self.havePcb()):
            #LUCHA POR EL SEMAFORO
            self.semaphore.acquire()
            if(self.havePcb()):
                self.currentPcb.old += 1 
                self.execute()

            #DEVUELVE EL SEMAFORO
            self.semaphore.release()   
