def transpose(data):
    #print(data)
    #transposed=zip(**transposed)
    #print(list(map(list, zip(*data))))
    return list(map(list, zip(*data)))

transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])