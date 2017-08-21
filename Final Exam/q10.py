import random,pylab

N=4
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.1
delta = 0.001
n_steps = 100
acc = 0
pos = []
for step in range(n_steps):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    min_dist_sq = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist_sq < 4.0 * sigma ** 2):
        a[:] = b
        acc += 1
        for k in range(N): pos.append(L[k][0])
    #print step, L

pylab.hist(pos, bins=20, normed=True)
pylab.xlabel('X position observable for N disks')
pylab.ylabel('Frequency')
pylab.title('Markov Chain sampling: x position coordinate histogram (density eta=0.18)')
pylab.grid()
pylab.savefig('markov_disks_histo.png')
pylab.show()

print acc/float(n_steps)