cut = [i for i in range(30)]

import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd
import math
import sympy as sym


def p(a,b,x):
    cut_1 = -(1.7)*a*(x-b)
    y = math.log(math.e**cut_1)
    return y


ans_1 = np.roots([1,-1*3*np.sqrt(2)-3*np.sqrt(6),36])
#print(ans_1)
#print(3*np.sqrt(3))
a, b, c, x, y = sym.symbols("a b c x y")
expr = 2 * x ** 2 + 5 * x - 3
expr
# 微分を計算する
print(sym.Derivative(expr).doit())

# x について微分
expr = a * x ** 2 + b * x * y + c * y ** 2
#xについて微分してx=1を代入
print(sym.diff(expr, x))
