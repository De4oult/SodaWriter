from colorama import Fore, Back, Style, init
from syntaxparser import parseread
from os import path, system
from editor import editor
import time

init()

def clear():
	#system("cls")  # windows
	system("clear") # linux

def readfile():
	file_path = input(Fore.GREEN + "Чтение файла (пожалуйста, введите имя файла): " + Style.RESET_ALL)
	if "workspace/" not in file_path.strip().lower():
		file_path = path.abspath("workspace/" + file_path.strip())
	if ".soda" not in file_path.strip().lower():
		file_path = path.abspath(file_path.strip() + ".soda")
	clear()
	
	if path.exists(file_path):
		parseread(file_path)

def typefile():
	file_path = input(Fore.GREEN + "Создание файла (пожалуйста, введите имя файла): " + Style.RESET_ALL)
	if ".soda" not in file_path.strip().lower():
		file_path = file_path + ".soda"
	if "workspace/" not in file_path.strip().lower():
		file_path = path.abspath("workspace/" + file_path.strip())

	if path.exists(file_path):
		clear()
		print(Fore.RED + "Файл уже существует!")
		time.sleep(2)
		
		clear()
		ans = input(Fore.YELLOW + "Вы хотите использовать этот файл? (д/н)\n-> ")
		print(Style.RESET_ALL)
		
		if ans.lower() == 'y' or ans.lower() == 'д':
			file = open(file_path, "a")
			
			clear()
			ans = input(Fore.RED + "Вы хотите удалить все содержимое? (д/н)\n-> ")
			print(Style.RESET_ALL)

			if ans.lower() == 'y' or ans.lower() == 'д':
				clear()
				print(Fore.RED + "Удаление содержимого..." + Style.RESET_ALL)
				
				file.seek(0)
				file.truncate()
			else:
				pass
		else:
			exit()
	else:
		clear()
		print(Fore.GREEN + "Создание нового файла..." + Style.RESET_ALL)
		file = open(file_path, "a")

	clear()
	print(Fore.GREEN + "Нажмите ENTER, чтобы начать новую строку.\nНажмите Ctrl + C, чтобы сохранить и закрыть." + Style.RESET_ALL)
	time.sleep(2)

	editor(file)

def compfile():
	filename = input(Fore.GREEN + "Компиляция файла (пожалуйста, введите имя файла): " + Style.RESET_ALL)

	if filename.strip() == "":
		clear()
		system("sudo java -cp Compiler.jar com.de4oult.soda.Main workspace/script.soda")
	elif ".soda" not in filename.lower():
		clear()
		if "workspace/" not in filename.strip().lower():
			filename = path.abspath("workspace/" + filename.strip())
		system("sudo java -cp Compiler.jar com.de4oult.soda.Main " + str(filename.strip() + ".soda"))
	else:
		clear()
		if "workspace/" not in filename.strip().lower():
			filename = path.abspath("workspace/" + filename.strip())
		system("sudo java -cp Compiler.jar com.de4oult.soda.Main " + str(filename.strip()))
