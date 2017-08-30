def hamming(n, m):
    result = "{0:b}".format(m^n)
    return result.count('1')
    
    
    hamming(117, 17)
    hamming(1, 2)
    hamming(16, 15)
    
    
