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


listTests = [ChanceTest,ClockTest,CpuTest,DiscTest,FifoQueueTest,InterruptionHandlerTest,InterruptionProcessorTest,KernelTest,PriorityQueueTest]

for test in listTests:
	suite = unittest.TestLoader().loadTestsFromTestCase(test)
	unittest.TextTestRunner(verbosity=2).run(suite) 
