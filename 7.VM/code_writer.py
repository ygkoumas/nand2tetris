import vm_commands
from parsed_instruction import ParsedInstruction

class CodeWriter:
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def run(self):
		self.shared_data.code_writer = map(self._run, self.shared_data.parser)

	# pi for parsed_instruction
	def _run(self, pi):
		if  pi.command in 'pushpop':
			return vm_comands_map[pi.command](pi.segment, pi.integer)
		else:
			return vm_comands_map[pi.command]()


vm_comands_map = {
	'add' : vm_commands.c_add,
	'sub' : vm_commands.c_sub,
	'eq' : vm_commands.c_eq,
	'gt' : vm_commands.c_gt,
	'lt' : vm_commands.c_lt,
	'and' : vm_commands.c_and,
	'or': vm_commands.c_or,
	'not' : vm_commands.c_not,
	'neg' : vm_commands.c_neg,
	'push' : vm_commands.c_push,
	'pop' : vm_commands.c_pop,
}
