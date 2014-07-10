from routines import Routines
class InterruptionProcessor():

    def __init__(self, aHandler, aKernel):
        self.routines = Routines(aKernel)
        self.handler = aHandler

    def execute(self):
        #mientras la cola de eventos tenga elementos
        while(self.handler.isNotEmpty()):
            #saca un evento
            event = self.handler.popFirstEvent()
            self.routines.execute(event)
