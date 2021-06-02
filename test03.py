import math
import numpy as nm
from scipy import integrate
from openpyxl import Workbook

y_1 =lambda x:(6*x)/(1+(2*x**2)+(x**4))
iy = integrate.quad(y_1,0,nm.infty)

#for i in range(1,11):
    #y_2 = 1/(1+math.exp(-1*(1+ (i/10))))
    #print(y_2)


print(iy)
