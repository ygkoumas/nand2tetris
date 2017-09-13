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
	return 'vm-arithmetic-boolean-commands-LABEL_{}'.format(label_num)

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
