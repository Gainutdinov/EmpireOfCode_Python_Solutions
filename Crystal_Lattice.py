import numpy as np
def golf(cube):
    flat_string = ""
    from collections import Iterable
    a = np.array(cube)
    #print(type(list(a.flatten())))
    flat_list = []
    flat_list = list(a.flatten(cube))
    for item in flat_list:
        flat_string += item
    #print(flat_list)
    iterator = int(len(flat_string)/2)
    index = int(0)
    while(index != (iterator-1)):
        if (flat_string[index] != flat_string[(len(flat_string)-index-1)]):
            index += 1
        else:
            #print('False')
            return False
    #print('True')
    return True

###

###


golf([[['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']], [['Z', 'X', 'Z'], ['X', 'Z', 'X'], ['Z', 'X', 'Z']], [['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']]])
#   print("All done? Earn rewards by using the 'Check' button!")
#XZZXXZ == True
#XZZZZX == False
