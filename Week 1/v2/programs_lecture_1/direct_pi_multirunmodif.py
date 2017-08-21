import random
import math
import pylab
#import random, math, pylab

pi = 3.1415926

def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits
 
n_runs = 500
n_trials_list = []
rms_deviation = []
#pi_ave = []
for poweroftwo in range(4,13):
    n_trials = 2 ** poweroftwo
    sum2 = 0.0
    for run in range(n_runs):
        #print (4.0 * direct_pi(n_trials) / float(n_trials) )
        pi_est = 4.0 * direct_pi(n_trials) / float(n_trials)
        #Compute the rms deviation
        sum2 += (pi_est - pi)**2

    rms_deviation.append(math.sqrt( sum2 / n_runs ))
    #pi_ave.append(pi_est)
    n_trials_list.append(n_trials)
    
    print ("At run ",poweroftwo,"pi = ", pi_est, "+- ",math.sqrt( sum2 / n_runs ))

pylab.plot(n_trials_list, rms_deviation, 'o')
pylab.plot([10.0, 10000.0], [1.644 / math.sqrt(10.0), 1.644 / math.sqrt(10000.0)])
pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel('number of trials')
pylab.ylabel('root mean square deviation')
pylab.title('Direct sampling of pi: root mean square deviation vs. n_trials')
pylab.savefig('C:\Users\emili\Desktop\Coursera\programs_lecture_1\direct_sampling_rms_deviationFit.png')
pylab.show()
