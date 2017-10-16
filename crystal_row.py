def check_line(line):
	import re
	print(len(line))
	listing=[]
	i=0
	if line[0]=="Z":
		for i in range(len(line)-1):
			listing.append("Z")
			listing.append("X")
	else:
		for i in range(len(line)-1):
			listing.append("X")
			listing.append("Z")
	my_String_listing = ''.join(listing)
	my_String_line=''.join(line)
	print(listing,my_String_listing,my_String_line)
	if re.match(my_String_line, my_String_listing):
		print("True")
		return True
	else:
		print("False")
		return False


#	assert check_line(["X", "Z", "X", "X"]) == False
#	assert check_line(["X", "Z"]) == True
#	assert check_line(["Z", "X"]) == True

check_line(["X", "Z", "X", "X"])




def check_line(line):
    if len(line) < 2:
        return True
    elif len(line) == 2:
        if line[0] == line[1]:
            return False
        else:
            return True
    else:
        res = True
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                res = False
                break
        return res