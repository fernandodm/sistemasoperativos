from routines import Routines
class InterruptionProcessor():

    def __init__(self, aHandler, aKernel):
    	#Routines se encarga de ejecutar un evento
        self.routines = Routines(aKernel)
        self.handler = aHandler

    def execute(self):
        #Mientras la cola de eventos tenga elementos
        while(self.handler.isNotEmpty()):
            #Saca un evento
            event = self.handler.popFirstEvent()
            #Ejecuta el evento
            self.routines.execute(event)
