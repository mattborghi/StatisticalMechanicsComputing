import random,pylab

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

delta_list = []
acceptance_rate = []

n_trials = 2**12
for delta in frange(0.062,4.0,0.01):
#frange(0.062,4.0,0.01):
#[0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]:
    x, y = 1.0, 1.0
    n_hits = 0
    n_miss = 0
    n_real = 0
    for i in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            n_real += 1
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0: n_hits += 1
        else: n_miss += 1
    delta_list.append(delta)
    acceptance_rate.append(float(n_real)/float(n_trials))
    #print (n_hits,n_miss, n_trials, n_real)
    #print ("For delta = ",delta," acceptance rate = ", 1.0*n_hits/float(n_trials),1.0*n_miss/float(n_trials) )
    #print 4.0 * n_hits / float(n_trials)  
    print (delta,float(n_real)/float(n_trials) )
    pylab.plot(delta_list, acceptance_rate, 'o')

pylab.xlabel('delta')
pylab.ylabel('acceptance rate')
pylab.savefig('C:\Users\emili\Desktop\Coursera\programs_lecture_1\DeltaOptimalValue.png')
pylab.show()
