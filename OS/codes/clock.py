import threading

class Clock(Thread):

    def __init__(self):
        self.suscribed = []
        self.isRunning = True

    def shutdown(self):
        self.isRunning = False

    def addSuscribed(self,aSuscribed):
        self.suscribed.append(aSuscribed)
        
    def notify(self):
        for susc in self.suscribed:
            susc.run()

    def run(self):
        while(self.isRunning):
            self.notify()
            self.sleep(1)
