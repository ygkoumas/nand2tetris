import re

class IOFile:
	'''converts input file.asm to array and processed array to output file.hack'''
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def file_to_array(self):
		fo = open(self.shared_data.input_file_name, 'r')
		file_list = map(lambda line: re.sub('[\t\n]|\/\/.*', ' ', line), fo.readlines())
		file_list = map(lambda line: re.sub('\s\s', ' ', line), file_list)
		file_list = filter(lambda line: True if line != ' ' and line != '' else False, file_list)
		self.shared_data.io_file = file_list

	def array_to_file(self):
		file_name = self.shared_data.input_file_name.replace('vm', 'asm')
		fo = open(file_name, 'w')
		fo.write('\n'.join(self.shared_data.code_writer))
		fo.close()

