def list_combination(list1, list2):
	i=0
	listin = []
	for val in list1:
		listin.append(val)
		listin.append(list2[i])
		i+=1

	return listing

if __name__ == '__main__':
#    assert list_combination([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6], "First"
#   assert list_combination([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2], "Second"
	list1=[1, 1, 1, 1]
	list2=[2, 2, 2, 2]
	i=0
	listin = []
	for val in list1:
		listin.append(val)
		listin.append(list2[i])
		i+=1
print(listin)

# shortest solution return [j for i in list(zip(list1, list2)) for j in i]
