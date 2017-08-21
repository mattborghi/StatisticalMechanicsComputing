import random, math

def energy(S):
    E = S[0] * S[1] - S[1] * S[2] + S[2] * S[3] + S[3] * S[4] - S[4] * S[0]
    return E

L = 5
S = [1] * L
beta = 1.0
nsteps = 100
for step in range(nsteps):
    k = random.randint(0, L - 1)
    S_new = S[:k] + [-S[k]] + S[k + 1:]
    delta_E = energy(S_new) - energy(S)
    if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
        S = S_new[:]