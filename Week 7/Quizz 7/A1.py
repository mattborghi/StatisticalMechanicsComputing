#Consider two distinguishable quantum particles in a one-dimensional harmonic trap (particles do not interact with each other)
#Write a simple program sampling their positions from levy_harmonic_path(k), with k=1.

#The two lists ("low" and "high") encode the positions at slice 0 (low, tau = 0) and at slice 1 (high, tau = beta).
import math, random, pylab

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

beta = 2.0
nsteps = 1000000
low = levy_harmonic_path(2)
high = low[:]
data = []
for step in xrange(nsteps):
    k = random.choice([0, 1])
    low[k] = levy_harmonic_path(1)[0]
    high[k] = low[k]
