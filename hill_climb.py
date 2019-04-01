# Aidin_ze
import numpy as np
import itertools as it
import random
import math
from time import sleep
#  create nebirs matrix

z = []
a = []
n = 2
for x in it.product('012', repeat=n): 
    for j in range(n):
        z.append(int(x[j]))
    a.append(z)
    z = []
del a[len(a)//2]
n_matrix = np.array(a) - 1
# function formula
def formula(x):
    return math.cos(x[0])*math.sin(x[1]) # return your function
# main code 
x_input=  [random.uniform(-20, 20),random.uniform(-20, 20)]
while(True):
    x_nebirs = x_input + n_matrix *0.05 #alfa size
    y_ne = []
    for i in x_nebirs:
        y_ne.append(formula(i))
    y_ne = np.array(y_ne)
    y_best = y_ne.min()
    if y_best <  formula(x_input):
        print("x={}".format(x_input))
        print("y={}".format(y_best))
        x_input = x_nebirs[y_ne.argmin()]

    else:
        print("best point:")
        print("x={}".format(x_input))
        print("y={}".format(y_best))
        break
    print("------------")
    sleep(1)
