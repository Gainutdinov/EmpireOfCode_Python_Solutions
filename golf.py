def golf(broken_report):
	broken_listing = broken_report.split (',')
	print(broken_listing)
	for word in broken_listing:
		print(word)
		iterator=0
		for j in list(word):
			print(j+1)
			#first_letter=j;second_letter=j+1
			#print(first_letter, '+', second_letter)

	'''sum_ingots=0
	listing = report.split (',');
	x = {}
	ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	prev=0
	for letter in ascii_uppercase:
		for i in range(1,10):
			prev+=1
			x[str(letter)+str(i)]=prev
	for element in listing:
		sum_ingots+= x[element]
	print(sum_ingots)'''

	return 1

golf("ASDA1,BB22D01C1") == 31
#golf("A1,B2,C1") == 31

# if __name__ == '__main__':
#	# These "asserts" using only for self-checking and not necessary for auto-testing
#	assert golf("ASDA1,BB22D01C1") == 31
#	assert golf("B1,C2,D3") == 60
#	print("Earn cool rewards by using the 'Check' button!")