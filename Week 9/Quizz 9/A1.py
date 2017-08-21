import random, math,pylab

def prob(x):
    s1 = math.exp(-(x + 1.2) ** 2 / 0.72)
    s2 = math.exp(-(x - 1.5) ** 2 / 0.08)
    return (s1 + 2.0 * s2) / math.sqrt(2.0 * math.pi)

x_tot = 0.0
nruns  = 4
x_pos = []
for i in range(nruns):
	delta = 100.0 
	nsteps = 100000
	acc_tot = 0
	acc_tmp = 0
	x = 0.0
	x_av = 0.0
	for step in xrange(nsteps):
	    xnew = x + random.uniform(-delta, delta)
	    if random.uniform(0.0, 1.0) < prob(xnew) / prob(x):
	        x = xnew
	        acc_tot += 1
	        acc_tmp += 1
	    x_av += x
	    x_pos.append(x)

	    if step%100 == 0: 
	    	if acc_tmp > 60: delta *= 1.1
	    	if acc_tmp < 40: delta /= 1.1 
	    	acc_tmp = 0

	x_tot += x_av/float(nsteps)
	print 'global acceptance ratio:', acc_tot / float(nsteps)
	print '<x> =', x_av / float(nsteps)
	print 'delta = ',delta

print 'Total average of nruns = ', nruns
print '<x>tot = ', x_tot/float(nruns)

#Make histogram of <x>
fig1 = pylab.figure()
pylab.hist(x_pos,normed=True,bins=70,label='histogram pos',alpha = 0.5,color='r')
pylab.legend()
pylab.xlabel('$x positions$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.grid()
#pylab.xlim(-3,3)
pylab.title('A1')
pylab.savefig('plot_A1.png')
pylab.show()