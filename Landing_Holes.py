def rerotate(num, mbits):
    num &= (2**mbits-1)
    bit = num & 1
    num >>= 1
    if bit:
        num |= (1 << (mbits-1))
    return num

def rotate(state, pipe_numbers):
    z = int(''.join([str(i) for i in state]), 2)
    r = []
    for n in range(len(state)):
        cc = bin(z)[2:].rjust(len(state), "0")
        if all([int(cc[i]) for i in pipe_numbers]):
            r.append(n)
        z = rerotate(z, len(state))
    return r
