import random,pylab

L = 5
t_max = 1000
site = [0, 0]
epsilon = 0.3
pos_x = []
pos_y = []
for t in range(t_max):
    if random.uniform(0.0, 1.0) > epsilon:
        delta = random.choice([[1, 0], [0, 1], [-1, 0], [0, -1]])
        site[0] = (site[0] + delta[0]) % L
        site[1] = (site[1] + delta[1]) % L
        pos_x.append(site[0])
    	pos_y.append(site[1]+10)
print site

fig1 = pylab.figure()
pylab.hist(pos_x,normed=True,bins=L,label='histogram pos x',alpha = 0.5,color='r')
pylab.hist(pos_y,normed=True,bins=L,label='histtogram pos y',alpha=0.6,color='b')
#pylab.legend()
pylab.xlabel('$x positions$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.grid()
pylab.xlim(-1,10+(L)+1)
pylab.title('B3')
#pylab.savefig('plot_B3_N.png')
pylab.show()