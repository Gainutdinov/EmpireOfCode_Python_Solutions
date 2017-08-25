def good_radix(str_number):
    k_base = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10,
              'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18,
              'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25, 'P': 26,
              'Q': 27, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34,
              'Y': 35, 'Z': 36}

    def converter(string, base):
        num_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        integer = 0
        for character in string:
            assert character in num_alphabet, 'Found unknown character!'
            value = num_alphabet.index(character)
            assert value < base, 'Found digit outside base!'
            integer *= base
            integer += value
        return integer
    for character in k_base:
        if character in str_number:
            base = character
    for k in range(k_base[base], 36 + 1):
        decimal_form = converter(str_number, k)
        if ((decimal_form) % (k - 1) == 0):
            return k
    return 0


print(good_radix('18'))

# if __name__ == '__main__':    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert good_radix("18") == 10, "Simple decimal"
#    assert good_radix("1010101011") == 2, "Any number is divisible by 1"
#    assert good_radix("222") == 3, "3rd test"
#    assert good_radix("A23B") == 14, "It's not a hex"
#    assert good_radix("IDDQD") == 0, "k is not exist"
