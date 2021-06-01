import math
import numpy as nm
from scipy import integrate
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
#wss = book['Sheet']


for i in range(1,11) :
    y_1 =lambda x: 1/(math.sqrt(2*math.pi))*math.exp(-x**2/2)
    iy = integrate.quad(y_1,-nm.infty,1)
    y_2 = 1/(1+math.exp(-1*(1+ (i/10))))
    ws.cell(row = i,column = 1).value = y_2
    ws.cell(row = i,column = 1).number_format = '0.0000000'
ws['B1'], ws['B2'] = iy
ws['B1'].number_format = '0.0000000'
wb.save('test.xlsx')
