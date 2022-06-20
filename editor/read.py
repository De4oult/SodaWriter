from funcs import absolute, exist, error, clear
from editor.syntaxparser import parseread

def read(file):
	file = absolute(file)
	clear()
	if exist(file):
		parseread(file)
	else:
		print(error("file", 0))