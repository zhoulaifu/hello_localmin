import scipy.optimize as op
import numpy as np

N=2

# Assume X is an numpy array of lenth 10
def f(X):
    sum=0 
    for i in range(N):
        sum+=X[i]*X[i]
    return sum

res = op.minimize(f,np.ones(N),method="powell")
print res
