import random
import math
import pylab
#import random, math, pylab

def markov_pi(N, delta): 
    x, y = 1.0, 1.0
    n_hits = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0: n_hits += 1
    return n_hits
 
n_runs = 500

print ("delta, acceptance rate")
for delta in [0.062, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0]:
    n_trials_list = []
    rms_deviation = []
    acceptance_rate = []
    
    for poweroftwo in range(4,13):
        n_trials = 2 ** poweroftwo
    
    
        sum2 = 0.0
        acceptance_rates = 0.0
    
        for run in range(n_runs):
            #print (4.0 * direct_pi(n_trials) / float(n_trials) )
            n_hits = markov_pi(n_trials,delta)
            pi_est = 4.0 * n_hits / float(n_trials)
            #Compute the rms deviation
            sum2 += (pi_est - math.pi)**2
            #acceptance_rates += n_hits/float(n_trials)
            #print("n_hits ",n_hits, "acceptance_rate",n_hits/float(n_trials))
    
        rms_deviation.append(math.sqrt( sum2 / n_runs ))
        #pi_ave.append(pi_est)
        n_trials_list.append(n_trials)
        acceptance_rate.append(acceptance_rates/float(n_runs) )
        #print ("At run ",poweroftwo,"pi = ", pi_est, "+- ",math.sqrt( sum2 / n_runs ))
        print (delta,"|", acceptance_rate)
        pylab.plot(n_trials_list, rms_deviation, 'o',ms=8, label='$\delta = $' + str(delta))

pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel('number of trials')
pylab.ylabel('root mean square deviation')
pylab.plot([10.0, 10000.0], [1.644 / math.sqrt(10.0), 1.644 / math.sqrt(10000.0)],label='direct')
pylab.title('Markov-chain sampling of pi: root mean square deviation vs. n_trials')
pylab.legend(loc='upper right')
pylab.savefig('C:\Users\emili\Desktop\Coursera\programs_lecture_1\markov_sampling_rms_deviationFit.png')
pylab.show()
