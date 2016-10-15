class IOFile:
	'''conversts files to arrays and the opposite'''
	def __init__(self, shared_data):
		self.shared_data = shared_data

	def file_to_array(self):
		fo = open(self.shared_data.input_file_name, 'r')
		self.shared_data.io_file = fo.readlines()
