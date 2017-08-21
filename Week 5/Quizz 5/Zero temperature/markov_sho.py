import random, math
import matplotlib.pyplot as plt
import numpy as np
# Markov-chain Monte Carlo algorithm for a particle in a SHO potential
# using the Metropolis algorithm
# V(x) = x^2/2


def phi_0_sqr(*pos):
	#print pos
	#print pos[0]
	if isinstance(pos[0],list):
		#print 'It is a list'
		#print pos, len(pos[0])
		#print range(1,len(pos[0])+1)
		#print [x for x in range(1,len(pos[0])+1)]
		new = [math.exp(- pos[0][i] ** 2 / 2.0) / (math.pi**(1.0/4.0)) for i in range(len(pos[0])) ]
		new2 = [new[x]*new[x] for x in range(len(new))]
	else:
		#print 'It is an int'
		new = math.exp(- pos[0] ** 2 / 2.0) / (math.pi**(1.0/4.0))
		new2 = new*new
	return new2

x = 0.0
delta = 0.5
pos = []
#y = [-0.057,2,3]
#print phi_0_sqr(y)
proba = phi_0_sqr(x)
for k in range(50000):
    x_new = x + random.uniform(-delta, delta)
    proba_ant = proba
    proba = phi_0_sqr(x_new)
    #print 'x_new = ',x_new, 'exp2 = ',proba,'exp = ',math.exp(- x_new ** 2 / 2.0) / (math.pi**(1.0/4.0))
    if random.uniform(0.0, 1.0) < proba/proba_ant : 
        x = x_new 
    #print x
    #pos += [proba] 
    pos.append(x)

plt.figure(figsize=(20,10))
t = np.linspace(min(pos),max(pos),1000).tolist()
plt.plot(t,phi_0_sqr(t),color="red",label="psi_0(x)^2")
plt.hist(pos,normed=True,bins=100,label="Histogram Markov-chain",color='b')
plt.legend()
plt.title('SHO Particle Positions')
plt.xlabel('$<Positions>$', fontsize=14)
plt.ylabel('$Frequency$', fontsize=14)
#plt.show()
plt.savefig('sho_potential.png')