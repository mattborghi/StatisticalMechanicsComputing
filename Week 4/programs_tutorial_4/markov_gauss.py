import random, math
# Markov-chain Monte Carlo algorithm for a particle in a Gaussian potential
# using the Metropolis algorithm
import pylab
x = 0.0
delta = 0.5
pos = []
for k in range(200000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  \
         math.exp (- x_new ** 2 / 2.0) / math.exp (- x ** 2 / 2.0): 
        x = x_new 
    #print x
    pos.append(x) 

pylab.hist(pos,normed=True,bins=100)
pylab.show()