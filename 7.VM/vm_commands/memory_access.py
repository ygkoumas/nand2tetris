file_name = None
def init(fn):
	global file_name
	file_name = fn

def c_push(segment, number):
	push = '''\
@SP
A=M
M=D
@SP
M=M+1\
'''

	if segment == 'constant':
		result = '@' + number +\
			'\nD=A\n' +\
			push

	elif segment == 'static':
		result = '@{}{}'.format(file_name, number) +\
			'\nD=M\n' +\
			push

	elif segment == 'temp':
		result = '@'+str(int(number) + 5) +\
			'\nD=M\n' +\
			push

	elif segment == 'vmsegment':
		result = '@'+str(int(number) + 13) +\
			'\nD=M\n' +\
			push

	elif segment == 'pointer':
		address = '@THIS' if int(number) == 0 else '@THAT'
		result = address +\
			'\nD=M\n' +\
			push
	else:
		set_var_address = '\nA=M+D'
		if int(number) < 0:
			number = number.replace('-', '')
			set_var_address = '\nA=M-D'
                result = '@' + number +\
                        '\nD=A' +\
                        '\n@'+segment_map[segment] +\
			set_var_address +\
                        '\nD=M\n' +\
			push

	return result

def c_pop(segment, number):
	pop = '''\
@SP
A=M
M=D
A=A-1
D=M
A=A+1
A=M
M=D
@SP
AM=M-1
M=0
A=A+1
M=0'''
	if segment == 'static':
		result = '@{}{}'.format(file_name, number) +\
			'\nD=A\n' +\
			pop

	elif segment == 'temp':
		result = '@'+str(int(number) + 5) +\
			'\nD=A\n' +\
			pop

	elif segment == 'vmsegment':
		result = '@'+str(int(number) + 13) +\
			'\nD=A\n' +\
			pop

	elif segment == 'pointer':
		address = '@THIS' if int(number) == 0 else '@THAT'
		result = address +\
			'\nD=A\n' +\
			pop


	else:
		set_var_address = '\nD=M+D'
		if int(number) < 0:
			number = number.replace('-', '')
			set_var_address = '\nD=M-D'
		result = '@'+ number +\
'\nD=A'+\
'\n@'+ segment_map[segment]+\
set_var_address + '\n'+\
pop
	return result

segment_map = {
	'local' : 'LCL',
	'argument' : 'ARG',
	'this' : 'THIS',
	'that' : 'THAT',
}
