import random

N = 3
#Create a dictionary called statistics
statistics = {}
L = range(N)
nsteps = 10000
for step in range(nsteps):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    #Permute any two elements of the 3 element list
    L[i], L[j] = L[j], L[i]
    #Increment or initialice the lists counter 
    if tuple(L) in statistics: 
        statistics[tuple(L)] += 1
    else:
        statistics[tuple(L)] = 1
    print L
    print range(N)
    print

for item in statistics:
    print item, statistics[item]
