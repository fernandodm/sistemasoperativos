from interruption import Interruption
from newroutine import NewRoutine
from killroutine import KillRoutine
from timeoutroutine import TimeOutRoutine
from iooutputroutine import IOOutputRoutine
from ioinputroutine import IOInputRoutine
from swapInRoutine import SwapInRoutine
from swapOutRoutine import SwapOutRoutine

class Routines():

    def __init__(self, aKernel):
        self.routines = {
            Interruption.NEW: NewRoutine(aKernel),
            Interruption.KILL: KillRoutine(aKernel),
            Interruption.TIMEOUT: TimeOutRoutine(aKernel),
            Interruption.IOINPUT: IOInputRoutine(aKernel),
            Interruption.IOOUTPUT: IOOutputRoutine(aKernel),
            Interruption.SWAPIN: SwapInRoutine(aKernel),
            Interruption.SWAPOUT: SwapOutRoutine(aKernel)
        }

    def getRoutines(self):
        return self.routines

    def returnRoutineType(self, irq):
        return self.getRoutines().get(irq.getType())

    #Ejecuta la rutina
    def execute(self, irq):
        #Obtengo la rutina que seria el evento
        routine = self.returnRoutineType(irq)
        print "[Routines] Ejecutar interrupcion: "+str(routine)
        #y la ejecuto
        routine.run(irq)
        
