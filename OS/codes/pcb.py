from status import Status

class Pcb():
  def __init__(self, aPid, aSize, aPriority):
    self.pid = aPid
    self.displacement = 0
    self.size = aSize
    self.status = Status.NEW
    self.priority = aPriority
    self.old = 0

  def getOld(self):
    return self.old

  def getSize(self):
    return self.size    

  def getPid(self):
    return self.pid

  def pasarAReady(self):
    self.status = Status.READY

  def toExit(self):
    self.status = Status.EXIT

  def toRunning(self):
    self.status = Status.RUNNING

  def toWait(self):
    self.status = Status.WAITING

  def toExit(self):
    self.status = Status.EXIT

  def pcIncrease(self):
    self.displacement = self.displacement + 1

  def changePriority(self, integ):
    self.priority = integ

  def getPriority(self):
    return self.priority
