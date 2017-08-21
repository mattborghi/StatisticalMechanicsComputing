import random, math
n_trials = 400000
n_hits = 0
var = 0.0
aveObs = 0.0
aveObs2 = 0.0

for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
    #var += (Obs - math.pi)**2
    aveObs += Obs
    aveObs2 += Obs **2

aveObs  = aveObs/float(n_trials)
aveObs2 = aveObs2/float(n_trials)

print ("Pi, <Obs>, <Obs^2>, <Obs>^2-<Obs^2>")
print 4.0 * n_hits / float(n_trials),aveObs,aveObs2, math.sqrt(abs((aveObs**2)-aveObs2))