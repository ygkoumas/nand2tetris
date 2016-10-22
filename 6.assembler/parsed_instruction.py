# instructions have the following form
# A-command: "@number"
# C-command: "dest=comp;jump" where "dest=" and ";jump" are optional

class ParsedInstruction:
	def __init__(self, number='', dest='', comp='', jump=''):
		self.number = number
		self.dest = dest
		self.comp = comp
		self.jump = jump
