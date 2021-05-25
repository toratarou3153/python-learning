import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.spatial import distance
import math

def dist(xss: list)->float :
    d = 0
    for i in range(len(xss)):
        d += math.sqrt((xss[i-1][1]-xss[i][1])**2 + (xss[i-1][2]-xss[i][2])**2 + (xss[i-1][3]-xss[i][3])**2)
    return d

def move(self: list) -> list:
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    self[a], self[b] = self[b], self[a]

    return self

#uni = pd.read_csv('campas.txt')
#init_cam = list(uni['name'])
#init_lon = list(uni['Longitude'])
#init_lat = list(uni['Latitude'])
#init_hig = list(uni['hight'])
#random.shuffle(init_cam)

xs = [["1号館",32,45,4],["2号館",52,63,45],["3号館",44,76,67],["4号館",19,23,65],["5号館",65,57,27]]
random.shuffle(xs)




x = np.linspace(-10,10,100)
y= 1/(1+np.exp(1/x))
plt.plot(x,y)
plt.show()



#print(xs)
#print(dist(xs))
#print(move(xs))
#print(y)
