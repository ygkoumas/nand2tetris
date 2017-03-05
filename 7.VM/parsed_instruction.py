class ParsedInstruction:
	def __init__(self, command, segment=None, integer=None):
		self.command = command
		self.segment = segment
		self.integer = integer

commands = [
	'push',
	'pop',
]

