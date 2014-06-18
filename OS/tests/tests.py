import unittest

from tchance import ChanceTest
from tclock import ClockTest
from tcpu import CpuTest
from tdisc import DiscTest
from  tfifoQueue import FifoQueueTest
from tinterruptionHandler import InterruptionHandlerTest
from tinterruptionProcessor import InterruptionProcessorTest
from tkernel import KernelTest
from tpriorityQueue import PriorityQueueTest
from tmainmemory import MainMemoryTest
from troutines import RoutinesTest
from tnewroutine import NewRoutineTest
from tkillroutine import KillRoutineTest


listTests = [ChanceTest,ClockTest,CpuTest,DiscTest,FifoQueueTest,InterruptionHandlerTest,
InterruptionProcessorTest,KernelTest,PriorityQueueTest, MainMemoryTest, RoutinesTest, 
NewRoutineTest, KillRoutineTest]

for test in listTests:
	suite = unittest.TestLoader().loadTestsFromTestCase(test)
	unittest.TextTestRunner(verbosity=2).run(suite) 
