from parsed_instruction import ParsedInstruction

class MachineCodeGenerator:
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def run(self):
		self.shared_data.machine_code_generator = map(self._run, self.shared_data.parser)

	def _run(self, parsed_instruction):
		if  parsed_instruction.number != '':
			number = binary(parsed_instruction.number)
			result = ParsedInstruction(number=number)
		else:
			dest = self.dest(parsed_instruction)
			comp = self.comp(parsed_instruction)
			jump = self.jump(parsed_instruction)
			result = ParsedInstruction(dest=dest, comp=comp, jump=jump)
		return result

	def dest(self, instruction):
		ins_dest = instruction.dest
		d1 = '1' if 'A' in ins_dest else '0'
		d2 = '1' if 'D' in ins_dest else '0'
		d3 = '1' if 'M' in ins_dest else '0'
		return d1+d2+d3

	def jump(self, instruction):
		ins_jump = instruction.jump
		return jump_map[ins_jump] if ins_jump != '' else '000'

	def comp(self, instruction):
		ins_comp = instruction.comp
		AMMuxSel = '1' if 'M' in ins_comp else '0'
		ins_comp = ins_comp.replace('M','A') 
		return AMMuxSel+comp_map[ins_comp]


def binary(n):
	bin_n = _binary(n)
	result = '0'*(16-len(bin_n))+bin_n
	return result

def _binary(n):
	int_n = int(n)
	if int_n == 0:
		return '0'
	else:
		return _binary(int_n/2) + str(int_n%2)

jump_map = dict(
	null = '000',
	JGT = '001',
	JEQ = '010',
	JGE = '011',
	JLT = '100',
	JNE = '101',
	JLE = '110',
	JMP = '111'
)

comp_map= {
	'0' : '101010',
	'1' : '111111',
	'-1' : '111010',
	'D' : '001100',
	'A' : '110000',
	'!D' : '001101',
	'!A' : '110001',
	'-D' : '001111',
	'-A' : '110011',
	'D+1' : '011111',
	'A+1' : '110111',
	'D-1' : '001110',
	'A-1' : '110010',
	'D+A' : '000010',
	'D-A' : '010011',
	'A-D' : '000111',
	'D&A' : '000000',
	'D|A' : '010101',
}

