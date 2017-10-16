def golf_mine(number):
	rez=1
	for i in str(number):
		if i=='0':
			pass
		else:
			rez=rez*1*int(i)
	return rez

def golf(n,w=1):
	for i in [int(i) for i in str(n) if i!='0']: w*=i
	return w
'''
#Shortest solution
+def golf(n,w=1):
+ for z in str(n):
+  w*=max(int(z),1)
+ return w
'''

#
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(123405) == 120
#    assert golf(999) == 729
#    assert golf(1000) == 1
#    assert golf(1111) == 1
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

golf(123450) == 1