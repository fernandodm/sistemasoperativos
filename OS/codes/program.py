class Program():
    def __init__(self,aName, anInstructions):
        self.name = aName
        self.instructions = anInstructions

    def getInstructions(self):
        return self.instructions

    def getName(self):
        return self.name

    def getSize(self):
        return len(self.getInstructions())

    def addIstrucction(self,aString):
        self.getInstructions().append(aString)
        
