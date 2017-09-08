import os
import re

class IOFile:
	'''converts input file.vm to array and processed array to output file.asm'''
	def __init__(self, shared_data):
		self.shared_data = shared_data
		self.output_file_name = self.shared_data.input_folder_name + '.asm'
		os.system('rm {}'.format(self.output_file_name))

	def file_to_array(self):
		file_path = '{}/{}'.format(self.shared_data.input_folder_name, self.shared_data.input_file_name)
		with open(file_path, 'r') as fo:
			raw_file_list = fo.readlines()
		file_list = map(lambda line: re.sub('[\t\n]|\/\/.*', ' ', line), raw_file_list)
		file_list = map(lambda line: re.sub('\s\s', ' ', line), file_list)
		self.shared_data.io_file = filter(lambda line: line != '' and line !=' ', file_list)

	def array_to_file(self):
		with open(self.output_file_name, 'a') as fo:
			fo.write('\n'.join(self.shared_data.code_writer))
