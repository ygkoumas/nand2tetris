import memory_access
import arithmetic_boolean
import program_flow

FUNCTION_STACK = []
def init(fn):
	global FUNCTION_STACK
	FUNCTION_STACK = [fn]

call_id = 0
def get_call_id():
	global call_id
	call_id += 1
	return str(call_id)

def c_function(function_name, local_variables_int):
	FUNCTION_STACK.append(function_name)

	result = ''#program_flow.c_goto('avoid-function-now')
	result += '\n({})'.format(function_name)
	for i in range(int(local_variables_int)):
		result += '\n'
		result += memory_access.c_push('constant', '0')
	return result

def c_call(function_name, args_int):
	return_label = 'return_label' + get_call_id()

	push_RETURN = memory_access.c_push('constant', return_label)
	push_LCL = memory_access.c_push('temp', '-4')
	push_ARG = memory_access.c_push('temp', '-3')
	push_THIS = memory_access.c_push('temp', '-2')
	push_THAT = memory_access.c_push('temp', '-1')

	update_LCL = '''\
@SP
D=M
@LCL
M=D'''
	update_ARG = '''\
@SP
D=M
@{}
D=D-A
@ARG
M=D\
'''.format(5+int(args_int))

	

	goto_function = '''
@{}
0;JMP\
'''.format(function_name)

	return_here = '({})'.format(return_label)
	result_list = [
		push_RETURN,
		push_LCL,
		push_ARG,
		push_THIS,
		push_THAT,
		update_LCL,
		update_ARG,
		goto_function,
		return_here,
	]
	return '\n'.join(result_list)

def c_return():
	del FUNCTION_STACK[-1]

	save_return_label = memory_access.c_push('local', '-5') + '\n'+\
		memory_access.c_pop('vmsegment', '0')
	save_arg_num = memory_access.c_push('temp', '-4') + '\n'+\
		memory_access.c_push('constant', '5') + '\n'+\
		arithmetic_boolean.c_sub() + '\n'+\
		memory_access.c_push('temp', '-3') + '\n'+\
		arithmetic_boolean.c_sub() + '\n'+\
		memory_access.c_pop('vmsegment', '1')

	push_return_value = memory_access.c_pop('argument', '0')
	set_sp_for_recover = '''\
@LCL
D=M
@SP
M=D'''
	#pop all the values to ....
	pop_THAT = memory_access.c_pop('temp', '-1')
	pop_THIS = memory_access.c_pop('temp', '-2')
	pop_ARG = memory_access.c_pop('temp', '-3')
	pop_LCL = memory_access.c_pop('temp', '-4')

#vmsegment is on 13 register
	set_sp = '''\
@14
D=M
@SP
M=M-D'''

	#return
	goto_caller = '''\
@13
A=M
0;JMP'''

	avoid_func_label = program_flow.c_label('avoid-function')

	result_list = [
		save_return_label,
		save_arg_num,
		push_return_value,
		set_sp_for_recover,
		pop_THAT,
		pop_THIS,
		pop_ARG,
		pop_LCL,
		set_sp,
		goto_caller,
#		avoid_func_label,
	]
	return '\n'.join(result_list)
