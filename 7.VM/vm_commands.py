basic_arithmetic = '''\
@SP
AM=M-1
D=M
M=0
A=A-1\
'''

label_num = -1
def make_label():
	global label_num
	label_num += 1
	return 'LABEL' + str(label_num)

def c_add():
	result = basic_arithmetic + '\nM=D+M'
	return result

def c_sub():
	result = basic_arithmetic + '\nM=M-D'
	return result

def c_eq():
	return __c_comp('JEQ')

def c_gt():
	return __c_comp('JGT')

def c_lt():
	return __c_comp('JLT')

def __c_comp(comp):
	label = make_label()
	compare = '\nD=M-D'+\
		'\nM=-1'+\
		'\n@'+label+\
		'\nD;'+comp+\
		'\n@SP'+\
		'\nA=M-1'+\
		'\nM=0'+\
		'\n('+label+')'

	result = basic_arithmetic + compare
	return result

def c_and():
	result = basic_arithmetic + '\nM=M&D'
	return result

def c_or():
	result = basic_arithmetic + '\nM=M|D'
	return result

def c_not():
	result = '''\
@SP
A=M-1
M=!M\
'''
	return result

def c_neg():
	result = '''\
@SP
A=M-1
M=-M\
'''
	return result


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
		result = '@filename.' + number +\
			'\nD=M\n' +\
			push

	elif segment == 'temp':
		result = '@'+str(int(number) + 5) +\
			'\nD=M\n' +\
			push
	elif segment == 'pointer':
		address = '@THIS' if int(number) == 0 else '@THAT'
		result = address +\
			'\nD=M\n' +\
			push
	else:
                result = '@' + number +\
                        '\nD=A' +\
                        '\n@'+segment_map[segment] +\
                        '\nA=M+D' +\
                        '\nD=M\n' +\
			push

	return result

def c_pop(segment, number):
	pop = '''
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
		result = '@filename.' + number +\
			'\nD=A\n' +\
			pop

	elif segment == 'temp':
		result = '@'+str(int(number) + 5) +\
			'\nD=A\n' +\
			pop

	elif segment == 'pointer':
		address = '@THIS' if int(number) == 0 else '@THAT'
		result = address +\
			'\nD=A\n' +\
			pop


	else:
		result = '@'+ number +\
'\nD=A'+\
'\n@'+ segment_map[segment]+\
'\nD=D+M'+\
pop
	return result

segment_map = {
	'static' : '',
	'local' : 'LCL',
	'argument' : 'ARG',
	'this' : 'THIS',
	'that' : 'THAT',
	'temp' : 'TEMP',
	'pointer' : '',
}
