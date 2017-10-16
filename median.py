def median(data):
    #print(type(data))
    data.sort()
    #print(len(data))
    if len(data)%2==0:
        median=(data[((len(data))//2)]+data[((len(data))//2-1)])/2
    else:
        median=data[((len(data))//2)]

    #print(median)
    #print(data)
    return median

#median([1, 2, 3, 4, 5]) == 3, "Sorted list"
#median([3, 1, 2, 5, 4])
median(list(range(1000000)))