parts = input()

def cut_cake (parts):
	try:
		return 1/int(parts)
	except: (ZeroDivisionError, TypeError, ValueError):
		return "С ума сошли?"

piece = cut_cake(parts)
print (piece)