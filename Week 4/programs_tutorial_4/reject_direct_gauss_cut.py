import random, math

y_max = 1.0 / math.sqrt(2.0 * math.pi)
x_cut = 5.0
n_data = 1000
n_accept = 0
while n_accept < n_data:
	#Random point in the square 0:ymax ; -xcut:xcut
    y = random.uniform(0.0, y_max)
    x = random.uniform(-x_cut, x_cut)
    #Is the point below the gaussian cut curve?
    if y < math.exp( - x **2 / 2.0)/math.sqrt(2.0 * math.pi): 
        n_accept += 1
        print x
