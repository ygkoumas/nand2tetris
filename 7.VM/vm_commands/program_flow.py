import function_calling

def get_label_prefix():
	return function_calling.FUNCTION_STACK[-1]

def c_label(label_name):
	lp = get_label_prefix()
	return '({}${})'.format(lp, label_name)

def c_goto(label_name):
	lp = get_label_prefix()
	result = '''\
@{}${}
0;JMP'''
	return result.format(lp, label_name)

def c_if_goto(label_name):
	lp = get_label_prefix()
	result = '''\
@SP
AM=M-1
D=M
M=0
@{}${}
D;JNE'''
	return result.format(lp, label_name)
