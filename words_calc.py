import re


from1to9 = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
dic1to9 = {}
for index, string in enumerate(from1to9):
	dic1to9 [string] = (index+1)

from10to19 = [ "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
"шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
dic10to19 = {}
for index, string in enumerate(from10to19):
	dic10to19 [string] = (index+10)

from20to90 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
dic20to90 = {}
for index, string in enumerate(from20to90):
	dic20to90 [string] = ((index+2)*10)

hundreds = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятсот"] 
dic100s = {}
for index, string in enumerate(hundreds):
	dic100s [string] = ((index+1)*100)

scales = {"тысяча":"1000", "миллион":"1000000", "миллиард":"1000000000", "трилион":"1000000000000"}

actions1 = {"плюс":"+", "минус":"-", "умножь":"*", "умножьте":"*", "умножить":"*", "сложи":"+", "сложить":"+", "сложите":"+"}
actions2 = {"разделить":"/", "раздели":"/", "разделите":"/"}
actions3 = {"вычти":"-", "вычесть":"-", "вычтите":"-",}

allActions = {}
allActions.update(actions1)
allActions.update(actions2)
allActions.update(actions3)

actionsPreps = {"на":"", "из":"", "и":"", "с":""}


addForms = {"однa":"1", "две":"2", "тысяч":"1000", "тысячи":"1000", "тысячу":"1000", "миллиона":"1000000", "миллионов":"1000000", 
"миллиарда":"1000000000", "миллиардов":"1000000000", "трилиона":"1000000000000", "трилионов":"1000000000000"}

actionsPlusPreps = {}
actionsPlusPreps.update(allActions)
actionsPlusPreps.update(actionsPreps)


allNumbers = {}
allNumbers.update(dic1to9)
allNumbers.update(dic10to19)
allNumbers.update(dic20to90)
allNumbers.update(dic100s)
allNumbers.update(scales)

allLists = {}
allLists.update(allNumbers)
allLists.update(allActions)
allLists.update(actionsPreps)


def find_action (inp, allActionsList):
	actionInText = False
	for action, sign in allActions.items() :
		if action in inp:
			actionInText = True
	return actionInText


inp = 'start!'

while len(inp) != 0 :
	inp = input()
	# удалим все специальные символы
	inp = re.sub('[^A-Za-zА-Яа-я ]+', '', inp)
	
	# разобьем текст на список через пробел и удалим все лишние слова
	inp = inp.split(" ")
	for value in inp :
		if value in allLists :
			print(value) 

	for value in inp :
		if value in actions1:
			print(actions1[value])
			# если найдешь предлог - не парься, не ищи предлог 
		elif value in actions2:
			print(actions2[value])
			# если найдешь предлог - то, что идет после предлога и до действия или до конца - что быстрее наступит - это делитель
			# если не найдешь предлог - ошибка
		elif value in actions3:
			print(actions3[value])
			# если найдешь предлог - то, что после предлога и до действия либо до конца (смотря что быстрее) - уменьшаемое
			# если не найдешь предлог - ошибка



	"""
	inp2 = cut_all_before(inp, allNumbers)
	findAction = find_action (inp2, allActions)
	if 	findAction == True :
		inp = inp2
	else :
		inp2 = cut_all_before(inp, actions)
		findAction = find_action (inp2, allActions)	
		if findAction == True :
			inp = inp2
		else :
			inp3 = cut_all_before(inp2, actionsShort)
			findAction = find_action (inp3, allActions)
			if findAction == True :
				inp = inp3

	print (findAction)
	print (inp)

	
	максимальное число разрядов =  999 999 999 999 999 - триллионов
	разрежем получившееся выражение на 2 части:
	обработать все действия и слово на - заменить их на *
	разбить по этой * в массив
	
	actionsList = []
	for action, sign in actionsPlusProps.items() :	
		while action in inp :
			actionsList.append(sign)
			inp = inp.replace(action, "&")

	for action, sign in actionsShort.items() :	
		while action in inp :
			actionsList.append(sign)
			inp = inp.replace(action, "&")
		
	while '' in actionsList:
		actionsList.remove('')

	if len(actionsList) == 0 :
		print ("Не хватает действия!")
		continue
	elif len(actionsList) > 1 :
		print ("Слишком много действий!")
		continue

	print (inp)
	inp = inp.split("&")

	while '' in inp:
		inp.remove('')
	
	# обрезать пробелы
	num1 = inp.pop()
	
	num2 = inp.pop()
	

	print (num1) 
	print (num2)
	
	# собственно вычисляем:

	a = str(allLists[num2]) + str(actionsList[0]) + str(allLists[num1])
	print (a)
	answer = eval(a)
	print (answer)

	
	

	# если в числительном было одно слово:
	if len(num1) == 1 :
		if num1 in allLists:
			toCalc1 = num1
			print(toCalc1)
		else:
			print("Какая-то ошибка в написании! Проверь, пожалуйста :)")
			inp = input()
			exp = inp.split(' ')
			continue

	elif sign in actions :
		print (actions[sign])
	elif len(num2) == 1 :
		if num2 in allLists:
			toCalc1 = num2
			print(toCalc2)
		else:
			print("Какая-то ошибка в написании! Проверь, пожалуйста :)")
			inp = input()
			exp = inp.split(' ')
			continue
	else :
		print ("Какая-то ошибка в написании! Проверь, пожалуйста :)")
		inp = input()
		exp = inp.split(' ')
		continue

# посмотрим на слудующее числительное:
	# если это scales - то будем умножать следующие числительные на размер этого скейла
	# если это десятки - добавим + размер этого десятка
	# если это сотни - добавим + размер этой сотни

# посмотрим на слудующее числительное:
	# если это scales - то будем умножать следующие числительные на размер этого скейла
	# если это десятки - ошибка
	# если это сотни - добавим + размер этой сотни



# определим, к каком из листов оно относится
"""