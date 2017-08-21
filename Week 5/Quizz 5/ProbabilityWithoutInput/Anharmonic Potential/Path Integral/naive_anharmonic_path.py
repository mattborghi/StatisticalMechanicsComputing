import math, random
import matplotlib.pyplot as plt

def read_file(filename):
    list_x = []
    list_y = []
    with open(filename) as f:
        for line in f:
            x, y = line.split()
            list_x.append(float(x))
            list_y.append(float(y))
    f.close()
    return list_x, list_y

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta)) 

#Anharmonic potential
def V(x,cubic,quartic):
    return x ** 2.0 / 2.0 + cubic * x ** 3 + quartic * x ** 4

quartic = 1.0
cubic = -quartic
beta = 4.0
N = 16                                             # number of slices
dtau = beta / N
delta = 1.0                                       # maximum displacement on one slice
n_steps = 1000000                                 # number of Monte Carlo steps
x = [0.0] * N                                     # initial path
hist = []                                         #For the histogram
hist2 = []
for step in range(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-dtau*V(x[k],cubic,quartic)) )
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-dtau*V(x_new,cubic,quartic)) )
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    #print x
    #normed histogram of the x[0], that is the position of the path at slice 0
    if step%10 == 0: 
      hist += [x[0]] 
      hist2 += [x[1]]

#Read from the file
matrix_square_x, matrix_square_y = read_file('B1data_anharm_matrixsquaring_beta4.0.dat')

plt.figure(figsize=(20,10))
plt.hist(hist,alpha=0.5,normed=True,bins=100,label='hist x[0]')
plt.hist(hist2,alpha=0.3,normed=True,bins=100,label='hist x[1]')
plt.plot(matrix_square_x,matrix_square_y,label='Matrix Square',linewidth=4.0)
plt.legend()
plt.xlim(-1.0, 1.0)
plt.title('SanHO Particle Positions \n Feynmann Path Integral\n $beta$ = %0.2f \n $Temp$ = %0.2f'% (beta,1/float(beta)) )
plt.xlabel('$<Positions>$', fontsize=14)
plt.ylabel('$Frequency$', fontsize=14)
plt.grid()
#plt.show()
plt.savefig('sanho_path_integral_beta%0.2f.png'%beta)
