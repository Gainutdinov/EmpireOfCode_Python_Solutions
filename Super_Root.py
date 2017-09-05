import math
def super_root(number):
    for i in range(number):
        if (i**i)==number:
            SRoot = i
            return int(SRoot)
    def lambertW(x, prec=1e-12):
        w = 0
        for i in range(100):
            wTimesExpW = w*math.exp(w)
            wPlusOneTimesExpW = (w+1)*math.exp(w)
            w -= (wTimesExpW-x)/(wPlusOneTimesExpW-(w+2)*(wTimesExpW-x)/(2*w+2))
            if (prec > abs((x-wTimesExpW)/wPlusOneTimesExpW)):
                break
        if (prec <= abs((x-wTimesExpW)/wPlusOneTimesExpW)):
            raise Exception ("W(x) не сходится достаточно быстро при x=%f" % x)
        return w
    SRoot = math.log(number) / lambertW(math.log(number))
    #print(SRoot)
    return SRoot


super_root(81)

#      check_result(super_root, 4), "Square"
#      check_result(super_root, 9), "Cube"
#      check_result(super_root, 81), "Eighty one"
