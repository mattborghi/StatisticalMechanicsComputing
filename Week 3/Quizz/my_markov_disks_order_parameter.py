import random,math,pylab,os,cmath
#For scatter plot 
import numpy as np
import matplotlib.pyplot as plt

#For the calculation of order parameter
def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L,N, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)

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
n_steps = 200001
Global_Order_Parameter = []
GOP_eta = []
eta_x = []
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
    #Compute the order parameter for every 100 steps
    if(steps%1000 == 0): 
        Global_Order_Parameter.append( abs(Psi_6(L,N, sigma) ))
        #print steps, Global_Order_Parameter[-1]
    #After 10.000 steps decrease the density by 0.02
    if(steps%10000 ==0 and steps!=0):
        #Promediate the global parameter for a fixed eta 
        #print steps,Global_Order_Parameter
        #print sum(Global_Order_Parameter)/float(len(Global_Order_Parameter))
        GOP_eta.append(sum(Global_Order_Parameter)/float(len(Global_Order_Parameter)))
        eta_x.append(eta)
        Global_Order_Parameter = []
        eta -= 0.02
        sigma = math.sqrt( eta/N/math.pi ) #Disks radii
        delta = 0.5*sigma
        print "eta = ",eta+0.02, "order parameter = ",GOP_eta[-1] #The [-1] prints the last element
#Print the abs(GOP) as a function of eta
fig = plt.figure()
plt.scatter(eta_x,GOP_eta,color='red')
plt.xlabel('eta')
plt.ylabel('Global Order Parameters')
plt.show()
fig.savefig('Global_Order_Parameter_etaN%i' % N)
#print L
print 'Writing final configuration in the file'
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
show_conf(L, sigma, 'Markov Chain \n hard disk configuration N%i eta%.2f' % (N, eta), 'disk_configuration_N%i_eta%.2f.png' % (N, eta) )