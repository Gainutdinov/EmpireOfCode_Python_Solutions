def common_words(first, second):
    common_words = []
    first_words = first.split(",")
    second_words = second.split(",")
    for word in first_words:
        if word in second_words:
            common_words.append(word)
    # print(common_words)
    common_words.sort()
    result_string = ','.join(common_words)
    # print(result_string)
    # if common_words:
    #    common_words = common_words[:-1]
    return result_string


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert common_words(
        "one,two,three", "four,five,six") == "", "Too different"
    assert common_words(
        "one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
