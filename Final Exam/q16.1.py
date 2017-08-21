import random, math,pylab

N      = 4
beta   = 1.0
tau    = beta / float(N)
x      = [0.0] * N
delta  = 0.5
nsteps = 100000
pos=[]
for step in range(nsteps):
    k = random.randint(0, N - 1)
    xprev = x[(k - 1) % N]
    xnext = x[(k + 1) % N]
    xnew = x[k] + random.uniform(-delta, delta)
    weight_old = (math.exp(-(x[k] - xprev) ** 2 / (2.0 * tau)) *
                  math.exp(-(x[k] - xnext) ** 2 / (2.0 * tau)))
    weight_new = (math.exp(-(xnew - xprev) ** 2 / (2.0 * tau)) *
                  math.exp(-(xnew - xnext) ** 2 / (2.0 * tau)))
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        x[k] = xnew
    pos.append(x[1]-x[0])

pylab.hist(pos,normed=True)
pylab.savefig('q16.1.png')
pylab.show()
