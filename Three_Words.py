def three_words(words):
    count = 0
    new_words = words.split(" ")
    for word in words.split(" "):
        if word.isdigit():
            count = 0
        else:
            count += 1
            if count == 3:
                return True
    return False


#three_words("Hello World hello"), "Hello"
#three_words("He is 123 man"), "123 man"
#three_words("1 2 3 4"), "Digits"
#three_words("bla bla bla bla"), "Bla Bla"
#three_words("Hi"), "Hi"
