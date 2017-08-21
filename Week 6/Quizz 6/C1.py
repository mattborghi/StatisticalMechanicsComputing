import math, random, pylab

def V(x, cubic, quartic):
    pot = x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot

def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

quartic = 1.0
cubic = -quartic
beta = 20.0
N = 100
dtau = beta / N
delta = 1.0
n_steps = 500000
x = [0.1] * N
old_Trotter_weight = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x))
data = []
Ncut = N/6
n_hits = 0
for step in range(n_steps):
    #k = random.randint(0, N - 1)
    #knext, kprev = (k + 1) % N, (k - 1) % N
    x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    #Change initial and final step
    x = x[1:] + x[:1]
    #print [-V(a,cubic,quartic)*dtau for a in x]
    new_Trotter_weight = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x_new))
    #x = levy_free_path(x[0], x[0], dtau, N)
    #x = x[Ncut:] + x[:Ncut]
    #x_new = x[k] + random.uniform(-delta, delta)
    #old_weight  = (rho_free(x[knext], x[k], dtau) *
    #               rho_free(x[k], x[kprev], dtau) *
    #               math.exp(-0.5 * dtau * x[k] ** 2))
    #new_weight  = (rho_free(x[knext], x_new, dtau) *
    #               rho_free(x_new, x[kprev], dtau) *
    #               math.exp(-0.5 * dtau * x_new ** 2))
    if random.uniform(0.0, 1.0) < new_Trotter_weight / old_Trotter_weight:
        n_hits += 1
        x = x_new[:]
        old_Trotter_weight = new_Trotter_weight
    
    if step % N == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])
    if step%(n_steps/10)==0: print step
print 'Acceptance Rate : ', n_hits / float(n_steps)
print 'If it is too small change Ncut!!'
#tau vector
#fig1 = pylab.figure()
#tau = [dtau*i for i in range(N)]
#pylab.plot(x,tau)
#pylab.xlabel('$x$')
#pylab.ylabel('$\\tau$')
#pylab.title('Feynman Path Integral (beta=%s, N=%i)' % (beta, N))
#pylab.xlim(-2, 2)
#pylab.savefig('plot_B2_beta%s.png' % beta)
#pylab.show()

fig2 = pylab.figure()
pylab.hist(data, normed=True, bins=100, label='QMC')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
pylab.plot(list_x, list_y, label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.title('Levy_anharmonic_path (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-2, 2)
pylab.savefig('plot_C1_beta%s.png' % beta)
pylab.show()