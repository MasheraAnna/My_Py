# -*- coding: utf-8 -*-
import re

print("Если хочешь посчитать, сколько слов во фразе - напиши ее в кавычках!")
msg = input()

# Проверим, есть ли в этой фразе кавычки, открывающие и закрывающие
# вот эту фигню нужно же в цикле while написать?

goodAnswer = False

while goodAnswer == False :
	if len(re.findall("\'", msg)) == 2 and len(re.findall("\"", msg)) == 0 : 
		goodAnswer = re.split ('\'', msg)
	elif len(re.findall("\"", msg)) == 2 and len(re.findall("\'", msg)) == 0 :
		goodAnswer = re.split ('\"', msg)
	else :
		print("Я запутался, используй две одинаковые кавычки, пожалуйста, и не больше!")
		msg = input()

# Перевод в нижний регистр
string = goodAnswer[1].lower()
# Количество слов узнаем
p = '([a-zA-Zа-яА-Я]+)'
words = re.findall(p,string)
string_count = str(len(words))

if string_count.endswith ('1') :
	print ('В этой фразе %s слово' % string_count)
elif string_count.endswith('2') or string_count.endswith('3') or string_count.endswith('4') :
	print ('В этой фразе %s слова' % string_count)
else :
	print ('В этой фразе %s слов' % string_count) 