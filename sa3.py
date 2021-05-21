import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.spatial import distance
import math

uni = pd.read_csv('campas.txt')
init_cam = list(uni['name'])
random.shuffle(init_cam)

def dist(xss: list)->float :
    d = 0
    for i in range(len(xss)):
        d += math.sqrt((xss[i-1][0]-xss[i][0]**2 + (xss)[i-1][1]-xss[i][1]))**2 + (xss[i-1][2]-xss[i][2]**2)
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
    A = 1/(1+math.ex(tep/T))

def main():
    Tp = T(0)
    n_per = 10
    x = init_cam
    print(x)
    y = move(x["Longitude"]["Latitude"])
    #while T(t)>0.001 :
    if dist(y) < dist(x):
        x = y
    else :
        #for i in range(n_per):
        print("だめです")


            #j = A(Tp)
            #if juri >=juri_hanntei :
                #x = y
    #t = t+1
    print(y)

if __name__ == '__main__':
    main()
