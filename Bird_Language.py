def translate(phrase):
    VOWELS = "aeiouy"
    result = ''

    def from_bird_to_human(secret_phrase):
        decoded_word = ''
        index = 0
        while (index != len(secret_phrase)):
            if secret_phrase[index] not in VOWELS:
                decoded_word += secret_phrase[index]
                index += 2
            elif (secret_phrase[index] in VOWELS) and (secret_phrase[index + 1] in VOWELS) and (secret_phrase[index + 2] in VOWELS):
                decoded_word += secret_phrase[index]
                index += 3
        return decoded_word
    for word in phrase.split(' '):
        result += from_bird_to_human(word) + ' '
    # print(result.rstrip())
    return 0


translate("sooooso aaaaaaaaa")

# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert translate("hieeelalaooo") == "hello", "Hi!"
#    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
#    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
#    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
#
#    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
