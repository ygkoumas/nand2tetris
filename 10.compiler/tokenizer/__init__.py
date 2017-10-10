import tokenizer

def tokenize(jack_code):
	tokenizer.init(jack_code)
	tokenizer.run()
	return tokenizer.get_jack_code()
