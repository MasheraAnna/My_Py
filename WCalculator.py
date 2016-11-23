import re
		
class WordCalc:
	def __init__(self):
		self.from1to9 = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
		self.dic1to9 = {}
		for index, string in enumerate(self.from1to9):
			self.dic1to9 [string] = (index+1)

		self.from1to9R = ["одного", "двух", "трех", "четырех", "пяти", "шести", "семи", "восеми", "девяти"]
		self.dic1to9R = {}
		for index, string in enumerate(self.from1to9R):
			self.dic1to9R [string] = (index+1)

		self.from1to9D = ["одному", "двум", "трем", "четырем", "пяти", "шести", "семи", "восьми", "девяти"]
		self.dic1to9D = {}
		for index, string in enumerate(self.from1to9D):
			self.dic1to9D [string] = (index+1)

		self.dic1to9.update ({"одна":1, "две":2})
		self.dic1to9.update (self.dic1to9R)
		self.dic1to9.update (self.dic1to9D)

		self.from10to19 = [ "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
		self.dic10to19 = {}
		for index, string in enumerate(self.from10to19):
			self.dic10to19 [string] = (index+10)

		self.from10to19R = [ "десяти", "одиннадцати", "двенадцати", "тринадцати", "четырнадцати", "пятнадцати", "шестнадцати", "семнадцати", "восемнадцати", "девятнадцати"]
		self.dic10to19R = {}
		for index, string in enumerate(self.from10to19R):
			self.dic10to19R [string] = (index+10)

		self.dic10to19.update(self.dic10to19R)



		self.from20to90 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
		self.dic20to90 = {}
		for index, string in enumerate(self.from20to90):
			self.dic20to90 [string] = ((index+2)*10)

		self.from20to90R = ["двадцати", "тридцати", "сорока", "пятидесяти", "шестидесяти", "семидесяти", "восьмидесяти", "девяноста"]
		self.dic20to90R = {}
		for index, string in enumerate(self.from20to90R):
			self.dic20to90R [string] = ((index+2)*10)
		self.dic20to90.update(self.dic20to90R)


		self.hundreds = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"] 
		self.dic100s = {}
		for index, string in enumerate(self.hundreds):
			self.dic100s [string] = ((index+1)*100)

		self.hundredsR = ["ста", "двухсот", "трехсот", "четырехсот", "пятисот", "шестисот", "семьисот", "восьмисот", "девятисот"] 
		self.dic100sR = {}
		for index, string in enumerate(self.hundredsR):
			self.dic100sR [string] = ((index+1)*100)

		self.hundredsD = ["стам", "двумстам", "тремстам", "четыремстам", "пятистам", "шестистам", "семистам", "восемистам", "девятистам"] 
		self.dic100sD = {}
		for index, string in enumerate(self.hundredsR):
			self.dic100sD [string] = ((index+1)*100)

		self.dic100s.update(self.dic100sR)
		self.dic100s.update(self.dic100sD)

		self.scales = {"тысяча":"1000", "миллион":"1000000", "миллиард":"1000000000", "трилион":"1000000000000"}
		self.thousands = {"тысяча":"1000", "тысячам":"1000", "тысяч":"1000", "тысячи":"1000", "тысячу":"1000"}
		self.millions = {"миллион":"1000000", "миллионам":"1000000", "миллиона":"1000000", "миллионов":"1000000", "милион":"1000000"}
		self.billions = {"миллиард":"1000000000", "миллиардам":"1000000000", "миллиарда":"1000000000", "миллиардов":"1000000000", "милиард":"1000000000",}
		self.trillions = {"триллион":"1000000000000", "триллионам":"1000000000000",  "триллиона":"1000000000000", "триллионов":"1000000000000", "трилион":"1000000000000",}

		self.classesList = []
		self.classesList.insert(1000000000000, self.trillions)
		self.classesList.insert(1000000000, self.billions)
		self.classesList.insert(1000000, self.millions)
		self.classesList.insert(1000, self.thousands)


		self.actions1 = {"прибавить": "+", "прибавь": "+", "плюс":"+", "минус":"-", "умножь":"*", "умножьте":"*", "умножить":"*", "сложи":"+", "сложить":"+", "сложите":"+"}
		self.actions2 = {"разделить":"/", "раздели":"/", "разделите":"/"}
		self.actions3 = {"вычти":"-", "вычесть":"-", "вычтите":"-",}

		self.allActions = {}
		self.allActions.update(self.actions1)
		self.allActions.update(self.actions2)
		self.allActions.update(self.actions3)

		self.actionsPreps = {"на":"", "из":"", "и":"", "с":""}


		self.addForms = {"однa":"1", "две":"2", "тысяч":"1000", "тысячи":"1000", "тысячу":"1000", "миллиона":"1000000", "миллионов":"1000000", 
		"миллиарда":"1000000000", "миллиардов":"1000000000", "трилиона":"1000000000000", "трилионов":"1000000000000"}

		self.actionsPlusPreps = {}
		self.actionsPlusPreps.update(self.allActions)
		self.actionsPlusPreps.update(self.actionsPreps)


		self.allNumbers = {}
		self.allNumbers.update(self.dic1to9)
		self.allNumbers.update(self.dic10to19)
		self.allNumbers.update(self.dic20to90)
		self.allNumbers.update(self.dic100s)
		self.allNumbers.update(self.scales)
		self.allNumbers.update(self.thousands)
		self.allNumbers.update(self.billions)
		self.allNumbers.update(self.trillions)

		self.allLists = {}
		self.allLists.update(self.allNumbers)
		self.allLists.update(self.allActions)
		self.allLists.update(self.actionsPreps)

	# Еще нужно обработать ошибки - try/catch - подумать, какие типы ошибок бывают
	# написать тестики?)

	# вот эта функция удаляет все лишние слова, кроме числительных и действий
	def clean_input (self, inpList, allLists):
		cleanInputList = []
		for value in inpList :
			if value in allLists :
				cleanInputList.append(value)
		return (cleanInputList)

	# вот это еще одна функция - она выбирает из текста действия и убирает их в массив
	def fetch_operations (self, cleanInputList, allActions):
		operations = []
		for index, sign in enumerate(cleanInputList): 
			if sign in allActions:
				operations.append(allActions[sign])
		return (operations)


	def split_on(self, what, delimiter = None):
	    splitted = [[]]
	    for item in what:
	        if item == delimiter:
	            splitted.append([])
	        else:
	            splitted[-1].append(item)
	    return splitted

	 

	def transform_words_to_numbers(self, classesList, number, allNumbers):
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
							numsplit = self.split_on(number, numName)

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




	def user_check (self, inp):
		# удалим все специальные символы
		inp = re.sub('[^A-Za-zА-Яа-я ]+', '', inp)
		# разобьем текст на список через пробел и удалим все лишние слова
		inpList = inp.split(" ")
		# удалим все слова, кроме числительных и действий
		self.cleanInputList = self.clean_input (inpList, self.allLists)
		answer = 'Проверим, правильно ли написаны слова. Я покажу тебе текст, если это то, что ты хочешь посчитать, ответь "да".\nТы хочешь вычислить:  ' + " ".join(self.cleanInputList)
		return answer

	def check (self, inp):
		# выпишем все действия в отдельный массив
		inp = re.sub('[^A-Za-zА-Яа-я ]+', '', inp)
		inpList = inp.split(" ")
		self.cleanInputList = self.clean_input (inpList, self.allLists)
		self.operations = self.fetch_operations (self.cleanInputList, self.allActions)

		# если нет действий - вывести ошибку
		if len(self.operations) == 0 :
			answer = "Не хватает действия!"
		elif len(self.operations) > 2 :
			answer = "Слишком много действий!"
		else:
			# выпишем два числительных :	
			self.numbersList = []
			for item in self.cleanInputList :
				if item in self.allNumbers :
					self.numbersList.append(item) 
				else :
					self.numbersList.append("&")
			
			self.twoDigits = self.split_on(self.numbersList, "&")
			
			# удалим пустые ячейки из списка с числительными
			for item in self.twoDigits:
				if not item:
					self.twoDigits.remove(item)

			# проверим: должно быть два числительных, если больше или меньше - ошибка
			if len(self.twoDigits) !=2 :
				answer = "Должно быть два числа, пожалуйста проверь, и введи заново:"
			else:
				answer = False
		return answer

	def calc (self):
		# проверь, не нужно ли поменять местами number1 и number2:	
		st = self.twoDigits[0]
		firstDigit = st[0]
		firstDigitParts = self.split_on(self.cleanInputList, firstDigit)
		for prep in self.actionsPreps :
			if prep in firstDigitParts[0] and "/" in self.operations:
				self.twoDigits.reverse()
			if prep in firstDigitParts[1] and "-" in self.operations:
				self.twoDigits.reverse()

		# преврати number1 и number2 в числа
		num2 = self.transform_words_to_numbers(self.classesList, self.twoDigits[1], self.allNumbers)
		num1 = self.transform_words_to_numbers(self.classesList, self.twoDigits[0], self.allNumbers)
		
		# вычислим
		a = str(num1) + " ".join(self.operations) + str(num2)
		answer = eval(a)
		return (answer)