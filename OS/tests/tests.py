import unittest

from tchance import ChanceTest
from tclock import ClockTest
from tcpu import CpuTest
from tdisc import DiscTest
from  tfifoQueue import FifoQueueTest
from tinterruptionHandler HandlerTest
from tinterruptionProcessor import InterruptionProcesorTest
from tkernel import KernelTest
from tpriorityQueue import PriorityQueueTest

listTests = [ChanceTest,ClockTest,CpuTest,DiscTest,FifoQueueTest,HandlerTest,InterruptionProcesorTest,KernelTest,PriorityQueueTest]

for test in range listTests:
	suite = unittest.TestLoader().loadTestsFromTestCase(test)
	unittest.TextTestRunner(verbosity=2).run(suite) 