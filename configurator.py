from os import path

dir = path.dirname(__file__)
helpMessage = open((dir + '/help.conf'), 'r')

commands = {
	"windows" : ["cls", f"java -jar {dir}/Compiler.jar com.de4oult.soda.Main "],
	"linux" : ["clear", f"sudo java -cp {dir}/Compiler.jar com.de4oult.soda.Main "]
}

errors = {
	"args" : [
		helpMessage.read(),
		"Ошибка аргумента! Вы указали только один аргумент!",
		"Ошибка аргумента! Вы указали неверный аргумент!"
	],
	"file" : [
		"Ошибка файла! Файл с таким названием не существует!"
	],
}

answers = {
	"yes" : ("yes", "y", "да", "д"),
	"no" : ("no", "n", "нет", "н")
}