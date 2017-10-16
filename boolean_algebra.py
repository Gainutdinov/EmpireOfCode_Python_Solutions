def boolean(x, y, operation):

	import re
	if re.fullmatch(operation, "conjunction"):
		return (x and y)
	elif re.fullmatch(operation, "disjunction"):
		return (x or y)
	elif re.fullmatch(operation, "implication"):
		return (not(x) or y)
	elif re.fullmatch(operation, "exclusive"):
		#print(int((bool(x) ^ bool(y))))
		return (int((bool(x) ^ bool(y))))
	elif re.fullmatch(operation, "equivalence") and x==y:
		return(1)
	else:
		return(0)
#boolean(0, 1, "exclusive")
#is_valid = pattern.match( address )