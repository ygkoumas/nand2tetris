from vm_commands import arithmetic_boolean as vm_abc
from vm_commands import memory_access as vm_mac
from vm_commands import program_flow as vm_pfc
from vm_commands import function_calling as vm_fcc

class CodeWriter:
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def run(self):
		self.shared_data.code_writer = map(self._run, self.shared_data.parser)

	# pi for parsed-instruction
	def _run(self, pi):
		return vm_commands_map[pi[0]](*pi[1:])

vm_commands_map = {}
arithmetic_boolean_commands = {
	'add' : vm_abc.c_add,
	'sub' : vm_abc.c_sub,
	'eq' : vm_abc.c_eq,
	'gt' : vm_abc.c_gt,
	'lt' : vm_abc.c_lt,
	'and' : vm_abc.c_and,
	'or': vm_abc.c_or,
	'not' : vm_abc.c_not,
	'neg' : vm_abc.c_neg,
}
vm_commands_map.update(arithmetic_boolean_commands)

memory_access_commands = {
	'push' : vm_mac.c_push,
	'pop' : vm_mac.c_pop,
}
vm_commands_map.update(memory_access_commands)
program_flow_commands = {
	'label' : vm_pfc.c_label,
	'goto' : vm_pfc.c_goto,
	'if-goto' : vm_pfc.c_if_goto,
}
vm_commands_map.update(program_flow_commands)

tobeusedlater='''
function_calling_commands = {
	'function' : vm_fcc.c_function,
	'call' : vm_fcc.c_call,
	'return' : vm_fcc.c_return,
}
vm_commands_map.update(function_calling_commands)
'''
