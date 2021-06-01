import math
import numpy as nm
from scipy import integrate
from openpyxl import Workbook

y_1 =lambda x: 1/(math.sqrt(2*math.pi))*math.exp(-x**2/2)
iy = integrate.quad(y_1,-nm.infty,1)

for i in range(1,11):
    y_2 = 1/(1+math.exp(-1*(1+ (i/10))))
    print(y_2)


print(iy)
