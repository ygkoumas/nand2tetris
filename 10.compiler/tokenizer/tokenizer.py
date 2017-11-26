import re
from tokens import tokens, token_types

def init(jack_code):
	global JACK_CODE
	JACK_CODE = jack_code

def run():
	remove_comments()
	escape_string_spaces()
	add_spaces()
	split_tokens()
	get_token_type()
	tag_tokens()

def remove_comments():
	global JACK_CODE
	JACK_CODE = re.sub('//.*\n|/\*.*\*/', ' ', JACK_CODE)

def escape_string_spaces():
	global JACK_CODE
	jc = list(JACK_CODE)
	string_state = 'end'
	for i in range(len(jc)):
		if jc[i] == '"':
			if string_state == 'end':
				string_state = 'begin'
			else:
				string_state = 'end'
		elif string_state == 'begin' and jc[i] == ' ':
			jc[i] = '\s'
	JACK_CODE = ''.join(jc)

def add_spaces():
	global JACK_CODE
	for i in tokens['symbol']:
		JACK_CODE = JACK_CODE.replace(i, ' {} '.format(i))

def split_tokens():
	global JACK_CODE
	JACK_CODE = JACK_CODE.split()

def get_token_type():
	global JACK_CODE, TOKENIZED_LIST
	JACK_CODE = map(_get_token_type, JACK_CODE)
	TOKENIZED_LIST = JACK_CODE

def _get_token_type(token):
	for token_type in token_types:
		# TODO HANDLE CHARACTERS
		if token in tokens[token_type]:
			if token_type == 'stringConst':
				token = token[1:-1]
			return token_type, token

def tag_tokens():
	global TOKENIZED_LIST
	TOKENIZED_LIST = map(lambda x: _tag_tokens(x[0], x[1]), JACK_CODE)
	TOKENIZED_LIST = '\n'.join(TOKENIZED_LIST)

def _tag_tokens(token_type, token):
	return '<{0}>{1}</{0}>'.format(token_type, token)

def get_jack_code():
	return JACK_CODE

def get_tokenized_list():
	return TOKENIZED_LIST
