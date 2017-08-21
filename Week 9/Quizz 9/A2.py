import math, random

def V(x, y):
    pot  = -4.0 * x ** 2 - x ** 3 + 4.0 * x ** 4
    pot += -4.0 * y ** 2 - y ** 3 + 4.0 * y ** 4
    return pot

loop = 6
gamma_min = 0.0025
gamma_max = 0.6
for i in range(loop):
    xmin, ymin = 0.807044513157, 0.807044513157
    gamma = (gamma_max - gamma_min)/float(loop-1) * i + gamma_min
    n_runs = 10
    n_success = 0
    for run in range(n_runs):
        T = 4.0
        x, y = 0.0, 0.0
        delta = 0.1
        step = 0
        acc = 0
        while T > 0.00001:
            step += 1
            #Modify delta through the acceptance rate [0.3:0.7]: automatic step-size control
            #annealing schedule: the temperature is reduced every 100 iterations
            if step == 100:
                T *= (1.0 - gamma)
                if acc < 30:
                   delta /= 1.2
                elif acc > 70:
                   delta *= 1.2
                step = 0
                acc = 0
            xnew = x + random.uniform(-delta, delta)
            ynew = y + random.uniform(-delta, delta)
            #Calculate acceptance rate
            if abs(xnew) < 1.0 and abs(ynew) < 1.0 and \
               random.uniform(0.0, 1.0) < math.exp(- (V(xnew, ynew) - V(x, y)) / T):
                x = xnew
                y = ynew
                acc += 1
        #Check if for a certain run there was a success
        #That is if the minimum found was the global minimum and not local
        if math.sqrt((x - xmin) ** 2 + (y - ymin) ** 2) < 0.1:
            n_success += 1
    print 'Gamma = ',gamma, '\t','# success = ', n_success / float(n_runs)