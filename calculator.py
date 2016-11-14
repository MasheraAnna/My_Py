# -*- coding: utf-8 -*-
import re

print("Это калькулятор. Напиши то, что хочешь посчитать, поставь равно и отправь сообщение")
msg = input()


goodAnswer = False


while goodAnswer == False:
	try:
		msg = msg.replace(" ", "")
		msg = msg.replace(",", ".")
		if msg.endswith('=') == False:
			print ('В конце строки должен быть знак "="')
			msg = input()
		else:
			msg = msg[:-1]
			if bool(re.match('=', msg)) == True:
				print('В строке должно быть только один знак =')
				msg = input()
			else:
				if bool(re.match('[\d(+/*)/./-]+$', msg)) == False:
					print ('В строке должны быть только цифры или знаки + - / * =')
					msg = input()
				else:
					signs = re.compile('[(+/*)/-]')
					if bool(signs.search(msg)) == False:
						print('В стороке должны быть знаки действий')
						msg = input()
					else:
						answer = eval(msg)
						print(answer)
						goodAnswer = True
						print ('Good input')
	except SyntaxError: 
		print("Какая-то ошибка. Проверь, пожалуйста!")
		msg = input()
	except ZeroDivisionError:
		print("На ноль делить нельзя!")
		msg = input()


# добавить справку по команде /help_calculator
