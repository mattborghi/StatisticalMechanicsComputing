import random, math

sigma = 0.16
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
for t in range(100000):
    a = random.choice(L)
    b = [random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma)]
    min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    if min_dist > 4.0 * sigma ** 2:
        a[:] = b
    print L
    print 'At t = ',t