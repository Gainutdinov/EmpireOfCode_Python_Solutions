def count_units(number):
	b_number=(bin(number)[2:])
	int_numb=0
	for i in b_number:
		int_numb+=int(i)
#	print(b_number,int_numb,type(b_number))


	return int_numb

count_units(1022)