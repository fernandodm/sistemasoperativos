class Cpu(): 
    
    def __init__(self, aMemoryManager, aHandler):
        self.currentPcb = None
        self.memoryManager = aMemoryManager
        self.handler = aHandler
        self.quantum = 0
        self.roundRobin = 2

    def getMemory(self):
        return self.memoryManager

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

    def getCurrentPcb(self):
	   return self.currentPcb

    def execute(self):
        
        #agarra instruccion de memoria por donde va
        pid = self.getCurrentPcb().getPid()
        disp = self.getCurrentPcb().getDisplacement()
        instruction = self.getMemory().getInstruction(pid,disp)
        #si expiro el quantum entonces..
        #WAIT/TIMEOUT  
        print "[CPU] Ejecutar instruccion.."         
        if(self.quantum == self.roundRobin):
            #setea quantum en 0
            self.quantum = 0
            # le dice al handler que lo ponga en wait
            #el handler se ocupa de delegar el contentSwitching
            self.handler.toWait(self.getCurrentPcb())

        #si la instruccion es de IO entonces..
        #IO
        elif(instruction.isIOInstruction()):
            #setea quantum en 0
            self.quantum = 0
            #le indica al hanlder que es de IO y le delega el contentSwitching
            self.handler.toIOInput(self.getCurrentPcb())
    
        #si la instruccion cuando se ejecuta nos da true
        #significa que es la ultima del proceso actual
        #por lo cual..
        #KILL
        elif(instruction.execute()):
            #setea quantum en 0
            self.quantum = 0
            #le manda el pcb al handler para que lo mate
            #el handler se ocupa de delegar el contentSwitching
            self.handler.toKill(self.getCurrentPcb())
            
        else:
            #si es false incrementa el pc y el quantum en 1
            self.getCurrentPcb().pcIncrease()
            self.quantum += 1

    def run(self):
        if(self.havePcb()):
            self.getCurrentPcb().old += 1 
            self.execute() 
