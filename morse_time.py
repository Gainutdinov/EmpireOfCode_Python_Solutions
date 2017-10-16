def morse_time(time_string):
    variable = time_string.split(':')
    if (len(variable[1])==1):
        variable[1] = '0' + variable[1]
    if (len(variable[2])==1):
        variable[2] = '0' + variable[2]
    if (len(variable[0])==1):
        variable[0] = '0' + variable[0]    
    two_number_code={'0': '..', '1': '.-', '2': '-.'}
    three_number_code={'0': '...', '1': '..-', '2': '.-.', '3': '.--', '4': '-..', '5': '-.-', '6': '--.'}
    four_number_code={'0': '....', '1': '...-', '2': '..-.',\
                        '3': '..--','4': '.-..','4': '.-..', '5': '.-.-', '6': '.--.', '7': '.---', '8': '-...', '9': '-..-'}
    answer = (two_number_code[(variable[0])[:1]]+' '+four_number_code[(variable[0])[1:2]]+' : '+
    three_number_code[(variable[1])[:1]]+' '+ four_number_code[(variable[1])[1:2]]+' : '+\
    three_number_code[(variable[2])[:1]]+' '+ four_number_code[(variable[2])[1:2]])
    #print(answer)
    return answer

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
