class IOInputRoutine():

		def __init__(self, aKernel):
			self.kernel = aKernel

		def run(self, aIrq):
			#le saca el pcb al irq
			pcb = aIrq.getPcb()
			self.kernel.getCpu().removePcb()
			otherPcb = self.kernel.getScheduler().getNextPcb()
			self.kernel.getCpu().assignPcb(otherPcb)
			#le dice le pide al kernel el IO y le encola el pcb
			self.kernel.getIO().receivePcb(pcb)