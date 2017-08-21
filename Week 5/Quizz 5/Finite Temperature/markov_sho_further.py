import random, math
import matplotlib.pyplot as plt
import numpy as np

# Markov-chain Monte Carlo algorithm for a particle in a SHO potential
# using the Metropolis algorithm
# V(x) = x^2/2

def psi_n_square(n,x):
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

def boltzmann(n,n_new,beta):
	energy_m = n_new + 0.5 
	energy_n = n + 0.5
	return math.exp(-beta*(energy_m - energy_n))

def pi_quant(input_val,beta):
	return [ math.sqrt( math.tanh(beta/2.0) / math.pi)* math.exp(- x**2 * math.tanh(beta/2.0) ) for x in input_val]

def pi_class(input_val,beta):
	return [math.sqrt(beta/(2.0*math.pi))*math.exp(-beta*x**2/2.0) for x in input_val]

delta = 0.5
beta_values = [0.2,1.0,5.0]
#y = [-0.057,2,3]
#print phi_0_sqr(y)
#print "psi_%d(x)^2 = "%n, proba
for beta in beta_values:
	pos = []
	x = 0.0
	n = 0
	print 'beta =',beta,'temp = ',1/float(beta)
	for k in range(50000):
		#Transition (n,x)->(n,x') where x' = x_new
	    x_new = x + random.uniform(-delta, delta)
	    proba = psi_n_square(n,x_new)
	    proba_ant = psi_n_square(n,x)
	    #print 'x_new = ',x_new, 'exp2 = ',proba,'exp = ',math.exp(- x_new ** 2 / 2.0) / (math.pi**(1.0/4.0))
	    #Metropolis acceptance rate
	    # r < min(1, psi_n(x')^2/psi_n(x)^2) = min(1, pi(x')/pi(x))
	    if random.uniform(0.0, 1.0) < proba/proba_ant : 
	        x = x_new 
	    #print x
	    #pos += [proba] 
	    pos.append(x)
	    #Transition (n,x) -> (n',x) where n' = m = n +/- 1
	    #Accepted with p=min(1, (psi_m(x)/psi_n(x))^2 * exp(-beta*(E_m-E_n))
	    if random.uniform(0.0,1.0) < 0.5: n_new = n - 1
	    else: n_new = n + 1
	    proba_ant = psi_n_square(n,x)
	    proba = psi_n_square(n_new,x)
	    if proba != 0.0:
	    	#Reject 
	    	if random.uniform(0.0,1.0) < proba/proba_ant*boltzmann(n,n_new,beta):
	    		n = n_new
	    pos.append(x)

	plt.figure(figsize=(20,10))
		#print min(pos),max(pos)
	t = np.linspace(min(pos),max(pos),1000).tolist()
		#t = [i * 0.2 for i in range(-25, 26)]
	plt.plot(t,pi_quant(t,beta),color="red",label="pi_quant(x)",linewidth=2.0)
	plt.plot(t,pi_class(t,beta),color="green",label="pi_class(x)",linewidth=2.0)
	plt.hist(pos,normed=True,bins=100,label="Histogram Markov-chain",color='b')
	plt.legend()
	plt.title('SHO Particle Positions \n $beta$ = %0.2f \n $Temp$ = %0.2f'% (beta,1/float(beta)) )
	plt.xlabel('$<Positions>$', fontsize=14)
	plt.ylabel('$Frequency$', fontsize=14)
	plt.grid()
	#plt.show()
	plt.savefig('sho_potential_beta%0.2f.png'%beta)