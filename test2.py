import math
import numpy as nm
from scipy import integrate

def move(self: list) -> list:
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    self[a], self[b] = self[b], self[a]

    return self

y_1 =lambda x: 1/(math.sqrt(2*math.pi))*math.exp(-x**2/2)
iy = integrate.quad(y_1,-nm.infty,1)

for i in nm.linspace(1.0,2.0,10) :
    y_2 = 1/(1+math.exp(-i))
    print(y_2)
