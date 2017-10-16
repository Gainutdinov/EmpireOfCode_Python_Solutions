def fizz_buzz(number):
    str_num=str(number)
    if (number%3==0) and (number%5==0):
        str_num='Fizz Buzz'
    elif number%3==0:
        str_num='Fizz'
    elif number%5==0:
        str_num='Buzz'



    #print(str1_num)
    # replace this for solution
    return str_num
fizz_buzz(7)
print(2%3)