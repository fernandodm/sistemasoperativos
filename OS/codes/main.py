import threading, time
from badwaysetting import BadWaySetting
from bestsetting import BestSetting
from block import Block
from chance import Chance
from fifoQueue import FifoQueue
from firstsetting import FirstSetting
from instruction import Instruction
from interruption import Interruption
from interruptionprocessor import InterruptionProcessor
from io import IO
from ioinputroutine import IOInputRoutine
from iooutputroutine import IOOutputRoutine
from irq import Irq
from kernel import Kernel
from killroutine import KillRoutine
from logicalMemory import LogicalMemory
from mainmemory import MainMemory
from memoryManager import MemoryManager
from newroutine import NewRoutine
from pcb import Pcb
from priorityQueue import PriorityQueue
from program import Program
from routines import Routines
from setting import Setting
from status import Status
from timeoutroutine import TimeOutRoutine

memorySize = 4

kernel = Kernel(memorySize)
#kernel.getScheduler().setPriorityMode()
#########################################
#########################################
instruction1 = Instruction("{Programa 1} primera instruccion",False,False)
instruction2 = Instruction("{Programa 1} segunda instruccion",False,True)


instruction3 = Instruction("{Programa 2} primera instruccion",True,False)
instruction4 = Instruction("{Programa 2} segunda instruccion",False,True)

instruction5 = Instruction("{Programa 3} primera instruccion",False,False)
instruction6 = Instruction("{Programa 3} segunda instruccion",False,True)

instruction7 = Instruction("{Programa 4} primera instruccion",False,False)
instruction8 = Instruction("{Programa 4} segunda instruccion",False,True)

instructionsP1 = [instruction1,instruction2]
instructionsP2 = [instruction3,instruction4]
instructionsP3 = [instruction5,instruction6]
instructionsP4 = [instruction7,instruction8]

prog1 = Program("Programa 1",instructionsP1)
##########################################

prog2 = Program("Programa 2",instructionsP2)
##########################################

prog3 = Program("Programa 3",instructionsP3)
##########################################

prog4 = Program("Programa 4",instructionsP4)
##########################################

kernel.getDisc().addProgram(prog1)
kernel.getDisc().addProgram(prog2)
kernel.getDisc().addProgram(prog3)
kernel.getDisc().addProgram(prog4)

kernel.startUp()
kernel.run("Programa 1")
kernel.run("Programa 2")
kernel.run("Programa 3")
kernel.run("Programa 4")
#time.sleep(1)
#kernel.getTable()[3].changePriority(2)
time.sleep(20)
kernel.shutDown()
