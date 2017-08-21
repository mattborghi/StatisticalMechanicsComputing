import math,random,pylab

def sample_final_point(beta, N):
    sigma = math.sqrt(beta / float(N))
    xprev = 0.0
    for i in range(N):
        xnext = random.gauss(xprev, sigma)
        xprev = xnext
    return xnext

beta = 2.0
N = 1
nruns = 10000
pos = []
pos2=[]
for sample in range(nruns):
	pos.append(sample_final_point(beta,N) )
	pos2.append(sample_final_point(0.5,99) )


pylab.hist(pos,normed=True,alpha=0.5)
pylab.hist(pos2,normed=True,alpha=0.3)
sigma = math.sqrt(beta / float(N))
pylab.xlim(-7,7)
#x = [i*0.01 for i in range(-100,100)]
#y = [math.exp(-beta*i**2)/sigma for i in x]
#pylab.plot(x,y)
pylab.show()