import math, random
#Generate a random walk path
#Then we have to pull back the path to a desired end.
#This is done in trivial_free_path.py
beta = 4.0
N = 8
sigma = math.sqrt(beta / N)
x = [0.0]
for k in range(N - 1):
    x.append(random.gauss(x[-1], sigma))
print x
