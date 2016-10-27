import sys

from shared_data import SharedData

from io_file import IOFile
from symbol_processor import SymbolProcessor
from parser import Parser
from machine_code_generator import MachineCodeGenerator
from unparser import Unparser


# get input file name
try:
	input_file_name = sys.argv[1]
except IndexError:
	print('there is no file.asm argument')


shared_data = SharedData(input_file_name)

io_file = IOFile(shared_data)
symbol_processor = SymbolProcessor(shared_data)
parser = Parser(shared_data)
machine_code_generator = MachineCodeGenerator(shared_data)
unparser = Unparser(shared_data)


io_file.file_to_array()
symbol_processor.run()
parser.run()
machine_code_generator.run()
unparser.run()
io_file.array_to_file()

