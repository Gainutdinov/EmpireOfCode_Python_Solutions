def check_structure(pattern, structure, pattern_level=2):

    def convert_to_Nbase(n,base):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, base)
            nums.append(str(r))
        return ''.join(reversed(nums))

    #pattern_new = str(bin(pattern)[2:])
    if pattern_level==2:
        pattern_new = str(bin(pattern)[2:])
    elif pattern_level==3:
        pattern_new = convert_to_Nbase(pattern,3)
    elif pattern_level==4:
        pattern_new = convert_to_Nbase(pattern,4)

    if (len(structure) > len(pattern_new)):
        diff = len(structure) - len(pattern_new)
        pattern_new = ("0" * diff) + pattern_new
    elif (len(structure) < len(pattern_new)):
        #print("falseeeee")
        return False
    #print(pattern_new)
    for pattern_elem, structure_elem in zip(pattern_new, structure):
        if (pattern_elem == "0" and structure_elem.isdigit()==True):
            pass
            #print("True digit")
        elif (pattern_elem == "2" and structure_elem.isupper()==True):
            pass
        elif (pattern_elem == "1" and structure_elem.isalpha()==True):
            pass
            #print("True Alpha")
        elif (pattern_elem == "3" and structure_elem == " "):
            pass
        else:
            #print("False because doesn't fits structure")
            #print("false")
            return False
    #print("True")
    return True

check_structure(127, "Checkio")

#check_structure(42, "12a0b3e4"), "42 is the answer"
#    assert not check_structure(101, "ab23b4zz"), "one hundred plus one"
#    assert check_structure(0, "478103487120470129"), "Any number"
#    assert check_structure(127, "Checkio"), "Uppercase"
#    assert not check_structure(7, "Hello"), "Only full match"
#    assert not check_structure(8, "a"), "Too short command"
#    assert check_structure(5, "H2O"), "Water"
#    assert not check_structure(42, "C2H5OH"), "Yep, this is not the Answer"
#
#    # Rank 2
     
#    assert not check_structure(1826, 'CheckiO', 3), "wrong up and down"
#    assert check_structure(66431, '9z1b2c4d6a7Z', 3), "Various"

# Rank 3
#    assert not check_structure(39294315, 'Kill Them ALL', 4), "Don't kill"
#    assert not check_structure(29, 'aXz', 4), "A Z"
