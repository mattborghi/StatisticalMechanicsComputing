import random,math

x = []
x, y,z = 0.0, 0.0, 0.0
delta = 0.1
n_trials = 4000
n_runs = 1000
Q4 = 0
for j in range(n_runs):
	n_hits = 0
	for i in range(n_trials):
	    del_x, del_y,del_z = random.uniform(-delta, delta), random.uniform(-delta, delta),random.uniform(-delta, delta)
	    alpha = random.uniform(-1.0,1.0)
	    #Inside unit sphere?
	    if (x + del_x)**2 + (y + del_y)**2 + (z+del_z)**2 < 1.0:
	        x, y, z = x + del_x, y + del_y, z+del_z
	    if x**2 + y**2 + z**2 + alpha**2 < 1.0: n_hits += 1
	#print 4.0 * n_hits / float(n_trials)
	#Updated once for each j (nruns)
	#print 2.0*n_hits/float(n_trials)
	Q4 += 2.0*n_hits/float(n_trials)
print 'Q4 = 2.0*Vsph(4)/Vsph(3) = ',Q4/float(n_runs)
print 'Vsph(4) = pi^2/2, so Q4 = pi^2/2/4/3pi = 3pi/8 = ',3.0*math.pi/8.0 