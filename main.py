from funcs import typefile, compfile, readfile, clear
from colorama import Fore, Back, Style, init
import sys

init()

#clear()
#print(Fore.GREEN + "1. Создать новый файл \n2. Читать файл \n3. Скомпилировать файл" + Style.RESET_ALL)
#do = input("\nВыберите действие >> ")
#clear()

#if do == "1":
#	typefile()
#elif do == "2":
#	readfile()
#elif do == "3":
#	compfile()
#else:
#	exit()

clear()

helpMes = open('help.conf', 'r')

if len(sys.argv) > 1:
	arg = sys.argv[1].lower()

	if arg == "type":
		typefile()
	elif arg == "read":
		readfile()
	elif arg == "comp":
		compfile()

else:
	print(helpMes.read())