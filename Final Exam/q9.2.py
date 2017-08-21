import math, random,pylab

L = 100
V = [math.sin((site + 1) * 0.2) / math.sqrt((site + 1) * 0.2) for site in range(L)]

gamma = 0.05
beta = 0.01
beta_max = 500.0
site = 0
step = 0
pos = []
while beta < beta_max:
    site_new = random.randint(0, L - 1)
    if random.uniform(0.0, 1.0) < math.exp(-beta * (V[site_new] - V[site])):
        site = site_new
    step += 1
    if step % 100 == 0:
        beta *= (1.0 + gamma)

    pos.append(site)
print site, V[site]

pylab.hist(pos,normed=True)
pylab.show()