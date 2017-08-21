import random, math
import matplotlib.pyplot as plt
import numpy as np

# Markov-chain Monte Carlo algorithm for a particle in a SHO potential
# using the Metropolis algorithm
# V(x) = x^2/2

def psi_n_square(x, n):
    if n == -1:
        return 0.0
    else:
    	#psi_0: ground state
        psi = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
        #psi_1: first excited state
        psi.append(math.sqrt(2.0) * x * psi[0])
        #generate with a recursion the psi_2(x)...psi_n(x)
        for k in range(2, n + 1):
            psi.append(math.sqrt(2.0 / k) * x * psi[k - 1] -
                       math.sqrt((k - 1.0) / k) * psi[k - 2])
        return psi[n] ** 2

def psi_n_square_list(n,*x_points):
	psi = {}
	if n == -1:
		return 0.0
	else:
		#print n
		for x in x_points[0]: 
			#psi_0: ground state
			psi[x] = [math.exp(-x ** 2 / 2.0) / math.pi ** 0.25]
			#print [x[0][1]]
			#psi_1: first excited state
			psi[x].append(math.sqrt(2.0) * x * psi[x][0])
			#generate with a recursion the psi_2(x)...psi_n(x)
			#print len(psi[0]),len(psi[1])
			for k in range(2, n + 1):
				psi[x].append(math.sqrt(2.0 / k) * x* psi[x][k - 1] -
							math.sqrt((k - 1.0) / k) * psi[x][k - 2])
		return [psi[i][n] ** 2 for i in x_points[0]]


def phi_0_sqr(*pos):
	#print pos
	#print pos[0]
	if isinstance(pos[0],list):
		#print 'It is a list'
		#print pos
		#print len(pos[0])
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
n = 0
#y = [-0.057,2,3]
#print phi_0_sqr(y)
proba = psi_n_square(x,n)
#print "psi_%d(x)^2 = "%n,proba
for k in range(50000):
	#Transition (n,x)->(n,x') where x' = x_new
    x_new = x + random.uniform(-delta, delta)
    proba_ant = proba
    proba = psi_n_square(x_new,n)
    #print 'x_new = ',x_new, 'exp2 = ',proba,'exp = ',math.exp(- x_new ** 2 / 2.0) / (math.pi**(1.0/4.0))
    #Metropolis acceptance rate
    # r < min(1, psi_n(x')^2/psi_n(x)^2) = min(1, pi(x')/pi(x))
    if random.uniform(0.0, 1.0) < proba/proba_ant : 
        x = x_new 
    #print x
    #pos += [proba] 
    pos.append(x)

plt.figure(figsize=(20,10))
#print min(pos),max(pos)
t = np.linspace(min(pos),max(pos),1000).tolist()
#t = [i * 0.2 for i in range(-25, 26)]
plt.plot(t,psi_n_square_list(n,t),color="red",label="psi_%d(x)^2"% n)
plt.hist(pos,normed=True,bins=100,label="Histogram Markov-chain",color='b')
plt.legend()
plt.title('SHO Particle Positions')
plt.xlabel('$<Positions>$', fontsize=14)
plt.ylabel('$Frequency$', fontsize=14)
#plt.show()
plt.savefig('sho_potential_pi_%d(x).png'%n)