import math, random, pylab

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

beta = 20.0
N = 80
dtau = beta / N
delta = 1.0
n_steps = 4000000
x = [5.0] * N
data = []
Ncut = N/2
for step in range(n_steps):
    #k = random.randint(0, N - 1)
    #knext, kprev = (k + 1) % N, (k - 1) % N
    x = levy_harmonic_path(x[0], x[0], dtau, N)
    #x_new = x[k] + random.uniform(-delta, delta)
    #old_weight  = (rho_free(x[knext], x[k], dtau) *
    #               rho_free(x[k], x[kprev], dtau) *
    #               math.exp(-0.5 * dtau * x[k] ** 2))
    #new_weight  = (rho_free(x[knext], x_new, dtau) *
    #               rho_free(x_new, x[kprev], dtau) *
    #               math.exp(-0.5 * dtau * x_new ** 2))
    #if random.uniform(0.0, 1.0) < new_weight / old_weight:
    #    x[k] = x_new
    if step % N == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])
    #Change initial and final step
    x = x[Ncut:] + x[:Ncut]
    if step%(n_steps/100)==0: print step
#tau vector
fig1 = pylab.figure()
tau = [dtau*i for i in range(N)]
pylab.plot(x,tau)
pylab.xlabel('$x$')
pylab.ylabel('$\\tau$')
pylab.title('Feynman Path Integral (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-2, 2)
pylab.savefig('plot_B2_beta%s.png' % beta)
pylab.show()

fig2 = pylab.figure()
pylab.hist(data, normed=True, bins=100, label='QMC')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
pylab.plot(list_x, list_y, label='analytic')
pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.title('Levy_harmonic_path (beta=%s, N=%i)' % (beta, N))
pylab.xlim(-2, 2)
pylab.savefig('plot_B2_beta%s.png' % beta)
pylab.show()