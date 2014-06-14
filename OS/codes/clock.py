import threading, time

class Clock(threading.Thread):

    def __init__(self):
        #esto es para que se puede parar el thread
        super(Clock, self).__init__()
        self._stop = threading.Event()
        self.suscribed = []
        self.isRunning = False

    def stop(self):
        self._stop.set()

    def startUp(self):
        self.isRunning = True
        self.start()

    def shutdown(self):
        self.isRunning = False
        self.stop()

    def addSuscribed(self,aSuscribed):
        self.suscribed.append(aSuscribed)
        
    def notify(self):
        for susc in self.suscribed:
            susc.run()

    def run(self):
        while(self.isRunning):
            self.notify()
            time.sleep(1)
