#def count_ingots(report):

#import unicodedata

def non_unique(data):

	list=[]
#	str1 = ''.join(data)
	str1="".join(str(elm) for elm in data)
#	print(str1)
	for i in data:
		if type(i)==int:
#			print('INT')
			if data.count(i) > 1:
				list.append(i)
		elif type(i)==str:
			up_i=i.upper()
			low_i=i.lower()
			if (str1.count(low_i)>1) or (str1.count(up_i)>1) or ((str1.count(up_i)==1) and (str1.count(low_i)==1)):
				list.append(i)
#			print('STR')
	return list
#	print(str1,list)
#	return 0

#non_unique([7, 44, 28, 'str', 'A', 'a',28, 44])
non_unique(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i','A', 'X', 'j', 'L', 'y', 's', 'K', 'g','p', 'r', 7, 'b'])