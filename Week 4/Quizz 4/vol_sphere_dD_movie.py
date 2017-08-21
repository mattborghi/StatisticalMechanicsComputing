import random,math,pylab

#VOlume of a sphere of dim dimension
def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)

#<Q_d>
d = 4
dimensions = d - 1
#Coordinates vector
x = []
#Initialize to zero
x = [0.0]*dimensions
delta = 0.1
n_trials = 40000
n_runs = 100
Qd = 0.0
old_radius_square = 0.0
hist_dist = []
for j in range(n_runs):
	n_hits = 0
	for i in range(n_trials):
		#Instead of modifying all components of x at a time, as we did in markov_pi.py,
		#modify only one component at each iteration i (with i=0, 1, 2,...., n_trials).
		k = random.randint(0, dimensions - 1)
		x_old_k = x[k]
		x_new_k = x_old_k + random.uniform(-delta, delta)
		new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2   
	    
		alpha = random.uniform(-1.0,1.0)
	    #Inside (d-1) unit sphere?
	    #I dont have to rest x[dimensions-1]**2 because I never sum it.
		if new_radius_square < 1.0:
			x[k] = x_new_k
			old_radius_square = new_radius_square
		if old_radius_square+alpha**2 < 1.0: 
			n_hits += 1
			hist_dist += [math.sqrt(old_radius_square+alpha**2)]
		#print k,new_radius_square,x[dimensions-1],new_radius_square+x[dimensions-1]**2,math.sqrt(new_radius_square+x[dimensions-1]**2)
		
	#print 4.0 * n_hits / float(n_trials)
	#Updated once for each j (nruns)
	#print 2.0*n_hits/float(n_trials)
	Qd += 2.0*n_hits/float(n_trials)
print 'Q',d,'average = ',Qd/float(n_runs)
print 'Q',d,'  exact = ',V_sph(d)/V_sph(d-1)

# exact distrubution:
npoints = 100
list_x = [i/float(npoints) for i in xrange(0, npoints)]
list_y = [d*x**(d-1) for x in list_x]
# graphics output
pylab.plot(list_x, list_y, color='k', label='exact')
pylab.hist(hist_dist, bins=150, normed=True) #, color='r', histtype='step', label='sampled'
pylab.legend()
pylab.title('Sampling of the Q%i' % d)
pylab.xlabel('$x$', fontsize=14)
pylab.xlim([0,1])
pylab.ylabel('$Q%i$' % d, fontsize=14)
pylab.savefig('q%i.png' % d)
