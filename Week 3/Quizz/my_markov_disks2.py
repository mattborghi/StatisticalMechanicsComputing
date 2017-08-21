import random,math,pylab

#Calculates the distances between two disks centers. Implements periodic boundary conditions.
def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

def show_conf(L, sigma, title, fname):
    pylab.axes()
    for [x, y] in L:
        #print [x,y]
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                #print "ix = ",ix, "iy = ",iy
                #print "x+ix =",x+ix, "iy = ",y+iy
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()

L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]] #
N = len(L) #Number of disks
eta = 0.5 #Density of disks
sigma = math.sqrt( eta/N/math.pi ) #Disks radii
#sigma = 0.15
#sigma_sq = sigma ** 2
delta = 0.1
n_steps = 1000
for steps in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b,c) for c in L if c != a)
    #min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    #box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    
    if not (min_dist < 2.0*sigma): #4.0 * sigma ** 2
    	#box_cond or 
        a[:] = [e%1.0 for e in b]
print L
show_conf(L, sigma, 'test graph', 'N_markov_disks_pbc.png')