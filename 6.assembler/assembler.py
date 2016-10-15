import sys

from shared_data import SharedData

from io_file import IOFile
#from symbol_process import SymbolProcess
#from parser import Parser
#from code import Code


# get input file name
try:
	input_file_name = sys.argv[1]
except IndexError:
	print('there is no file.asm argument')

# here i should create the data object in order to pass the parameter input_file


shared_data = SharedData(input_file_name)

io_file = IOFile(shared_data)
io_file.file_to_array()

# symbol_process = SymbolProcess(shared_data)


