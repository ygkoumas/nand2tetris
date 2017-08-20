class Parser:
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def run(self):
		self.shared_data.parser = map(self._run, self.shared_data.io_file)

	def _run(self, instruction):
		# get the command of the instraction
		instruction_array = instruction.split()
		return instruction_array
