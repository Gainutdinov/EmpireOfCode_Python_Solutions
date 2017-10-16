
def swap_sort(array):
	array=list(array)
	#print(type(array))
	list1=[]
	for i in reversed(range(len(array))):
		for j in range(1, i + 1):
			if array[j-1] > array[j]:
				#numj=int(j);num_j=int(j-1)
				# print(swap_numb)
				swap_numb='%i%i' % ((j-1), j);
				list1.append(str(swap_numb));#list1.append(j)
				array[j], array[j-1] = array[j-1], array[j]
	#myList = ['str1', 'str2', 'str3']

	myString = ", ".join(list1)
	print(list1, myString)
	return myString
swap_sort((1, 4, 2, 3, 5))
def swap_sort1(array): #solution from internet
    result = ''
    array = list(array)
    for p_left in range(len(array)-1, 0, -1):
        for index in range(p_left):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                result += str(index) + str(index + 1) + ','
return result[:-1]