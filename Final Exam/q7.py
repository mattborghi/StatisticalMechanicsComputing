import random,pylab

L = 9
b = 0
x = 0
pos = []
posx= 0
nsteps = 1000000
for step in range(nsteps):
    if random.uniform(0.0, 1.0) < 0.5 + b:
        dx = 1
    else:
        dx = -1
    #print x+dx
    if x + dx >= 0 and x + dx < L:
        x += dx
    pos.append(x)
    if (x==0): posx +=1

print posx/float(nsteps), '== 1/L =', 1/float(L)
pylab.hist(pos,normed=True,bins=L)
pylab.show()