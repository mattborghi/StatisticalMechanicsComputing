import random, math,pylab

def prob(x):
    s1 = math.exp(-(x + 1.2) ** 2 / 0.72)
    s2 = math.exp(-(x - 1.5) ** 2 / 0.08)
    return (s1 + 2.0 * s2) / math.sqrt(2.0 * math.pi)

x_pos = []    
nruns = 4
for i in range(nruns):
	delta = 2.0
	nsteps = 100000
	acc_tot = 0
	x = 0.0
	x_av = 0.0
	for step in xrange(nsteps):
	    xnew = x + random.uniform(-delta, delta)
	    if random.uniform(0.0, 1.0) < prob(xnew) / prob(x):
	        x = xnew
	        acc_tot += 1
	    x_av += x
	    x_pos.append(x)

	print 'global acceptance ratio:', acc_tot / float(nsteps)
	print '<x> =', x_av / float(nsteps)


#Make histogram of <x>
fig1 = pylab.figure()
pylab.hist(x_pos,normed=True,bins=70,label='histogram pos',alpha = 0.5,color='r')
pylab.legend()
pylab.xlabel('$x positions$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.grid()
#pylab.xlim(-3,3)
pylab.title('A')
pylab.savefig('plot_A.png')
pylab.show()