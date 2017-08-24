def probability(sequence, step):
    w = sequence.count('w')
    b = sequence.count('b')
    s = step
    def probability_finder(white, black, step):
        white_prob = white / (white+black)
        black_prob = 1 - white_prob
        if step == 1:
            return round(white_prob,2)

        else:
            pick_white = white_prob * probability_finder(white-1, black+1, step-1)
            pick_black = black_prob * probability_finder(white+1, black-1, step-1)
            return round((pick_white + pick_black),2)

    return probability_finder(w, b, s)

print(probability('bbw', 3))
