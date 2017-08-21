import random, math, pylab

def gauss_cut():
    while True:
        #Mean = 0
        #SD = 1
        x = random.gauss(0.0, 1.0)
        if abs(x) <= 1.0:
            return x

alpha = 0.5
nsteps = 1000000
samples_x = []
samples_y = []
x, y = 0.0, 0.0
for step in range(nsteps):
    if step % 2 == 0:
        while True:
            x = gauss_cut()
            p = math.exp(- alpha * x ** 4 )
            if random.uniform(0.0, 1.0) < p:
                break
    else:
        while True:
            y = gauss_cut()
            p = math.exp(- alpha * y ** 4 )
            if random.uniform(0.0, 1.0) < p:
                break
    samples_x.append(x)
    samples_y.append(y)
    if step%100000==0: print step

pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A2_2')
pylab.savefig('plot_A2_2.png')
pylab.show()