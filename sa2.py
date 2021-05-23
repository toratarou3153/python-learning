from numpy import sqrt


import random
import numpy as np
from scipy.spatial import distance

M=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
    [13,14,15],
    [16,17,18]
]
dist_M = distance.cdist(M,M,metric = 'euclidean')
print(dist_M)
