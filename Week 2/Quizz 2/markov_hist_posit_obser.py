import random, pylab,math

def markov_disks_box(L,sigma):
    n_steps = 500
    #L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
    for steps in range(n_steps):
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        #Calculo la distancia minima entre los centros de los discos en L que no se movieron
        #y el nuevo 'b'
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        #Hay overlapping?
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            #Save the new accepted position
            a[:] = b
    return L

L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
N = 4
delta = 0.1
sigma = 0.1197 #eta = 0.18 corresponds to sigma = 0.1197
power=5
n_runs = 10**power
histo_data = []
for run in range(n_runs):
    if run % 10000 == 0 : 
        print run
    pos = markov_disks_box(L, sigma)
    for k in range(N):
        #Save the x position of the N-disks to an histogram
        histo_data.append(pos[k][0])
pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('X position observable for N disks')
pylab.ylabel('Frequency')
pylab.title('Markov Chain sampling: x position coordinate histogram (density eta=0.18)')
pylab.grid()
pylab.savefig('markov_disks_histo.png')
pylab.show()