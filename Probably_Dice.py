def probability(dice_number, sides, target):
    from math import factorial
    s = target
    b = sides
    a = dice_number
    n = b**a #all possible combinations
    m = 0 # lucky combinations when sum of the dices equal to target

    def Lucky_combinations(Number_of_times, i):
        if i == 0:
            c = 1
        else:
            c = factorial(Number_of_times)/( factorial(Number_of_times-i) * factorial(i) )
        return int(c)
    
    print(Lucky_combinations((2),(1)),"divide")
    for index in range( 0, ((s-a)//b+1) ):
        print(index)
        m += (-1)**index*Lucky_combinations(a,index)*Lucky_combinations( (s-b*index-1),(a-1) )

    print(m/n)
    return 0.0

probability(10, 10, 50)

def almost_equal(checked, correct, significant_digits=4):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision

#    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
#    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
#    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
#    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
#    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
#    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
#    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
