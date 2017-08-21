import random,math,pylab,os

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

#------------------------------------------------------
#Declaring constants
N_sqrt = 8
N = N_sqrt ** 2 #=len(L) #Number of disks
eta = 0.72 #Density of disks .> limit value eta = 0.78
sigma = math.sqrt( eta/N/math.pi ) #Disks radii
#sigma = 0.15
#sigma_sq = sigma ** 2
#delta = 0.1
delta = 0.5*sigma
#sigma + i*(1-2.0*sigma)/8.0
n_steps = 100000
#------------------------------------------------------

filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)
if os.path.isfile(filename):
    #If the file exists read it
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)]) 
    f.close()
    print 'starting from file', filename
else:
    #If the file does not exists generate L and write to the file
    L = []
    #This calculations were deduced by saying that the gap between 0-L=1 is
    #(k+1)*deltt + 2*sigma*k=L=1 [1] 
    #where deltt is a gapp between the disks
    #So the step size is sigma+deltt -> + deltt + 2*sigma -> idem last
    #Generally, sigma+deltt +i*(deltt+2*sigma) where i from 0 to k-1 
    #from equation [1] -> deltt =( 1-2*sqrt(eta/pi) )/ (k+1)
    #so for delta <= 0 (the gaps between the disks) there are overlaps between the disks. 
    #This corresponds to a value of density eta >= pi/4~ 0.78  
    #So for values between 0 < eta < 0.78 the initial configuration is legal.
    deltt = ( 1-2.0*math.sqrt(eta/math.pi) )/float(N_sqrt+1)
    delxy = sigma + deltt
    two_delxy = 2.0*sigma + deltt#(1-2.0*sigma)/8.0
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]        
    print 'starting from a new random configuration'
    print 'and writing the file'
    f = open(filename, 'w')
    for a in L:
       f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
    f.close()


for steps in range(n_steps):

    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist = min(dist(b,c) for c in L if c != a)
    #min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    #box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    
    if not (min_dist < 2.0*sigma): #4.0 * sigma ** 2
    	#box_cond or 
        a[:] = [e%1.0 for e in b]
#print L
print 'Writing final configuration in the file'
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
show_conf(L, sigma, 'Markov Chain \n hard disk configuration N%i eta%.2f' % (N, eta), 'disk_configuration_N%i_eta%.2f.png' % (N, eta) )