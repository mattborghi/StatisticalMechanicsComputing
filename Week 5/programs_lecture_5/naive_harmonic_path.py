import math, random
import matplotlib.pyplot as plt

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta)) 

beta = 4.0
N = 8                                             # number of slices
dtau = beta / N
delta = 1.0                                       # maximum displacement on one slice
n_steps = 1000000                                 # number of Monte Carlo steps
x = [0.0] * N                                     # initial path
hist = []                                         #For the histogram
for step in range(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x[k] ** 2))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x_new ** 2))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    print x
    #normed histogram of the x[0], that is the position of the path at slice 0
    if step%10 == 0: hist += x[0] 

plt.figure(figsize=(20,10))
plt.hist(hist,normed=True,label='hist')
plt.legend()
plt.title('SHO Particle Positions \n Feynmann Path Integral\n $beta$ = %0.2f \n $Temp$ = %0.2f'% (beta,1/float(beta_tmp)) )
plt.xlabel('$<Positions>$', fontsize=14)
plt.ylabel('$Frequency$', fontsize=14)
plt.grid()
#plt.show()
plt.savefig('sho_path_integral_beta%0.2f.png'%beta)
