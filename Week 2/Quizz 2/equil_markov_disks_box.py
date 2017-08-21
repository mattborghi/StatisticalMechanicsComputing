import random,math
def markov_disks_box(L,sigma):
	n_steps = 500
	#L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
	for steps in range(n_steps):
		a = random.choice(L)
		b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
		#Calculo la distancia minima entre los centros de los discos en L que no se movieron
		#y el nuevo 'b'
		min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
		box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
		#Hay overlapping?
		if not (box_cond or min_dist < 4.0 * sigma ** 2):
			#Save the new accepted position
			a[:] = b
	return L


sigma = 0.15
delta = 0.1
x_vec = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]

del_xy = 0.05
power = 6  
n_runs = 10**power
conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
configurations = [conf_a, conf_b, conf_c]
hits = {conf_a: 0, conf_b: 0, conf_c: 0}
for run in range(n_runs):
    x_vec = markov_disks_box(x_vec,sigma)
    #print x_vec
    for conf in configurations:
        condition_hit = True
        for b in conf:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in x_vec) < del_xy
            condition_hit *= condition_b
        if condition_hit:
            hits[conf] += 1
for a in hits:
    print a, hits[a]
