from vm_commands import arithmetic_boolean as vmc_ab
from vm_commands import memory_access as vmc_ma
from vm_commands import program_flow as vmc_pf
from vm_commands import function_calling as vmc_fc
from vm_commands.__init__ import init as vmc_init

class CodeWriter:
	def __init__(self, shared_data):
		self.is_asm = False
		self.shared_data = shared_data

	def run(self):
		vmc_init(self.shared_data.input_file_name.replace('\.vm', ''))
		self.shared_data.code_writer = map(self._run, self.shared_data.parser)

	# pi for parsed-instruction
	def _run(self, pi):
		if pi[0] == '<asm>':
			self.is_asm = True
			return ''
		elif pi[0] == '</asm>':
			self.is_asm = False
			return ''
		elif self.is_asm:
			return ''.join(pi)

		return vm_commands_map[pi[0]](*pi[1:])

vm_commands_map = {}
arithmetic_boolean_commands = {
	'add' : vmc_ab.c_add,
	'sub' : vmc_ab.c_sub,
	'eq' : vmc_ab.c_eq,
	'gt' : vmc_ab.c_gt,
	'lt' : vmc_ab.c_lt,
	'and' : vmc_ab.c_and,
	'or' : vmc_ab.c_or,
	'not' : vmc_ab.c_not,
	'neg' : vmc_ab.c_neg,
}
vm_commands_map.update(arithmetic_boolean_commands)

memory_access_commands = {
	'push' : vmc_ma.c_push,
	'pop' : vmc_ma.c_pop,
}
vm_commands_map.update(memory_access_commands)

program_flow_commands = {
	'label' : vmc_pf.c_label,
	'goto' : vmc_pf.c_goto,
	'if-goto' : vmc_pf.c_if_goto,
}
vm_commands_map.update(program_flow_commands)

function_calling_commands = {
	'function' : vmc_fc.c_function,
	'call' : vmc_fc.c_call,
	'return' : vmc_fc.c_return,
}
vm_commands_map.update(function_calling_commands)
