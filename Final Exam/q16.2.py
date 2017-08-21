import random, math,pylab

N      = 4
beta   = 1.0
tau    = beta / float(N)
x      = [0.0] * N
delta  = 0.5
nsteps = 100000
pos = []
for step in range(nsteps):
    xnew = [x[k] + random.uniform(-delta, delta) for k in range(N)]
    weight_old = 1.0
    weight_new = 1.0
    for k in range(N):
        knext = (k + 1) % N
        weight_old *= math.exp(-(x[k] - x[knext]) ** 2 / (2.0 * tau))
        weight_new *= math.exp(-(xnew[k] - xnew[knext]) ** 2 / (2.0 * tau))
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        x = xnew[:]
    pos.append(x[1]-x[0])

pylab.hist(pos,normed=True)
pylab.savefig('q16.2.png')
pylab.show()