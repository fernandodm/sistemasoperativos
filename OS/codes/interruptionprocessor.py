from routines import Routines
class interruptionProcessor():

    def __init__(self, aHandler, aKernel):
        aRoutines.setKernel(aKernel)
        self.routines = Routines(aKernel)
        self.handler = aHandler

    def execute(self):
        #mientras la cola de eventos tenga elementos
        while(self.handler.eventQueue.isNotEmpty()):
            #saca un evento
            event = handler.queueEvent.popEvent()
            self.routines.execute(event)
