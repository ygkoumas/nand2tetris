import re

class SymbolProcessor:
	'''convert symbolic assembly to assembly without symbols'''
	def __init__(self, shared_data):
		self.shared_data = shared_data
		self.symbol_table = SymbolTable()

	def run(self):
		self.find_all_symbols()
		self.remove_labels()
		self.replace_symbols()

	def find_all_symbols(self):
		labels = 0
		next_address = 16
		enumerate_instractions = enumerate(self.shared_data.io_file)
		for index, value in enumerate_instractions:
			if '(' in value:
				symbol = re.sub('[()]', '', value)
				if not self.symbol_table.contains(symbol):
					self.symbol_table.add_symbol(symbol, index - labels)
					labels += 1
		enumerate_instractions = enumerate(self.shared_data.io_file)
		for index, value in enumerate_instractions:
			if '@' in value:
				symbol = re.sub('@', '', value)
				if not (self.symbol_table.contains(symbol) or symbol.isdigit()):
					self.symbol_table.add_symbol(symbol, next_address)
					next_address += 1


	def remove_labels(self):
		self.shared_data.symbol_processor = [instraction for instraction  in self.shared_data.io_file if not '(' in instraction]

	def replace_symbols(self):
		enumerate_instractions = enumerate(self.shared_data.symbol_processor)
		for index, value in enumerate_instractions:
			if '@' in value:
				symbol = re.sub('@', '', value)
				if not symbol.isdigit():
					self.shared_data.symbol_processor[index] = '@'+str(self.symbol_table.get_address(symbol))



class SymbolTable:
	'''Map of the symbols to numbers'''
	def __init__(self):
		self.symbols = {
			'SP': 0,
			'LCL': 1,
			'ARG': 2,
			'THIS': 3,
			'THAT': 4,
			'R0': 0,
			'R1': 1,
			'R2': 2,
			'R3': 3,
			'R4': 4,
			'R5': 5,
			'R6': 6,
			'R7': 7,
			'R8': 8,
			'R9': 9,
			'R10': 10,
			'R11': 11,
			'R12': 12,
			'R13': 13,
			'R14': 14,
			'R15': 15,
			'SCREEN': 0x4000,
			'KBD': 0x600
		}

	def add_symbol(self, symbol, address):
		self.symbols[symbol] = address

	def contains(self, symbol):
		return symbol in self.symbols

	def get_address(self, symbol):
		return self.symbols[symbol]

