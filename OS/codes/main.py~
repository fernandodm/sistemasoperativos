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
size = 20
kernel = Kernel(semaphore,size)

#########################################
instruction1 = Instruction("primer instruccion",False,False)
instruction2 = Instruction("segunda instruccion",False,False)
instruction3 = Instruction("tercer instruccion",False,True)

instructions = [instruction1,instruction2,instruction3]

prog1 = Program("Programa 1",instructions)
##########################################

prog2 = Program("Programa 2",instructions)
##########################################

prog3 = Program("Programa 3",instructions)
##########################################

kernel.getDisc().addProgram(prog1)
kernel.getDisc().addProgram(prog2)
kernel.getDisc().addProgram(prog3)

kernel.startUp()
kernel.run("Programa 1")
kernel.run("Programa 2")
kernel.run("Programa 3")
time.sleep(20)
kernel.shutDown()