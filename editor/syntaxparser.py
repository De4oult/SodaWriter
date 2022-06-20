#  	type word :: white
#	type "text" :: yellow
#	type operator and nums 123 :: blue
#  	type func() :: cyan
#	type command if/else/while... :: cyan
#	type comments // /**/ :: grey
from colorama import Fore, Style, init
import tokens
import re

init()

def parseread(filename):
	file = open(filename, encoding='utf-8')
	
	operators = '(\s+|//.+|/\*.*|.*\*/|\(|\)|,|;|{|}|[|]|\+|-|\*|/|>=|<=|==|>|<|=|!=|!|&|&&|\||\|\||\".\")'

	document = []

	comments = []

	lineNum = 1
	spacesCount = 1

	#for row in file:
	#	print(" " * 5)
	#	spacesCount += 1

	file.seek(0)
	

	for row in file:
		#if "/*" in row:
		#	comments.append(row) # ["row", ]
		#	for row in file:
		#		commentIndex = len(comments) - 1
		#		if "*/" in row:
		#			comments[commentIndex] = comments[commentIndex] + row
		#			break
		#		else:
		#			comments[commentIndex] = comments[commentIndex] + row

		#print(comments)

		line = re.split(operators, row)
		#print(line)
		line[:] = [x for x in line if x]
		#print(line, end="\n")
		spacesCount = len(str(spacesCount))
				
	
		lineSpace = ' ' * spacesCount
		print(lineNum, end=lineSpace)
		
		if line == []:
			print("")
		else:
						
			for expression in line:
				if expression.lower() in tokens.operators["keywords"]:
					print(Fore.BLUE + str(expression) + Style.RESET_ALL, end="")
				elif expression.lower() in tokens.operators["logical"]:
					print(Fore.MAGENTA + str(expression) + Style.RESET_ALL, end="")	
				elif expression.lower() in tokens.operators["math"]:
					print(Fore.CYAN + str(expression) + Style.RESET_ALL, end="")					
				elif re.fullmatch('\d+|\d+.\d+', expression.lower()):
					print(Fore.CYAN + str(expression) + Style.RESET_ALL, end="")
				elif re.fullmatch('#\w{,6}', expression.lower()):
					print(Fore.CYAN + str(expression) + Style.RESET_ALL, end="")
				else:
					print(expression + Style.RESET_ALL, end="")
		lineNum += 1
			 
	file.close()

def parseeditor(line):
	operators = '(\s+|//.+|/\*.*|.*\*/|\(|\)|,|;|{|}|[|]|\+|-|\*|/|>=|<=|==|>|<|=|!=|!|&|&&|\||\|\||\".\")'

	line = re.split(operators, line)

	parsedExpressions = []
	parsedLine = ""

	for expression in line:
		if expression.lower() in tokens.operators["keywords"]:
			parsedExpressions.append(Fore.BLUE + str(expression) + Style.RESET_ALL)
		elif expression.lower() in tokens.operators["logical"]:
			parsedExpressions.append(Fore.MAGENTA + str(expression) + Style.RESET_ALL)	
		elif expression.lower() in tokens.operators["math"]:
			parsedExpressions.append(Fore.CYAN + str(expression) + Style.RESET_ALL)			
		elif re.fullmatch('\d+|\d+.\d+', expression.lower()):
			parsedExpressions.append(Fore.CYAN + str(expression) + Style.RESET_ALL)
		elif re.fullmatch('#\w{,6}', expression.lower()):
			parsedExpressions.append(Fore.CYAN + str(expression) + Style.RESET_ALL)
		else:
			parsedExpressions.append(expression + Style.RESET_ALL)
	
	for lineEls in parsedExpressions:
		index = parsedExpressions.index(lineEls)
		parsedLine = parsedLine + parsedExpressions[index]

	return parsedLine