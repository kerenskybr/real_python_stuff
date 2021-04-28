import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x = [8., 1, 2.5, 4, 28.]
x_with_nan = [8., 1, 2.5, math.nan, 4, 28.]

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

################################
# Mean of the values (média)
print(sum(x) / len(x))
# or, more elegant (fmean() for python > 3.8)
print(statistics.mean(x))
# or numpy
print(np.mean(x))
# For values with NaN data
print(np.nanmean(y_with_nan))
# Or even pandas
print(z_with_nan.mean())
####################################

###########################################
#Weighted Mean (media aritmetica ponderada)
w = [0.1, 0.2, 0.3, 0.25, 0.15]
print(sum(w[i] * x[i] for i in range(len(x))) / sum(w))
# Using numpy
y, z, w = np.array(x), pd.Series(x), np.array(w)
print(np.average(y, weights=w))
#############################################

###################################33
#Harmonic Mean
print(statistics.harmonic_mean(x))
############################

##########################
# Geometric mean
#########################
gmean = 1
for item in x:
    gmean *= item

gmean **= 1/ len(x)
print(gmean)
# or
#print(statistics.geometric_mean(x)) # python >=3.8

##################3
# Sample median
############
n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index-1] + x_ord[index])

print(median_)
# or
print(statistics.median(x))