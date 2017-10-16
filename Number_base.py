def convert(str_number, radix):
	listing={
			'0' : 0, '1': 1, '2' : 2, '3': 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7,  '8' : 8,
			'9' : 9, 'A' : 10,  'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15, 'G' : 16,
			'H' : 17, 'I' : 18, 'J' : 19, 'K' : 20, 'L' : 21, 'M' : 22, 'N' : 23, 'O' : 24,
			'P' : 25, 'Q' : 26, 'R' : 27, 'S' : 28, 'T' : 29, 'U' : 30, 'V' : 31, 'W' : 32,
			'X' : 33, 'Y' : 34, 'Z' : 35
			} #dictionary
	inv_str_number=str_number[::-1]
	i=0; fin_val=0
	for value in inv_str_number:
		#print(listing[value])
		if listing[value]>=radix:
			fin_val=-1
			#break
			return -1
		else:
			#	numb=int(value);	print(numb)
			fin_val+=listing[value]*(radix**i)
			i+=1


	#print(fin_val)
	return fin_val


convert("Z", 10)
#str_number1="192A"; radix=10

#print(inv_str_number1[::-1])

#print(len(inv_str_number1))




