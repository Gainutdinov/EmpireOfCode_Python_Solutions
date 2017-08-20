FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def recognize(image):
    #print([item[1] for item in image])
    #print(list(zip(*image))) best variant
    zero= [(1,1,1,1,0),
           (1,0,0,0,1),
           (0,1,1,1,1)]
    one = [(0,1,0,0,0),
           (1,1,1,1,1),
           (0,0,0,0,0)]
    two = [(1,0,0,1,1),
           (1,0,1,0,1),
           (1,1,1,0,1)]
    three=[(1,0,0,0,1),
           (1,0,1,0,1),
           (1,1,0,1,1)]
    four =[(1,1,1,0,0),
           (0,0,1,0,0),
           (1,1,1,1,1)]
    five =[(1,1,1,0,1),
           (1,0,1,0,1),
           (1,0,0,1,0)]
    six = [(0,1,1,1,0),
           (1,0,1,0,1),
           (1,0,1,1,1)]
    seven=[(1,0,0,1,1),
           (1,0,1,0,0),
           (1,1,0,0,0)]
    eight=[(1,1,1,1,1),
           (1,0,1,0,1),
           (1,1,1,1,1)]
    nine =[(0,1,1,0,1),
           (1,0,1,0,1),
           (1,1,1,1,0)]
    list_numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    Listing = list(zip(*image))
    OutputList = list(filter(lambda x: x!=(0, 0, 0, 0, 0), Listing))  #remove empty tuples from list
    print(OutputList)
    for number in zip(OutputList[0::3],OutputList[1::3],OutputList[2::3]): #some_list[start:stop:step]
        for n in number: # first line of the number, after that we start comparing with other numbers
                flag = 0 #if greater than 1 go to the next number
            for n in 
          print('\n')
    for number in list_numbers:
        pass
        #print(number)
       
    return 1

recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
           [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
           [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
           [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]])
