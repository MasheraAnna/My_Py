# -*- coding: utf-8 -*-
import re

class WordsCounter:
	def __init__(self):
		self.msg = ''
		
	# Проверим, есть ли в этой фразе кавычки, открывающие и закрывающие
	def check_input(self, msg):
		if len(re.findall("\'", msg)) == 2 and len(re.findall("\"", msg)) == 0 : 
			self.goodInput = re.split ('\'', msg)
			state = True
		elif len(re.findall("\"", msg)) == 2 and len(re.findall("\'", msg)) == 0 :
			self.goodInput = re.split ('\"', msg)
			state = True
		else :
			state = False
			self.reply = "Я запутался, используй две одинаковые кавычки, пожалуйста, и не больше!"
		return state

	def count(self):
		# Перевод в нижний регистр
		string = self.goodInput[1].lower()
		# Количество слов узнаем
		w = '([a-zA-Zа-яА-Я]+)'
		words = re.findall (w, string)
		string_count = str(len(words))

		if string_count.endswith ('1') :
			self.answer = 'В этой фразе %s слово' % string_count
		elif string_count.endswith('2') or string_count.endswith('3') or string_count.endswith('4') :
			self.answer = 'В этой фразе %s слова' % string_count
		else :
			self.answer = 'В этой фразе %s слов' % string_count
		return self.answer
