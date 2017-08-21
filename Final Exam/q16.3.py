import random, math,pylab

N      = 4
beta   = 1.0
tau    = beta / float(N)
x      = [0.0] * N
nsteps = 100000
pos =[]
for step in range(nsteps):
    k = random.randint(0, N - 1)
    xprev = x[(k - 1) % N]
    xnext = x[(k + 1) % N]
    sigma = math.sqrt(tau / 2.0)
    x[k] = random.gauss((xprev + xnext) / 2.0, sigma)
    pos.append(x[1]-x[0])

pylab.hist(pos,normed=True)
pylab.savefig('q16.3.png')
pylab.show()