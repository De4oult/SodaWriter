from colorama import Fore, Style, init
from configurator import commands, errors

import platform
import os

init()

system = platform.system().lower()

def clear():
	os.system(commands[system][0])

def absolute(file):
	if ".soda" not in file.strip().lower():
		file = file + ".soda"
	file = os.path.abspath(file)
	return file

def exist(file):
	return os.path.exists(file)

def error(errType, num):
	print(Fore.RED + errors[errType][num] + Style.RESET_ALL)

def comp(file):
	os.system(commands[system][1] + str(file))