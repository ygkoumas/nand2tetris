import re
from tokens import tokens, token_types

def init(jack_code, curr_index=0):
	global JACK_CODE, CURR_INDEX
	JACK_CODE = jack_code
	CURR_INDEX = curr_index

def run():
	remove_comments()
	add_spaces()
	split_tokens()
	get_token_type()
	tag_tokens()

def remove_comments():
	global JACK_CODE
	JACK_CODE = re.sub('//.*\n|/\*.*\*/', ' ', JACK_CODE)

def add_spaces():
	global JACK_CODE
	for i in tokens['symbol']:
		JACK_CODE = JACK_CODE.replace(i, ' {} '.format(i))

def split_tokens():
	global JACK_CODE
	JACK_CODE = JACK_CODE.split()

def get_token_type():
	global JACK_CODE
	JACK_CODE = map(_get_token_type, JACK_CODE)

def _get_token_type(token):
	for token_type in token_types:
		# TODO HANDLE CHARACTERS
		if token in tokens[token_type]:
			if token_type == 'stringConst':
				token = token[1:-1]
			return token_type, token

def tag_tokens():
	global JACK_CODE
	JACK_CODE = map(lambda x: _tag_tokens(x[0], x[1]), JACK_CODE)
	JACK_CODE = '\n'.join(JACK_CODE)

def _tag_tokens(token_type, token):
	return '<{0}>{1}</{0}>'.format(token_type, token)

def get_jack_code():
	return JACK_CODE
