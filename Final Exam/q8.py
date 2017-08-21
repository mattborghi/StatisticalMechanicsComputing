import random,math,pylab

def A1(sigma):
    x1 = random.uniform(sigma, 1.0 - sigma)
    while True:
        x2 = random.uniform(sigma, 1.0 - sigma)
        if abs(x1 - x2) > 2.0 * sigma:
            break
    return [x1, x2]


def A2(sigma):
    y1 = random.uniform(0.0, 1.0 - 4.0 * sigma)
    y2 = random.uniform(0.0, 1.0 - 4.0 * sigma)
    y1, y2 = sorted([y1, y2])
    L = [y1 + sigma, y2 + 3.0 * sigma]
    random.shuffle(L)
    return L


def A3(sigma):
    while True:
        x1 = random.uniform(sigma, 1.0 - sigma)
        x2 = random.uniform(sigma, 1.0 - sigma)
        if abs(x1 - x2) > 2.0 * sigma:
            break
    return [x1, x2]

sigma = 0.15
nruns = 10000
posx = []
posy = []

for sample in range(nruns):
    x,y = A3(sigma)
    posx.append(x)
    posy.append(y)

f1 = pylab.figure()
pylab.hist(posy,normed=True,alpha=0.5)
pylab.hist(posx,normed=True,alpha=0.3)
pylab.show()

f2 = pylab.figure()
pylab.hist(posy+posx,normed=True,alpha=0.3)
#pylab.hist(posx,normed=True,alpha=0.3)
pylab.show()