import sys

import tokenizer
import parser

# get input file name
try:
	input_file_name = sys.argv[1]
except IndexError:
	print('there is no file argument')

with open(input_file_name, 'r') as fo:
	jack_code = fo.read()

tokenized_list = tokenizer.tokenize(jack_code, xml_format=False)
parsed_code = parser.parse(tokenized_list, xml_format=True)
print parsed_code
