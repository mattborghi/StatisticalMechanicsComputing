import random

N = 8
nsteps = 100
for step in range(nsteps):
    tmp = range(N)
    L = []
    while tmp != []:
        element = random.choice(tmp)
        tmp.remove(element)
        L.append(element)
    print L[0]