from interruption import Interruption
from newroutine import NewRoutine
from killroutine import KillRoutine
from timeoutroutine import TimeOutRoutine

#Clase abstracta
#class Routine(): 

#    def __init__(self, aKernel):
#        self.kernel = aKernel

#    def run(self, irq):
        #delegacion a la subclase
#        pass

class Routines():

    def __init__(self, aKernel):
        self.routines = {Interruption.NEW: NewRoutine(aKernel), Interruption.KILL: KillRoutine(aKernel), Interruption.TIMEOUT: TimeOutRoutine(aKernel)}

    def getRoutines(self):
        return self.routines

    def returnRoutineType(self, irq):
        return self.getRoutines().get(irq.getType())

    def execute(self, irq):
        routine = self.returnRoutineType(irq)
        routine.run(irq)
        
