commands = {
	"windows" : ["cls", "java -jar Compiler.jar com.de4oult.soda.Main "],
	"linux" : ["clear", "sudo java -cp Compiler.jar com.de4oult.soda.Main "]
}

helpMessage = open('help.conf', 'r')

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