import re

from parsed_instruction import ParsedInstruction

class Parser:
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def run(self):
		self.shared_data.parser = map(self._run, self.shared_data.symbol_processor)

	def _run(self, instruction):
		if '@' in instruction:
			number = instruction.replace('@','')
			result = ParsedInstruction(number=number)
		else:
			dest = self.dest(instruction)
			comp = self.comp(instruction)
			jump = self.jump(instruction)
			result = ParsedInstruction(dest=dest, comp=comp, jump=jump)
		return result

	def dest(self, instruction):
		return re.sub('=.*', '', instruction) if '=' in instruction else ''

	def jump(self, instruction):
		return re.sub('.*;', '', instruction) if ';' in instruction else ''

	def comp(self, instruction):
		return re.sub('.*=|;.*', '', instruction)

