def disjoint(number):
    # find all triangularNumbers between 0 and number
    triangularNumbers = []
    tN = []
    for i in range(1, number):
        tN.append( int(( i * (i + 1))/2) )
        if tN[i-1] >= number:
            break
        else:
            triangularNumbers.append(tN[i-1])
    # find all good combinations
    summ = 0
    sumOk = []

    for y in range(len(triangularNumbers)):
        for x in triangularNumbers[y:len(triangularNumbers)]:
            summ += x
            if (summ == number):
                sumOk.append(triangularNumbers[y:triangularNumbers.index(x)+1])
            elif (summ > number):
                break
        summ = 0
    #find the longest array
    theWinnerIs = []
    if (len(sumOk)==0):
        return theWinnerIs
    else:
        return max(sumOk, key=len)
    
print(disjoint(882))
