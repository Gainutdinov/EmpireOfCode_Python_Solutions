def flat_list(array):

    array1 = []
    array = str(array).replace("[","").replace("]","").replace(" ","")
    if array == "":
        return []
    else:
        array = list(array.split(","))
        #print(array)
        for item in array:
            if item!="":
                array1.append(int(item))
            else:
                pass
        #print(array1)
        return array1

#flat_list([-1, [1, [-2, [3], [[5], [10, -11], [1, 100, [-1000, [5000]]], [20, -10, [[[]]]]]]]])
#flat_list([[[[[[[[[]]]]]]]]])
#flat_list([1, 2, 3])
#flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])
#flat_list([-1, [1, [-2], 1], -1])

