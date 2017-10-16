def golf(broken_report):
    listing = broken_report.split(',')
    x_dict = {}
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    prev = 0
    for letter in ascii_uppercase:
        for i in range(1, 10):
            prev += 1
            x_dict[str(letter) + str(i)] = prev
    #for element in listing
    # sum_ingots +=x[element]
    #print(sum_ingots)
    sum_ingots = 0
    #print(listing)
    for element_of_listing in listing:
        for i in range(0, len(element_of_listing)-1):
            #print(i, '  ', element_of_listing[i] + element_of_listing[i+1])
            poss_wordlist = element_of_listing[i] + element_of_listing[i+1]
            if poss_wordlist in x_dict:
                sum_ingots += x_dict[poss_wordlist]
                #print(poss_wordlist, 'Bingo!')
    #print(sum_ingots)

    return sum_ingots
golf("ASDA1,BB22D01C1")