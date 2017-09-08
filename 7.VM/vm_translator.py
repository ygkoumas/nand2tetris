#! /usr/bin/env python
import sys
import os
from collections import deque

from shared_data import SharedData

from io_file import IOFile
from parser import Parser
from code_writer import CodeWriter

# get input file name
try:
	input_folder_name = sys.argv[1].replace('/', '')
except IndexError:
	print('there is no folder argument')
vm_files = filter(lambda f :  f.endswith('.vm'), os.listdir(input_folder_name))
vm_files = deque(vm_files)

for f in ['Main.vm', 'Sys.vm']:
	if f in vm_files:
		vm_files.remove(f)
		vm_files.appendleft(f)

shared_data = SharedData(input_folder_name)

io_file = IOFile(shared_data)
parser = Parser(shared_data)
code_writer = CodeWriter(shared_data)

for f in vm_files:
	shared_data.set_input_file_name(f)

	io_file.file_to_array()
	parser.run()
	code_writer.run()
	io_file.array_to_file()
