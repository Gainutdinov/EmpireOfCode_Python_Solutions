def check_structure(pattern, structure, pattern_level=2):
    pattern_new = str(bin(pattern)[2:])

    if (len(structure) > len(pattern_new)):
        diff = len(structure) - len(pattern_new)
        pattern_new = ("0" * diff) + pattern_new
        #print(pattern_new)
    elif (len(structure) < len(pattern_new)):
        #print("falseeeee")
        return False
    for pattern_elem, structure_elem in zip(pattern_new, structure):
        if (pattern_elem == "0" and structure_elem.isdigit()==True):
            pass
            #print("True digit")
        elif (pattern_elem == "1" and structure_elem.isalpha()==True):
            pass
            #print("True Alpha")
        else:
            #print("False because doesn't fits structure")
            #print("false")
            return False
    #print("True")
    return True
