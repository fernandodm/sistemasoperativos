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

from threading import Semaphore

semaphore = Semaphore(1)
size = 6
kernel = Kernel(semaphore,size)

#########################################
#########################################
instruction1 = Instruction("primer instruccionP1",False,False)
instruction2 = Instruction("segunda instruccionP1",False,False)
instruction3 = Instruction("tercer instruccionP1",False,True)

instructionp1 = Instruction("primer instruccionP2",False,False)
instructionp2 = Instruction("segunda instruccionP2",False,False)
instructionp3 = Instruction("tercer instruccionP2",False,True)

instruction14 = Instruction("primer instruccionP3",False,False)
instruction24 = Instruction("segunda instruccionP3",False,False)
instruction34 = Instruction("tercer instruccionP3",False,True)

instructions = [instruction1,instruction2,instruction3]
instruc = [instructionp1,instructionp2,instructionp3]
ins = [instruction14,instruction24,instruction34]

prog1 = Program("Programa 1",instructions)
##########################################

prog2 = Program("Programa 2",instruc)
##########################################

prog3 = Program("Programa 3",ins)
##########################################

kernel.getDisc().addProgram(prog1)
kernel.getDisc().addProgram(prog2)
kernel.getDisc().addProgram(prog3)

kernel.startUp()
kernel.run("Programa 1")
kernel.run("Programa 3")
kernel.run("Programa 2")
time.sleep(20)
kernel.shutDown()