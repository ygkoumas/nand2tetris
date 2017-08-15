import re

class IOFile:
	'''converts input file.asm to array and processed array to output file.hack'''
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def file_to_array(self):
		fo = open(self.shared_data.input_file_name, 'r')
		file_list = map(lambda line: re.sub('[\s\t\n]|\/\/.*', '', line), fo.readlines())
		self.shared_data.io_file = filter(lambda line: line != '', file_list)

	def array_to_file(self):
		file_name = self.shared_data.input_file_name.replace('asm', 'hack')
		fo = open(file_name, 'w')
		fo.write('\n'.join(self.shared_data.unparser))
		fo.close()

