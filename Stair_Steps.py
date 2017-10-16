
#  (i) cost (Price[i]) of the Price list 
#  let's guess (C(n)) — cost of the path from (0) stair to last one (n). 
#  now let's make recurrent correlation expression C(n). We able to jump in (n) stair we need to choose between stairs to (n−1) or to (n−2) stair 
#  Thus,  (C(n−1)) and (C(n−2)) costs of the stairs accordingly, we need to summ value (Price[n]) for each stair (n). 
#  but between two stairs we need to choose the biggest one (n−1) and (n−2).

# recurrent expression
# C(n)=max(C(n−1),C(n−2))+Price(n).

# C = [0] * (n + 1)
# C[1] = Price[1]
#for i in range(2, n + 1):
#    С[i] = max(C[i — 1], C[i — 2]) + Price[i]


def golf(n):
    dist = {0:0}
    ret = []
    for i in range(1, len(n)+1):
        dist[i] = max(n[i-1]+dist[i-1], n[i-1]+dist.get(i-2, 0))
        ret.append(dist[i])
    return max(ret[-2:])

# 3 stars solution
def golf(n):
 v=[0]
 for i in range(len(n)):
  v += [n[i] + max(v[i-1],v[i])]
 return max(v[-2:])