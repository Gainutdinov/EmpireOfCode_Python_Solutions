def good_radix(str_number):
    result = 0
    num_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def converter(string, base):
        value_integ = 0
        for character in string:
            value_integ *= base
            value_integ += num_alphabet.index(character)
        #print(value_integ)
        return value_integ
    for symbol in num_alphabet:
        if symbol in str_number:
            base_of = symbol
    #print(range(k_base[base_of], 36 + 1))
    for k in range(num_alphabet.index(base_of) + 1, 36 + 1):
        if ((converter(str_number, k)) % (k - 1) == 0):
            result = k
            break
    return result

print(good_radix('18'))

# if __name__ == '__main__':    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert good_radix("18") == 10, "Simple decimal"
#    assert good_radix("1010101011") == 2, "Any number is divisible by 1"
#    assert good_radix("222") == 3, "3rd test"
#    assert good_radix("A23B") == 14, "It's not a hex"
#    assert good_radix("IDDQD") == 0, "k is not exist"
