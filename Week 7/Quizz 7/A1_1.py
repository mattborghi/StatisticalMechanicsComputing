#Consider two distinguishable quantum particles in a one-dimensional harmonic trap (particles do not interact with each other)
#Write a simple program sampling their positions from levy_harmonic_path(k), with k=1.

#The two lists ("low" and "high") encode the positions at slice 0 (low, tau = 0) and at slice 1 (high, tau = beta).
import math, random, pylab

#Single particle analytic solution pi(x)
def pi_x(x, beta):
    sigma = 1.0 / math.sqrt(2.0 * math.tanh(beta / 2.0))
    return math.exp(-x ** 2 / (2.0 * sigma ** 2)) / math.sqrt(2.0 * math.pi) / sigma

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

beta = 2.0
nsteps = 1000000
low = levy_harmonic_path(2)
high = low[:]
data = []
for step in xrange(nsteps):
    k = random.choice([0, 1])
    low[k] = levy_harmonic_path(1)[0]
    high[k] = low[k]
    data += low[:]
    #data.append(high[k])

x = [i*0.1 for i in range(-30,31) ]
y = [pi_x(i,beta) for i in x]
pylab.plot(x,y, label='histogram')
pylab.hist(data,normed=True,bins=50, label='analytic')
pylab.legend()
pylab.xlabel('$x positions$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.grid()
pylab.xlim(-3, 3)
pylab.title('Two distinguishable particles in an harmonic trap (beta=%s)' % (beta))
pylab.savefig('plot_A1_1_beta%s.png' % beta)
pylab.show()