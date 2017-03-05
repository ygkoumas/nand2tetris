import sys

from shared_data import SharedData

from io_file import IOFile
from parser import Parser
from code_writer import CodeWriter

# get input file name
try:
	input_file_name = sys.argv[1]
except IndexError:
	print('there is no file.asm argument')


shared_data = SharedData(input_file_name)

io_file = IOFile(shared_data)
parser = Parser(shared_data)
code_writer = CodeWriter(shared_data)


io_file.file_to_array()
parser.run()
code_writer.run()
io_file.array_to_file()

