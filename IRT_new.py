import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd
import math
import sympy as sym

#データの読み込み------------------------
df = pd.read_csv('データ1013[162].csv')

#人数、項目数---------------------------
num_item = 15
num_users = 539

#式の定義---------------------------------
#2母数ロジスティックモデル-----------------
def L2P(a,b,x):
    return 1/ (1 + (-1.7) * np.exp(-a*(x-b)))

#上記の微分------------------------------
def dL2P(a,b,x):
    da = sym.diff(L2P,a)
    db = sym.diff(L2P,b)
    dx = sym.diff(L2P,x)
    return [da,db,dx]

#3母数ロジスティックモデル-----------------
def L3P(a,b,c,x):
    return (1 - c) / (1 + (-1.7) * np.exp(-a*(x-b)))

#上記の微分------------------------------
def dL3P(a,b,c,x):
    da = sym.diff(L2P,a)
    db = sym.diff(L2P,b)
    dc = sym.diff(L2P,c)
    dx = sym.diff(L2P,x)
    return [da,db,dc,dx]


#項目母数の推定(最尤推定法)------------------------------
