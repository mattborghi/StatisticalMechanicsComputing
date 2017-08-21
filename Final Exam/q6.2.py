import random,math,pylab

#p1(x) = exp(-x ** 2 / 2),     for x < -1.0 or x > 1.0
#p1(x) = exp(-x ** 2 / 2) / 2, for -1 <= x <= 1.0
#p2(x) = exp(-x ** 2 / 2),     for any x

def p1(x):
	if abs(x)<=1: 
		return math.exp(-x ** 2 / 2.0) / 2.0
	else:
		return math.exp(-x ** 2 / 2.0)

def p2(x): return math.exp(-x ** 2 / 2.0)


x = [i*0.01 for i in range(-300,300)]
p22 = [math.exp(-i**2 /2) for i in x]

nruns = 10000
distr = []
rand_x = 0
for sample in range(nruns):
	#Choice a random x
	rand_x = random.choice(x)
	eta = random.uniform(0.0,1.0)
	rand_x = eta*rand_x
	#eta = random.uniform(0.0,p2(rand_x))
	if p1(rand_x) <= p2(rand_x): distr.append(rand_x) 

pylab.hist(distr,normed=True)
#pylab.xlim(-1,1)
pylab.show()