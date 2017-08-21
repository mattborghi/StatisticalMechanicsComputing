import random,pylab

N = 52
nruns = 1
nsteps = 1000000
L = range(N)
zero = 0
pos_z = []
for i in range(nruns):
	for step in range(nsteps):
	    i = random.randint(0, N - 1)
	    j = random.randint(0, N - 1)
	    L[i], L[j] = L[j], L[i]
	    #print L[0]
	    #if L[0] == 0: zero += 1
	    pos_z.append(L[28])
	#if L[0] == 0: zero += 1
	#print zero/float(nsteps), 'Close to ',1/float(N)

#print zero/float(nruns), 'Close to ', 1 - 2 * (N - 1) / float(N) ** 2
fig1 = pylab.figure()
pylab.hist(pos_z,normed=True,bins=N,label='histogram pos x',alpha = 0.5,color='r')
#pylab.legend()
pylab.xlabel('$x positions$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.grid()
pylab.xlim(-1,N)
pylab.title('B3')
#pylab.savefig('plot_B3_N.png')
pylab.show()