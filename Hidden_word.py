def find_word(text, word):

    multiline_text = text.split("\n")
    # in case word whole can be found in one line of the text

    for index, line_of_the_text in enumerate(multiline_text, start=1):
        line_of_the_text = line_of_the_text.replace(" ", "").lower()
        if word in line_of_the_text:
            start_point = line_of_the_text.index(word[0]) + 1
            last_point = start_point + len(word) - 1
            #print( index, start_point, index, last_point)
            return [index, start_point, index, last_point]
    if '\n' in text:  # if we got multiline text
        # create matrix of the letters
        text = [list(x) for x in text.replace(" ", "").lower().splitlines()]
        text = list(map(list, zip(* text)))  # transpose matrix of the letters
        for line in text:
            if len(line) != max(map(len, text)):
                text[text.index(line)] = line + '_' * \
                    (max(map(len, text)) - len(line))
    else:
        text = text.lower().split(' ')
        for line in text:
            if len(line) != max(map(len, text)):
                text[text.index(line)] = line + '_' * \
                    (max(map(len, text)) - len(line))
        text = list(map(list, zip(* text)))  # transpose matrix of the letters
    for index, line in enumerate(text, start=1):
        if word in ''.join(line):
            start_point = last_point = index
            start_point = ''.join(line).index(word) + 1
            stop_point = last_point = start_point + len(word) - 1
            #print(start_point, index, last_point,  index)
            return [start_point, index, last_point,  index]


# == [1,2,2,2] [row_start, column_start, row_end, column_end]
find_word("xa xb x", "ab")



