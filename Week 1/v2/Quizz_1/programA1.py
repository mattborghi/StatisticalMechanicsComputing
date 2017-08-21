import random

#import plotly.plotly as py
#import plotly.graph_objs as go

#import numpy as np
N = 20
position = 0
x = []

for t in range(1):
    if random.uniform(0.0, 1.0) < 0.5:
        position = (position + 1) % N
    elif random.uniform(0.0, 1.0) > 0.5:
        position = (position - 1) % N
        
    x.append(1)
    x[t] = position
    print (t," , ",x[t])


