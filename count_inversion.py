def count_inversion(sequence):
    n = 0
    for i, x in enumerate(sequence):
        for j, y in enumerate(sequence[i:]):
            if x <= y:
                continue
            else:
                n += 1
    #print(n)
    return n

count_inversion((1, 2, 5, 3, 4, 7, 6))
count_inversion((0, 1, 2, 3))
count_inversion((99, -99))
count_inversion((5, 3, 2, 1, 0))