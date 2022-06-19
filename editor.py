from colorama import Fore, Back, Style, init
from syntaxparser import parseeditor
from os import path, system

init()

def clear():
	system("clear")

def editor(file):
	system("clear")

	line_count = 1

	lines = []

	while line_count > 0:
		try:
			clear()
			#print(lines)
			for i in lines:
				print(i, end="\n")
			line = input(str(line_count) + " ")
			lines.append(str(line_count) + " " + parseeditor(line))
			file.write(line)
			file.write('\n')
			line_count += 1

		except KeyboardInterrupt:
			print(Style.RESET_ALL)
			clear()
			print(Fore.YELLOW + "Закрытие..." + Style.RESET_ALL)
			clear()
			break

	file.close()