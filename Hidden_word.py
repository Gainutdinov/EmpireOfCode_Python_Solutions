def find_word(text, word):

        
    multiline_text = text.split("\n")
    # in case word whole can be found in one line of the text
    for index, line_of_the_text in enumerate(multiline_text, start = 1):
        line_of_the_text = line_of_the_text.replace(",","").replace(" ","").replace(".","").lower()
        if word in line_of_the_text:
            start_point = line_of_the_text.index(word[0]) + 1
            last_point = start_point + len(word) - 1
            print('Bingo!!!', index,start_point,index,last_point)
            return [index,start_point,index,last_point]
    # in case word separately located in the text
    word = list(word)
    found_letters = 0
    #print(multiline_text[0:3])
    start = 0
    stop = len(word)
    while stop!=len(multiline_text):
        Full_match = True
        for letter,line in zip(word,multiline_text[start:stop]):
            print(letter, line)
            if letter in line:
                pass
            else:
                Full_match = False 
        if Full_match is True:
            print(start+1, stop)
        stop+=1
        start+=1

    print('----------------------')
    
    print([2, 14, 2, 16])
    return 0



find_word("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") # == [4, 16, 7, 16]


