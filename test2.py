import math
import numpy as nm
from scipy import integrate




for i in nm.linspace(1.0,2.0,10) :
    y_1 =lambda x: 1/(math.sqrt(2*math.pi))*math.exp(-x**2/2)
    iy = integrate.quad(y_1,-nm.infty,1.1)
    y_2 = 1/(1+math.exp(-i*1.1))
    print(y_2)
print(iy)
