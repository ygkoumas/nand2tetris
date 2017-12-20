import parser

def parse(tokenized_list, xml_format=False):
	parser.init(tokenized_list)
	parser.parse()
	if xml_format:
		parser.get_xml_format()
	return parser.get_parsed_code()
