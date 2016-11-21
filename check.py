import WCalculator

wCalculator = WCalculator.WordCalc()

state = "work"
while state == "work":
	msg = input()
	userCheck = wCalculator.user_check(msg)
	print (userCheck)
	
	response = input()
	if response != "да":
		print ("Тогда напиши заново!")
		continue
	else:
		print ("Все в порядке, продолжаем!")

	anyProblems = wCalculator.check()

	if anyProblems != False:
		print(anyProblems)
		continue
	else:
		print ("Все в порядке, продолжаем!")

	result = wCalculator.calc()
	print (result)		
