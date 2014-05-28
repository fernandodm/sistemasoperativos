class Routines:

    def __init__(self):

        self.routines = {Interruption.NEW: NewRoutine(), Interruption.KILL: self.executeKill, Interruption.}

    def execute(irq):
        routine= self.routines.get(irq.type)
        routine.run()

class NewRoutine:

    def run
