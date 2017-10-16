#Crystal Grid
def check_grid(grid):
	comparison_i='0';
	for i in grid:
		#print(comparison_i)
		comparison_y='0';
		if comparison_i==(''.join(i)):
			#print('False')
			return False
		comparison_i=''.join(i)
		for y in i:
			if y==comparison_y:
				#print('False Comparison_y')
				return False
			comparison_y=y;
	return True


check_grid([["X", "X"], ["X", "X"]])






'''
	if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
	assert check_grid([["X", "Z", "X"],
						["Z", "X", "Z"],
						["X", "Z", "X"]]), "3x3 Good"
	assert check_grid([["X", "Z", "X", "Z"],
						["Z", "X", "Z", "X"]]), "2x4 Good"
	assert not check_grid([["X", "X"],
							["X", "X"]]), "2x2 Bad"
	assert not check_grid([["X", "Z", "X"],
							["Z", "Z", "Z"],
							["X", "Z", "X"]]), "3x3 Bad"
	assert not check_grid([["X", "Z", "X", "Z"],
							["X", "Z", "X", "Z"]]), "2x4 Bad"

	print("Use 'Check' to earn sweet rewards!")

	check_grid([["X", "Z"], ["Z", "X"]]) == True
	check_grid([["X", "X"], ["X", "X"]]) == False
	'''