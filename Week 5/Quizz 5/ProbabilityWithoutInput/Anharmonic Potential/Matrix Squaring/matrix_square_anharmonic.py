import math, numpy
import matplotlib.pyplot as plt


#Anharmonic potential
def V(x,cubic,quartic):
    return x ** 2.0 / 2.0 + cubic * x ** 3 + quartic * x ** 4

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

# Anharmonic density matrix in the Trotter approximation (returns the full matrix)
#rho(x,x',beta) = exp(-beta V(x) / 2) rho_free(x, x', beta) exp(-beta V(x') / 2).
def rho_anharmonic_trotter(grid, beta,cubic,quartic):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * ( V(x, cubic, quartic) + V(xp, cubic, quartic)) ) \
                         for x in grid] for xp in grid])

def pi_quant(input_val,beta):
	return [ math.sqrt( math.tanh(beta/2.0) / math.pi)* math.exp(- (x)**2 * math.tanh(beta/2.0) ) for x in input_val]

quartic = 1.0
cubic = -quartic
x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]
beta_tmp = 2.0 ** (-5)                   # initial value of beta (power of 2)
beta     = 2.0 ** 2                      # actual value of beta (power of 2)
rho = rho_anharmonic_trotter(x, beta_tmp,cubic,quartic)  # density matrix at initial beta
while beta_tmp < beta:
    rho = numpy.dot(rho, rho)
    rho *= dx
    beta_tmp *= 2.0
    print 'beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp)

Z = sum(rho[j, j] for j in range(nx + 1)) * dx
pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
f = open('data_anharm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
for j in range(nx + 1):
    f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
f.close()

plt.figure(figsize=(20,10))
plt.plot(x,pi_of_x,color="red",label="pi(x)",linewidth=4.0)
#plt.plot(x,pi_quant(x,beta_tmp),'ob',label="pi_quant(x)",linewidth=2.0)
plt.legend()
plt.title('SAnHO Particle Positions \n Matrix Square Harmonic\n $beta$ = %0.2f \n $Temp$ = %0.2f'% (beta_tmp,1/float(beta_tmp)) )
plt.xlabel('$<Positions>$', fontsize=14)
plt.ylabel('$Frequency$', fontsize=14)
plt.grid()
#plt.show()
plt.savefig('sho_matrix_square_beta%0.2f.png'%beta_tmp)