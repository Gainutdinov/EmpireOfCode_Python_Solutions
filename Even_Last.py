def even_last(array):
	#print(len(array), array[0])
	expression=0
	if len(array)==0:
		return 0
	else:
		for i in (array[::2]):
			if i==array[0]:
				print("Zero!")
				#print(i)
				expression+=i
			else:
				expression+=i
		expression=expression*array[len(array)-1]
		#print(expression)
		return expression

#even_last([0, 1, 2, 3, 4, 5])
#even_last([1, 3, 5])
#even_last([6])
even_last([])