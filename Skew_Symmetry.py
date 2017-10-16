#Skew Symmetry
def is_skew_symmetric(matrix):
	for n,m in zip(matrix, list(map(list, zip(*matrix)))):
		for x,y in zip(n,m):
			if x!=(-y):
				#print(False)
				return False
	#print(True)
	return True

is_skew_symmetric([
		[ 0,  1, 2],
		[-1,  0, 1],
		[-3, -1, 0]])