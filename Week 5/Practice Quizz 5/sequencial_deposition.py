import random, math

sigma = 0.2
for t in range(1000):
    L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
    print L
    while True:
        a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
        min_dist = min(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L)
        if min_dist > 2.0 * sigma:
            L.append(a)
            print 'Append: ',L
            if len(L) == 4: break
    print L
    print 'Llego hasta: ',t