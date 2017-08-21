import random, math,pylab

sigma = 0.16
L_hist = []
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
for t in range(1000):
    a = random.choice(L)
    while True:
        b = [random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        if min_dist > 4.0 * sigma ** 2:
            a[:] = b
            break
    print L
    print 'At t = ',t
    #L_hist += L



#pylab.hist(L_hist, bins=10) #, normed=True, color='r', histtype='step', label='sampled'
#pylab.legend()
#pylab.title('Histogram L')
#pylab.xlabel('$Disks positions$', fontsize=14)
#pylab.xlim([0,1])
#pylab.ylabel('Freq', fontsize=14)
#pylab.savefig('figura.png')