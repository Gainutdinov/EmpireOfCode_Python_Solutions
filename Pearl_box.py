def probability(sequence, step):
    
    def pearl_prob(white, black):
        return white / (white+black)

    w = sequence.count('w')
    b = sequence.count('b')
    #print(sequence, w, b)

    while (step!=1):
        w_prob = pearl_prob(w, b)
        b_prob = pearl_prob(b, w)      
        
        pick_white = w_prob * pearl_prob((w-1), (b+1))
        pick_black = b_prob * pearl_prob((w+1), (b-1))

        step -= 1
    
    #print (pick_white + pick_black)

    return (pick_white + pick_black)
   
probability('bbw', 3)
