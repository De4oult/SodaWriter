from editor.syntaxparser import parseeditor
from funcs import clear

def editor(file):
	clear()

	line_count = 1

	lines = []

	while line_count > 0:
		try:
			clear()
			for i in lines:
				print(i, end="\n")
			line = input(str(line_count) + " ")
			lines.append(str(line_count) + " " + parseeditor(line))
			file.write(line)
			file.write('\n')
			line_count += 1

		except KeyboardInterrupt:
			clear()
			break

	file.close()