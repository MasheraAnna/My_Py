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

thousands = {"тысяча":"1000", "тысяч":"1000", "тысячи":"1000", "тысячу":"1000"}
millions = {"миллион":"1000000", "миллиона":"1000000", "миллионов":"1000000"}
billions = {"миллиард":"1000000000", "миллиарда":"1000000000", "миллиардов":"1000000000"}
trillions = {"триллион":"1000000000000",  "триллиона":"1000000000000", "триллионов":"1000000000000"}

allNumbersLists = []
allNumbersLists.insert(0, thousands)
allNumbersLists.insert(1, millions)
allNumbersLists.insert(2, billions)
allNumbersLists.insert(3, trillions)

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
allNumbers.update(thousands)
allNumbers.update(billions)
allNumbers.update(trillions)

allLists = {}
allLists.update(allNumbers)
allLists.update(allActions)
allLists.update(actionsPreps)


def split_on(what, delimiter = None):
    splitted = [[]]
    for item in what:
        if item == delimiter:
            splitted.append([])
        else:
            splitted[-1].append(item)
    return splitted

"""
def transform_words_to_numbers(classesList, number):
		currentClass = classesList.pop()
		for item in classesList:
			if item in numberList:
				numsplit = split_on(num1, item)
				num1thousands = numsplit[0]
				num1units = numsplit[1]
				for num in num1units:
					result = result + allNumbers[num]*1
"""
inp = input()
number = inp.split()
print(number)
"""
print(transform_words_to_numbers(allNumbersLists, number))
"""

def factorial(n):
	if n == 0:
	    return 1
	else:
	    return n * factorial(n - 1)


"""
inp = 'start!'

while len(inp) != 0 :
	inp = input()
	# удалим все специальные символы
	inp = re.sub('[^A-Za-zА-Яа-я ]+', '', inp)
			
	# разобьем текст на список через пробел и удалим все лишние слова
	inpList = inp.split(" ")
	cleanInputList = []
	for value in inpList :
		if value in allLists :
			cleanInputList.append(value) 

	# выпишем все действия в отдельный массив
	operations = []
	for index, sign in enumerate(cleanInputList): 
		if sign in allActions:
			operations.append(allActions[sign])
	# если нет действий - вывести ошибку
	if len(operations) == 0 :
		print ("Не хватает действия!")
		continue
	if len(operations) > 2 :
		print ("Слишком много действий!")
		continue

	# выпишем два числительных :	
	numbersList = []
	for item in cleanInputList :
		if item in allNumbers :
			numbersList.append(item) 
		else :
			numbersList.append("&")
	
	twoDigits = split_on(numbersList, "&")
	
	# удалим пустые
	for item in twoDigits:
		if not item:
			twoDigits.remove(item)


	# проверим: должно быть два числительных, если больше или меньше - ошибка
	if len(twoDigits) !=2 :
		print ("Должно быть два числа, пожалуйста, и введи заново:")
		continue


	# проверь, не нужно ли поменять местами number1 и number2:
	
	st = twoDigits[0]
	firstDigit = st[0]
	firstDigitParts = split_on(cleanInputList, firstDigit)

	for prep in actionsPreps :
		if prep in firstDigitParts[0] and "/" in operations:
			twoDigits.reverse()
		if prep in firstDigitParts[1] and "-" in operations:
			twoDigits.reverse()

	print(twoDigits)

	# преврати number1 и number2 в числа
	num2 = twoDigits.pop()
	num1 = twoDigits.pop()
	result = 0

	# все списки с названиями разрядов записать в список, который передавать в функцию
	# потом из этого списка делать pop
	# тестировать вынутый список
	# кроме этого списка в функцию передавать еще само числительное
	# глубину рекурсии определять автоматически, т.е. повторять функцию, пока в массиве есть разряды

	


	

	
		разбиваем массив по словам "тысяч", "миллионов", "миллиардов", "триллионов", если таки слова встречаются в этом массиве
		

	# если в числительном было одно слово:
		
	if len(num1) == 1 :
		if num1[0] in allNumbers:
			toCalc1 = num1[0]
		else:
			print("Какая-то ошибка в написании! Проверь, пожалуйста :)")
			continue
	
	if len(num2) == 1 :
		if num2[0] in allNumbers:
			toCalc2 = num2[0]
		else:
			print("Какая-то ошибка в написании! Проверь, пожалуйста :)")
			continue
	

	# вычислим
	a = str(allNumbers[toCalc1]) + " ".join(operations) + str(allNumbers[toCalc2])
	print (a)
	answer = eval(a)
	print ("Ответ:", answer)
	"""	