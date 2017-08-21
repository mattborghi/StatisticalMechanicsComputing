import random, math, numpy, sys, os

def levy_harmonic_path_3d(k):
    x0 = tuple([random.gauss(0.0, 1.0 / math.sqrt(2.0 *
                math.tanh(k * beta / 2.0))) for d in range(3)])
    x = [x0]
    for j in range(1, k):
        Upsilon_1 = 1.0 / math.tanh(beta) + 1.0 / \
                          math.tanh((k - j) * beta)
        Upsilon_2 = [x[j - 1][d] / math.sinh(beta) + x[0][d] /
                     math.sinh((k - j) * beta) for d in range(3)]
        x_mean = [Upsilon_2[d] / Upsilon_1 for d in range(3)]
        sigma = 1.0 / math.sqrt(Upsilon_1)
        dummy = [random.gauss(x_mean[d], sigma) for d in range(3)]
        x.append(tuple(dummy))
    return x

def rho_harm_3d(x, xp):
    Upsilon_1 = sum((x[d] + xp[d]) ** 2 / 4.0 *
                    math.tanh(beta / 2.0) for d in range(3))
    Upsilon_2 = sum((x[d] - xp[d]) ** 2 / 4.0 /
                    math.tanh(beta / 2.0) for d in range(3))
    return math.exp(- Upsilon_1 - Upsilon_2)

N = 300
T_star = 0.8
beta = 1.0 / (T_star * N ** (1.0 / 3.0))
min_cycle = 10
hist_cycle = []
hist_cycle_10 = []
# snippet 1: read the configuration from a file (if possible)
filename = 'data_boson_configuration_N%s.txt'% N
# Initial condition
positions = {}
if os.path.isfile(filename):
    f = open(filename, 'r')
    for line in f:
        a = line.split()
        positions[tuple([float(a[0]), float(a[1]), float(a[2])])] = \
               tuple([float(a[3]), float(a[4]), float(a[5])])
    f.close()
    if len(positions) != N:
        sys.exit('ERROR in the input file.')
    print 'Starting from file', filename
else:
    for k in range(N):
        a = levy_harmonic_path_3d(1)
        positions[a[0]] = a[0]
    print 'Starting from a new configuration'

# Monte Carlo loop
nsteps = 100000
for step in range(nsteps):
    # move 1: resample one permutation cycle
    boson_a = random.choice(positions.keys())
    perm_cycle = []
    while True:
        perm_cycle.append(boson_a)
        boson_b = positions.pop(boson_a)
        if boson_b == perm_cycle[0]:
            break
        else:
           boson_a = boson_b
    k = len(perm_cycle)
    if k > min_cycle: 
        hist_cycle_10 += [boson_a[0]]
        #print 'filling'
    hist_cycle += [boson_a[0]]
    perm_cycle = levy_harmonic_path_3d(k)
    positions[perm_cycle[-1]] = perm_cycle[0]
    for k in range(len(perm_cycle) - 1):
        positions[perm_cycle[k]] = perm_cycle[k + 1]
    # move 2: exchange
    a_1 = random.choice(positions.keys())
    b_1 = positions.pop(a_1)
    a_2 = random.choice(positions.keys())
    b_2 = positions.pop(a_2)
    weight_new = rho_harm_3d(a_1, b_2) * rho_harm_3d(a_2, b_1)
    weight_old = rho_harm_3d(a_1, b_1) * rho_harm_3d(a_2, b_2)
    if random.uniform(0.0, 1.0) < weight_new / weight_old:
        positions[a_1] = b_2
        positions[a_2] = b_1
    else:
        positions[a_1] = b_1
        positions[a_2] = b_2
#for boson in positions.keys():
    #print boson, positions[boson]

# snippet 2: write configuration on a file
f = open(filename, 'w')
for a in positions:
   b = positions[a]
   f.write(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]) + ' ' +
           str(b[0]) + ' ' + str(b[1]) + ' ' + str(b[2]) + '\n')
f.close()

# snippet 3: Analyze cycles, do 3d plot
import pylab, mpl_toolkits.mplot3d

fig = pylab.figure()
ax = mpl_toolkits.mplot3d.axes3d.Axes3D(fig)
ax.set_aspect('equal')
n_colors = 10
list_colors = pylab.cm.rainbow(numpy.linspace(0, 1, n_colors))[::-1]
dict_colors = {}
i_color = 0
positions_copy = positions.copy()
while positions_copy:
    x, y, z = [], [], []
    starting_boson = positions_copy.keys()[0]
    boson_old = starting_boson
    while True:
        x.append(boson_old[0])
        y.append(boson_old[1])
        z.append(boson_old[2])
        boson_new = positions_copy.pop(boson_old)
        if boson_new == starting_boson: break
        else: boson_old = boson_new
    len_cycle = len(x)
    if len_cycle > 2:
        x.append(x[0])
        y.append(y[0])
        z.append(z[0])
    if len_cycle in dict_colors:
        color = dict_colors[len_cycle]
        ax.plot(x, y, z, '+-', c=color, lw=0.75)
    else:
        color = list_colors[i_color]
        i_color = (i_color + 1) % n_colors
        dict_colors[len_cycle] = color
        ax.plot(x, y, z, '+-', c=color, label='k=%i' % len_cycle, lw=0.75)
pylab.title(str(N) + ' bosons at T* = ' + str(T_star))
pylab.legend()
ax.set_xlabel('$x$', fontsize=16)
ax.set_ylabel('$y$', fontsize=16)
ax.set_zlabel('$z$', fontsize=16)
xmax = 6.0
ax.set_xlim3d([-xmax, xmax])
ax.set_ylim3d([-xmax, xmax])
ax.set_zlim3d([-xmax, xmax])
pylab.savefig('plot_boson_configuration_T%s.png'% T_star)
pylab.show()


fig2 = pylab.figure()
x = [i*0.1 for i in range(-30,31)]
y = [ math.exp(-i**2)/math.sqrt(math.pi) for i in x]
pylab.plot(x,y,label='|psi0(x)|^2')
pylab.hist(hist_cycle,normed=True,bins=70,label='histogram pos',alpha = 0.5,color='r')
pylab.hist(hist_cycle_10,normed=True,bins=70,label='hist min_cycle=10',alpha=0.6,color='b')
pylab.legend()
pylab.xlabel('$x positions$')
pylab.ylabel('$\\pi(x)$ (normalized)')
pylab.grid()
pylab.xlim(-3,3)
pylab.title('B3 (beta=%s)'% beta)
pylab.savefig('plot_B3_N%s.png'% N)
pylab.show()