from colorama import Fore, Back, Style, init
from os import path, system
import time

init()

def clear():
	system("cls")

def typefile():
	clear()
	file_path = input(Fore.GREEN + "Создание файла (пожалуйста, введите имя файла): " + Style.RESET_ALL)
	file_path = path.abspath("workspace/" + file_path.strip())

	if path.exists(file_path):
		clear()
		print(Fore.RED + "Файл уже существует!")
		time.sleep(3)
		
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
	time.sleep(3)

	line_count = 1
	system("color 1f")
	clear()

	while line_count > 0:
		try:
			line = input(str(line_count) + " ")
			file.write(line)
			file.write('\n')
			line_count += 1

		except KeyboardInterrupt:
			clear()
			print(Fore.YELLOW + "Закрытие..." + Style.RESET_ALL)
			system("color")
			clear()
			break

	file.close()

def compfile():
	filename = input(Fore.GREEN + "Компиляция файла (пожалуйста, введите имя файла): " + Style.RESET_ALL)

	if filename.strip() == "":
		clear()
		system("java -cp Compiler.jar com.de4oult.soda.Main script.sc")
		print(str(absolute))
	elif ".sc" not in filename.lower():
		clear()
		system("java -cp Compiler.jar com.de4oult.soda.Main " + str("workspace/" + filename.strip() + ".sc"))
	else:
		clear()
		system("java -cp Compiler.jar com.de4oult.soda.Main " + str("workspace/" + filename.strip()))
