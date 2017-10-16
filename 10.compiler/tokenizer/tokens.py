import re

keyword_set = set([
	'class',
	'method',
	'function',
	'constructor',
	'var',
	'static',
	'field',
	'int',
	'boolean',
	'char',
	'void',
	'let',
	'do',
	'if',
	'else',
	'while',
	'return',
	'true',
	'false',
	'null',
	'this',
])

symbol_set = set('{}()[].,;+-*/&|<>=~')

class IntegerConstants:
	def __contains__(self, value):
		try:
			int(value)
			return True
		except ValueError:
			return False

class StringConstants:
	def __contains__(self, value):
		if value[0] == '"' and value[-1] == '"':
			return True
		return False

class Identifiers:
	def __contains__(self, value):
		if not value[0].isdigit() and re.match("^[A-Za-z0-9_-]*$", value):
			return True
		return False

token_types = ['keyword', 'symbol', 'intConst', 'stringConst', 'identifier']

tokens = dict(
	keyword = keyword_set,
	symbol = symbol_set,
	integerConstant = IntegerConstants(),
	stringConstant = StringConstants(),
	identifier = Identifiers(),
)
