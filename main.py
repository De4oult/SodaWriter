from editor.compile import compile
from editor.create import create 
from editor.read import read 

from funcs import error, clear

import sys

clear()

commands = [
	"create", # new file
	"read",   # read file
	"comp"    # compile file
]

args = sys.argv

if len(args) >= 3:
	command = args[1].lower()
	file = args[2].lower()

	if command == commands[0]:
		create(file)
	elif command == commands[1]:
		read(file)
	elif command == commands[2]:
		compile(file)
	else:
		error("args", 2)

elif len(args) == 1:
	error("args", 0)
elif args[1] not in commands:
	error("args", 2)
elif len(args) == 2:
	error("args", 1)