from colorama import Fore, Back, Style, init
from funcs import typefile, compfile, clear

init()

print(Fore.GREEN + "\n1. Создать новый файл \n2. Скомпилировать скрипт" + Style.RESET_ALL)
do = input("\nВыберите действие >> ")
clear()

if do == "1":
	typefile()
elif do == "2":
	compfile()
else:
	exit()