import random, math, pylab

def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def gauss_cut():
    while True:
        #Mean = 0
        #SD = 1
        x = random.gauss(0.0, 1.0)
        if abs(x) <= 1.0:
            return x

alpha = 0.5
nsamples = 1000000
samples_x = []
samples_y = []
for sample in xrange(nsamples):
    while True:
        x = gauss_cut()
        y = gauss_cut()
        #x = random.uniform(-1.0,1.0)
        #y = random.uniform(-1.0,1.0)
        #rad = math.sqrt(x ** 2 + y**2)
        #actualize
        #xnew = x/rad
        #ynew = y/rad
        #xnew = phi(x)
        #ynew = phi(y)
        #p = math.exp(-0.5*(xnew**2+ynew**2)-alpha*(xnew**4+ynew**4))
        p = math.exp(-alpha*(x**4+y**4))
        if random.uniform(0.0,1.0) < p:
            break
    samples_x.append(x)
    samples_y.append(y)
    if sample%100000==0: print sample

pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A1_2')
pylab.savefig('plot_A1_2.png')
pylab.show()