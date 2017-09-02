VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
DELIMETERS = ".,?"


def striped_words(text):
    for separator in DELIMETERS:
        text=text.replace(separator," ")
    text=text.split()
    count = 0
    not_stripe = ''
    for word in text:
        #print(word)
        if len(word)<2:
            pass
        else: # find even and odd indexes and after that check - do all of them are vowels(odd) and consonants (even) and vice versa
            if word[0] in VOWELS:
                for letter_odd in word[::2]:
                    if letter_odd in VOWELS:
                        pass
                    else:
                        not_stripe = "not"
                        break
                for letter_even in word[1::2]:
                    if letter_even in CONSONANTS:
                        pass
                    else:
                        not_stripe = "not"
                        break
            else:
                for letter_odd in word[::2]:
                    if letter_odd in CONSONANTS:
                        pass
                    else:
                        not_stripe = "not"
                        break
                for letter_even in word[1::2]:
                    if letter_even in VOWELS:
                        pass
                    else:
                        not_stripe = "not"
                        break
            
            if not not_stripe:
                count +=1
            else:
                not_stripe = ''
    #print(count)
    return count

striped_words("Dog,cat,mouse,bird.Human.")

#    assert striped_words("My name is ...") == 3, "All words are striped"
#    assert striped_words("Hello world") == 0, "No one"
#    assert striped_words("A quantity of striped words.") == 1, "Only of"
#    assert striped_words("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
