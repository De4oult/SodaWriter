from colorama import Fore, Style, init
from os import getlogin

from configurator import answers
from editor.editor import editor
from funcs import absolute, clear, exist

init()

def create(file):
	file = absolute(file)

	if exist(file):
		clear()
		print(Fore.RED + "Файл уже существует!")
		print(Fore.YELLOW + "\nВы хотите удалить все содержимое и \nиспользовать этот файл?\n")
		
		userInput = input(Fore.BLUE + str(getlogin()) + " >> ") 

		if userInput.lower() in answers["yes"]:
			clear()
			file = open(file, "a")

			file.seek(0)
			file.truncate()

			print(Style.RESET_ALL)
		
		else:
			exit()
	else:
		clear()
		file = open(file, 'w+')

	editor(file)