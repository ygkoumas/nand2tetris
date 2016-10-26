class Unparser:
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def run(self):
		self.shared_data.unparser = map(self._run, self.shared_data.machine_code_generator)

	def _run(self, instr):
		if instr.number != '':
			return instr.number
		else:
			return '111' + instr.comp + instr.dest + instr.jump

