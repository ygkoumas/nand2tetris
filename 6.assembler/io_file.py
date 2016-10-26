import re

class IOFile:
	'''conversts files to arrays and the opposite'''
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def file_to_array(self):
		fo = open(self.shared_data.input_file_name, 'r')
		file_list = map(lambda line: re.sub('[\s\t\n]|\/\/.*', '', line), fo.readlines())
		self.shared_data.io_file = filter(lambda line: True if line != '' else False, file_list)

	def array_to_file(self):
		file_name = self.shared_data.io_file.replace('asm', 'hack')
		fo = open(file_name, 'w')
		fo.write('\n'.join(self.shared_data.code))
		fo.close()
