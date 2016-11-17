import re

from1to9 = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
dic1to9 = {}
for index, string in enumerate(from1to9):
	dic1to9 [string] = (index+1)

from1to9R = ["одного", "двух", "трех", "четырех", "пяти", "шести", "семи", "восеми", "девяти"]
dic1to9R = {}
for index, string in enumerate(from1to9R):
	dic1to9R [string] = (index+1)

from1to9D = ["одному", "двум", "трем", "четырем", "пяти", "шести", "семи", "восьми", "девяти"]
dic1to9D = {}
for index, string in enumerate(from1to9D):
	dic1to9D [string] = (index+1)

dic1to9.update ({"одна":1, "две":2})
dic1to9.update (dic1to9R)
dic1to9.update (dic1to9D)


from10to19 = [ "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
dic10to19 = {}
for index, string in enumerate(from10to19):
	dic10to19 [string] = (index+10)

from10to19R = [ "десяти", "одиннадцати", "двенадцати", "тринадцати", "четырнадцати", "пятнадцати", "шестнадцати", "семнадцати", "восемнадцати", "девятнадцати"]
dic10to19R = {}
for index, string in enumerate(from10to19R):
	dic10to19R [string] = (index+10)

dic10to19.update(dic10to19R)



from20to90 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
dic20to90 = {}
for index, string in enumerate(from20to90):
	dic20to90 [string] = ((index+2)*10)

from20to90R = ["двадцати", "тридцати", "сорока", "пятидесяти", "шестидесяти", "семидесяти", "восьмидесяти", "девяноста"]
dic20to90R = {}
for index, string in enumerate(from20to90R):
	dic20to90R [string] = ((index+2)*10)
dic20to90.update(dic20to90R)


hundreds = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"] 
dic100s = {}
for index, string in enumerate(hundreds):
	dic100s [string] = ((index+1)*100)

hundredsR = ["ста", "двухсот", "трехсот", "четырехсот", "пятисот", "шестисот", "семьисот", "восьмисот", "девятисот"] 
dic100sR = {}
for index, string in enumerate(hundredsR):
	dic100sR [string] = ((index+1)*100)

hundredsD = ["стам", "двумстам", "тремстам", "четыремстам", "пятистам", "шестистам", "семистам", "восемистам", "девятистам"] 
dic100sD = {}
for index, string in enumerate(hundredsR):
	dic100sD [string] = ((index+1)*100)

dic100s.update(dic100sR)
dic100s.update(dic100sD)



scales = {"тысяча":"1000", "миллион":"1000000", "миллиард":"1000000000", "трилион":"1000000000000"}
thousands = {"тысяча":"1000", "тысячам":"1000", "тысяч":"1000", "тысячи":"1000", "тысячу":"1000"}
millions = {"миллион":"1000000", "миллионам":"1000000", "миллиона":"1000000", "миллионов":"1000000", "милион":"1000000"}
billions = {"миллиард":"1000000000", "миллиардам":"1000000000", "миллиарда":"1000000000", "миллиардов":"1000000000", "милиард":"1000000000",}
trillions = {"триллион":"1000000000000", "триллионам":"1000000000000",  "триллиона":"1000000000000", "триллионов":"1000000000000", "трилион":"1000000000000",}

classesList = []
classesList.insert(1000000000000, trillions)
classesList.insert(1000000000, billions)
classesList.insert(1000000, millions)
classesList.insert(1000, thousands)


actions1 = {"прибавить": "+", "прибавь": "+", "плюс":"+", "минус":"-", "умножь":"*", "умножьте":"*", "умножить":"*", "сложи":"+", "сложить":"+", "сложите":"+"}
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

# Еще нужно обработать ошибки - try/catch - подумать, какие типы ошибок бывают
# написать тестики?)

# вот эта функция удаляет все лишние слова, кроме числительных и действий
def clean_input (inpList, allLists):
	cleanInputList = []
	for value in inpList :
		if value in allLists :
			cleanInputList.append(value)
	return (cleanInputList)

# вот это еще одна функция - она выбирает из текста действия и убирает их в массив
def fetch_operations (cleanInputList, allActions):
	operations = []
	for index, sign in enumerate(cleanInputList): 
		if sign in allActions:
			operations.append(allActions[sign])
	return (operations)


def split_on(what, delimiter = None):
    splitted = [[]]
    for item in what:
        if item == delimiter:
            splitted.append([])
        else:
            splitted[-1].append(item)
    return splitted

 

def transform_words_to_numbers(classesList, number, allNumbers):
	classMultipl=1
	result=0
	allNumbersList = {}
	for item in classesList:
		allNumbersList.update(item)

	while number != False:
		#проверим, есть ли названия разрядов в числительном	
		classInNumber = False
		for index, value in allNumbersList.items() :
			if index in number :
				classInNumber = True
		
		# если название разряда есть, определим, какие именно указатели разрядов есть в числительном
		if classInNumber == True :
			for numlist in classesList :
				for numName in numlist :
					if numName in number :
						numsplit = split_on(number, numName)

						if numsplit[0] :
								# numsplit[0] "Переводим в цифры, если сущестует, разряд": numName"
								for num in numsplit[0] :
									result = result + int(allNumbers[num])*int(numlist[numName])
						else:
							#"Если не существует, но есть название разряда, то будем считать, что количество равно 1"
							result = result + int(numlist[numName])
						
						number = numsplit[1]
						# number, "отправляем на сл круг"
		else:
			for num in number :
				result = result + int(allNumbers[num])*classMultipl
			number = False

	return result


inp = 'start!'

print ("Привет! Я словарный калькулятор. Если ты напишешь числа и действия словами, я посчитаю результат.")
while len(inp) != 0 :
	print ("Напиши, пожалуйста, то, что нужно посчитать.")
	inp = input()
	# удалим все специальные символы
	inp = re.sub('[^A-Za-zА-Яа-я ]+', '', inp)
			
	# разобьем текст на список через пробел и удалим все лишние слова
	inpList = inp.split(" ")

	# удалим все слова, кроме числительных и действий
	cleanInputList = clean_input (inpList, allLists)	

	print ('Проверим, правильно ли написаны слова. Я покажу тебе текст, если это то, что ты хочешь посчитать - ответь "да"')
	print ("Ты хочешь вычислить:", " ".join(cleanInputList))
	agree = input()
	if agree != "да":
		continue 

	# выпишем все действия в отдельный массив
	operations = fetch_operations (cleanInputList, allActions)

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
	
	# удалим пустые ячейки из списка с числительными
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

	# преврати number1 и number2 в числа
	num2 = transform_words_to_numbers(classesList, twoDigits[1], allNumbers)
	num1 = transform_words_to_numbers(classesList, twoDigits[0], allNumbers)
	
	# вычислим
	print (num1)
	print (num2)
	a = str(num1) + " ".join(operations) + str(num2)
	answer = eval(a)
	print ("Ответ:", answer)
	inp = []