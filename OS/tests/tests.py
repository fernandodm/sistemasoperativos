import unittest

from tchance import ChanceTest
from tclock import ClockTest
from tcpu import CpuTest
from tdisc import DiscTest
from tfifoQueue import FifoQueueTest
from tinterruptionHandler import InterruptionHandlerTest
from tinterruptionProcessor import InterruptionProcessorTest
from tkernel import KernelTest
from tpriorityQueue import PriorityQueueTest
from tmainmemory import MainMemoryTest
from troutines import RoutinesTest
from tnewroutine import NewRoutineTest
from tkillroutine import KillRoutineTest
from tlogicalmemory import LogicalMemoryTest
from tioInputRoutine import IOInputRoutineTest
from tioOutputRoutine import IOOutputRoutineTest
from tswapInRoutine import SwapInRoutineTest
from tswapOutRoutine import SwapOutRoutineTest
from tbadwaysetting import BadWaySettingTest
from tbestsetting import BestSettingTest
from tfirstsetting import FirstSettingTest
from tcontinuousassignment import ContinuousAssignmentTest
from tinstruction import InstructionTest
from tio import IOTest
from tmemoryManager import MemoryManagerTest
from tscheduler import SchedulerTest
from ttimeoutroutine import TimeOutRoutineTest

listTests = [ChanceTest,ClockTest,CpuTest,DiscTest,FifoQueueTest,InterruptionHandlerTest,
InterruptionProcessorTest,KernelTest,PriorityQueueTest, MainMemoryTest, RoutinesTest, 
NewRoutineTest, KillRoutineTest, LogicalMemoryTest, IOOutputRoutineTest, SwapInRoutineTest,
SwapOutRoutineTest, BadWaySettingTest, BestSettingTest, FirstSettingTest,
ContinuousAssignmentTest, InstructionTest, IOTest, MemoryManagerTest, SchedulerTest,
TimeOutRoutineTest]

for test in listTests:
	suite = unittest.TestLoader().loadTestsFromTestCase(test)
	unittest.TextTestRunner(verbosity=2).run(suite) 
