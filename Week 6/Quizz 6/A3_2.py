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
    xnew, ynew = gauss_cut(),gauss_cut()
    exp_new = - alpha * (xnew ** 4 + ynew ** 4)
    exp_old = - alpha * (x ** 4 + y ** 4)
    if random.uniform(0.0, 1.0) < math.exp(exp_new - exp_old):
        x = xnew
        y = ynew
    samples_x.append(x)
    samples_y.append(y)
    if step%100000==0: print step

pylab.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
pylab.axis([-1.0, 1.0, -1.0, 1.0])
cb = pylab.colorbar()
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title('A3_2')
pylab.savefig('plot_A3_2.png')
pylab.show()