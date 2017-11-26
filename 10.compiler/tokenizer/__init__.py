import tokenizer

def tokenize(jack_code, xml_format=False):
	tokenizer.init(jack_code)
	tokenizer.run()
	if xml_format:
		return tokenizer.get_tokenized_list()
	else:
		return tokenizer.get_jack_code()
