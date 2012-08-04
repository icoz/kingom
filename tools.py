
#import * from lang
# tools

def inputNum(string):
	while (True):
		s = input(string)
		try:
			n = int(s)
			return n
		except ValueError as err:
			print ("Неверный ввод! Повторите.")