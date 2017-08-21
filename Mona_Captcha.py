FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")





def recognize(image):
    #print([item[1] for item in image])
    #print(list(zip(*image))) compact variant variant
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
    model_numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    answer = ''
    Listing = list(zip(*image))
    #print(Listing)
    
    del Listing[::4]
    #print(Listing[::4], "OutputList")
    OutputList = Listing
    #print(OutputList)
    
    #OutputList = list(filter(lambda x: x!=(0, 0, 0, 0, 0), Listing))  #remove empty tuples from list

    for number in zip(OutputList[0::3],OutputList[1::3],OutputList[2::3]):#some_list[start:stop:step]
        index = 0
        flag=0
        for guess in model_numbers:
            for a,b in zip(guess,number):
                for x,y in zip(a,b):
                    if x!=y:
                        flag += 1
            if flag>1:
                pass
            else:
                answer+=str(index)
                break
            index += 1
            flag = 0 
    #print(answer)
    return int(answer)

recognize ([[0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0], 
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], 
            [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0], 
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
            [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0]])
