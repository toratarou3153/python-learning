import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.spatial import distance
import math

#uni = pd.read_csv('campas.txt')
#init_cam = list(uni['name'])
#init_lon = list(uni['Longitude'])
#init_lat = list(uni['Latitude'])
#init_hig = list(uni['hight'])
#random.shuffle(init_cam)


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

def T(t):
    T = 1/math.log(t+2)
    return T

def A(T):
    A = 1/(1+math.exp(1/(T+1)))
    return A

def main():
    xs = [["1号館",32,45,4],["2号館",52,63,45],["3号館",44,76,67],["4号館",19,23,65],["5号館",65,57,27]]
    random.shuffle(xs)
    n_per = 10
    y = move(xs)
    l = [[] for _ in range(100)]
    t = 0
    while T(t)>0.5 :
        for i in range(100):
            if dist(y) < dist(xs):
                xs = y
                l[i].append(xs)
            else :
                for k in range(n_per) :
                    j = A(i)
                    if j > 0.05:
                        xs = y
                        l[i].append(xs)
    t = t+1

    print(min(l))
if __name__ == '__main__':
    main()