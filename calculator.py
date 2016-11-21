# -*- coding: utf-8 -*-
import re

class Calculator:
	def __init__(self):
		self.answer = ''

	def count(self, msg):
		try:
			msg = msg.replace(" ", "")
			msg = msg.replace(",", ".")
			if msg.endswith('=') == False:
				self.answer ='В конце строки должен быть знак "="'
			else:
				msg = msg[:-1]
				if bool(re.match('=', msg)) == True:
					self.answer ='В строке должно быть только один знак ='
				else:
					if bool(re.match('[\d(+/*)/./-]+$', msg)) == False:
						self.answer = 'В строке должны быть только цифры или знаки + - / * ='
					else:
						signs = re.compile('[(+/*)/-]')
						if bool(signs.search(msg)) == False:
							self.answer = 'В стороке должны быть знаки действий'
						else:
							self.answer = eval(msg)
							goodAnswer = True
		except SyntaxError:
			self.answer = "Какая-то ошибка. Проверь, пожалуйста!"
		except ZeroDivisionError:
			self.answer = "На ноль делить нельзя!"

		return self.answer

# добавить справку по команде /help_calculator
