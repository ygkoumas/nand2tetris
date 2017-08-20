label_prefix = 'vm-source-code-LABEL_'
def c_label(label_name):
	return '({}{})'.format(label_prefix, label_name)

def c_goto(label_name):
	result = '''\
@{}{}
0;JMP'''
	return result.format(label_prefix, label_name)

def c_if_goto(label_name):
	result = '''\
@SP
AM=M-1
D=M
M=0
@{}{}
D;JNE'''
	return result.format(label_prefix, label_name)
