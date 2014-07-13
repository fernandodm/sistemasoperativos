class Disc():
    def __init__(self):
        self.cells = []
        self.instructions = {}

    def getInstructions(self):
        return self.instructions

    def getCells(self):
        return self.cells

    def addProgram(self,program):
        self.getCells().append(program)

    def getProgram(self,name):
        cells = self.getCells()
        for index in cells:
            if(index.getName()==name):
                return index
            
    def saveIntructions(self,aPid,instructions):
        self.instructions[aPid] = instructions
