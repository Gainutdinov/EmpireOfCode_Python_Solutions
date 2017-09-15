def convert(chislitel, znamenatel):
    result = [str(chislitel//znamenatel) + "."]
    summ_ostatok = [chislitel % znamenatel]   
    chislitel = int(summ_ostatok[0])
    while chislitel != 0:
        chislitel *= 10
        dilitel, chislitel = divmod(chislitel, znamenatel)
        result.append(str(dilitel))             
        if chislitel not in summ_ostatok:
            summ_ostatok.append(chislitel)
        else:
            result.insert(summ_ostatok.index(chislitel) + 1, "(")
            result.append(")")
            break
    return "".join(result)
    
    
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"

    print("Earn cool rewards by using the 'Check' button!")
