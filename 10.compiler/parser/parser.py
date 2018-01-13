import re

parser_map = {}
token_index = -1

def init(tokenized_list):
	global TOKENIZED_LIST
	TOKENIZED_LIST = tokenized_list

def run():
	parse()
	get_xml_format()

def parse():
	global TOKENIZED_LIST
	next_token()
	TOKENIZED_LIST = _parse('forever')

def next_token():
	global current_token
	global token_index
	token_index += 1
	current_token = TOKENIZED_LIST[token_index]

def prev_token():
	global current_token
	global token_index
	token_index -= 1
	current_token = TOKENIZED_LIST[token_index]

def _parse(closing_token='forever'):
	result = []
	if closing_token == 'once':
		result.extend(parser_map[current_token[1]]())
		try:
			next_token()
		except IndexError:
			pass
		return result

	while current_token[1] != closing_token:
		result.extend(parser_map[current_token[1]]())
		try:
			next_token()
		except IndexError:
			return result
	try:
		next_token()
	except IndexError:
		pass
	return result

def _parse_class():
	result = [('class', [])]
	cls = result[0][1]
	cls.append(('keyword', 'class'))
	next_token()
	cls.append(current_token) # identifier
	next_token()
	cls.append(current_token) # symbol {
	next_token()
	cls.extend(_parse('}'))
	cls.append(('symbol', '}'))
	return result
parser_map['class'] = _parse_class

def _parse_classvardec():
	result = [('varDec', [])] if current_token[1] == 'var' else [('classVarDec', [])]
	vd = result[0][1]
	vd.append(current_token) # var/field/static
	next_token()
	vd.append(current_token) # type
	next_token()
	while current_token[1] != ';':
		vd.append(current_token) # identifier
		next_token()

	vd.append(current_token) # symbol ';'
	return result
parser_map['var'] = _parse_classvardec
parser_map['static'] = _parse_classvardec
parser_map['field'] = _parse_classvardec

def _parse_subroutinedec():
	result = [('subroutineDec', [])]
	sr = result[0][1]
	sr.append(current_token) # function/method/constrictor
	next_token()
	sr.append(current_token) # type or identifier
	next_token()
	sr.append(current_token) # identifier
	next_token()
	sr.append(current_token) # (
	sr.append(('parameterList', []))
	next_token()
	while current_token[1] != ')':
		sr[-1][1].append(current_token)
		next_token()
	sr.append(current_token) # )
	next_token()
	sr.append(('subroutineBody', []))
	sr[-1][1].append(current_token) # {
	next_token()

	while current_token[1] in ['var', 'static', 'field']:
		sr[-1][1].extend(_parse('once')) # vars dec
	sr[-1][1].append(('statements', [])) # statements
	sr[-1][1][-1][1].extend(_parse('}')) # statements
	sr[-1][1].append(('symbol', '}')) # }
	prev_token()
	return result
parser_map['function'] = _parse_subroutinedec
parser_map['method'] = _parse_subroutinedec
parser_map['constructor'] = _parse_subroutinedec

def _parse_while():
	result = [('whileStatement', [])]
	whl = result[0][1]
	whl.append(current_token) # while
	next_token()
	whl.append(current_token) # '('
	next_token()
	whl.extend(_parse_expression(')'))
	next_token() # only _parse goes to the next itself
	whl.append(('symbol', ')')) # )
	whl.append(current_token) # {
	next_token()
	whl.append(('statements', []))
	st =  whl[-1][1]
	st.extend(_parse('}'))
	whl.append(('symbol', '}'))
	prev_token()
	return result
parser_map['while'] = _parse_while

def _parse_do():
	result = [('doStatement', [])]
	d = result[0][1]
	d.append(current_token) # do
	next_token()
	d.append(current_token) # identifier
	next_token()
	while current_token[1] != '(':
		d.append(current_token)
		next_token()
	d.append(current_token) # (
	next_token()
	d.extend(_parse_expressionList())
	d.append(current_token) # symbol )
	d.append(('symbol', ';')) # symbol ';'
	next_token()
	return result
parser_map['do'] = _parse_do

def _parse_let():
	result = [('letStatement', [])]
	lt = result[0][1]
	lt.append(current_token) # let keyword
	next_token()
	while current_token[1] != '=':
		if current_token[1] == '[':
			lt.append(current_token) # symbol '['
			next_token()
			lt.extend(_parse_expression(']'))
			lt.append(current_token)
			next_token()
		else:
			lt.append(current_token) # identifier
			next_token()
	lt.append(current_token) # symbol '='
	next_token()
	lt.extend(_parse_expression(';'))
	lt.append(current_token) # symbol ';'
	return result
parser_map['let'] = _parse_let

def _parse_expressionList():
	result = [('expressionList', [])]
	exl = result[0][1]
	if current_token[1] == ')':
		return result
	exl.extend(_parse_expression(',)'))
	while current_token[1] == ',':
		exl.append(current_token)
		next_token()
		exl.extend(_parse_expression(',)'))
	return result

def _parse_expression(closing_tokens=');'):
	symbol_stack = [[]]
	result = [('expression', [])]
	ex = result[0][1]
	while current_token[1] in symbol_stack[-1] or current_token[1] not in closing_tokens:
		if current_token[1] in symbol_stack[-1]:
			ex.append(current_token)
			del symbol_stack[-1]
			next_token()
		elif current_token[1] == '~':
			ex.append(('term', []))
			trm = ex[-1][1]
			trm.append(current_token)
			next_token()
			trm.extend(_parse_term(closing_tokens))
		elif current_token[0] == 'symbol':
			ex.append(current_token)
			if current_token[1] == '(':
				symbol_stack.append(')')
			next_token()
		else:
			ex.extend(_parse_term(closing_tokens))
	return result

def _parse_term(closing_tokens=')'):
	result = [('term', [])]
	ex = result[0][1]
	while current_token[1] not in closing_tokens:
		if current_token[1] in {'<','=','>','-','+','/','|'}:
		#	prev_token()
			return result
		elif current_token[0] in {'stringConstant', 'integerConstant', 'identifier', 'keyword'} \
			or current_token[1] == '.':
			ex.append(current_token)
		elif current_token[1] == '(':
			ex.append(current_token)
			next_token()
			ex.extend(_parse_expressionList())
			ex.append(current_token)
			next_token()
			return result
		elif current_token[1] == '[':
			ex.append(current_token)
			next_token()
			ex.extend(_parse_expression(']'))
			ex.append(current_token)
			next_token()
			return result
		next_token()
	return result

def _parse_return():
	result = [('returnStatement', [])]
	rs = result[0][1]
	rs.append(current_token) # return
	next_token()
	if current_token[1] == ';':
		rs.append(current_token) # symbol ';'
	else:
		rs.extend(_parse_expression(';'))
		rs.append(('symbol', ';')) # symbol ';'
	return result
parser_map['return'] = _parse_return

def get_xml_format():
	global TOKENIZED_LIST
	TOKENIZED_LIST = _get_xml_format(TOKENIZED_LIST)

def _get_xml_format(code_tree):
	result = ''
	for element in code_tree:
		if type(element[1]) is str:
			result += '<{0}>{1}</{0}>\n'.format(element[0], _escape_xml_symbols(element[1]))
		elif type(element[1]) is list:
			result += '<{0}>\n{1}</{0}>\n'.format(element[0], _get_xml_format(element[1]))
	return result

def _escape_xml_symbols(word):
	word = word.replace('<', '&lt;')
	word = word.replace('>', '&gt;')
	return word

def get_parsed_code():
	return TOKENIZED_LIST

