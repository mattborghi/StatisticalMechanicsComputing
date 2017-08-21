import math, random, pylab

def z(beta):
    return 1.0 / (1.0 - math.exp(- beta))

def pi_two_bosons(x, beta):
    pi_x_1 = math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta / 2.0))
    pi_x_2 = math.sqrt(math.tanh(beta)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta))
    weight_1 = z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta))
    weight_2 = z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta))
    pi_x = pi_x_1 * weight_1 + pi_x_2 * weight_2
    return pi_x

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def rho_harm_1d(x, xp, beta):
    Upsilon_1 = (x + xp) ** 2 / 4.0 * math.tanh(beta / 2.0)
    Upsilon_2 = (x - xp) ** 2 / 4.0 / math.tanh(beta / 2.0)
    return math.exp(- Upsilon_1 - Upsilon_2)

list_beta = [i*0.1 in range(1,50)]
nsteps = 1000
low = levy_harmonic_path(2)
high = low[:]
data = []
for beta in list_beta:
    for step in xrange(nsteps):
        # move 1
        if low[0] == high[0]:
            k = random.choice([0, 1])
            low[k] = levy_harmonic_path(1)[0]
            high[k] = low[k]
        else:
            low[0], low[1] = levy_harmonic_path(2)
            high[1] = low[0]
            high[0] = low[1]
        data += low[:]
        # move 2
        weight_old = (rho_harm_1d(low[0], high[0], beta) *
                      rho_harm_1d(low[1], high[1], beta))
        weight_new = (rho_harm_1d(low[0], high[1], beta) *
                      rho_harm_1d(low[1], high[0], beta))
        if random.uniform(0.0, 1.0) < weight_new / weight_old:
            high[0], high[1] = high[1], high[0]

#Analytic solutions of the probabilities of both permutations
fract_two_cycles = [z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]
fract_one_cycle = [z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]

fig1 = pylab.figure()
pylab.plot(list_beta,fract_one_cycle,label='one cyle')
pylab.plot(list_beta,fract_two_cycles,label='two cyles')
pylab.legend()
pylab.xlabel('$\\beta$')
pylab.ylabel('$Probabilities of permutations$')
pylab.grid()
pylab.xlim(-3,3)
pylab.title('Two bosons (beta=%s)'% beta)
pylab.savefig('plot_A2_beta%s.png'% beta)
pylab.show()

fig2 = pylab.figure()
x = [i*0.1 for i in range(-30,31)]
y = [pi_two_bosons(i,beta) for i in x]
pylab.plot(x,y,label='histogram')
pylab.hist(data,normed=True,bins=50,label='analytic')
pylab.legend()
pylab.xlabel('$x positions$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.grid()
pylab.xlim(-3,3)
pylab.title('Two bosons (beta=%s)'% beta)
pylab.savefig('plot_A2_beta%s.png'% beta)
pylab.show()