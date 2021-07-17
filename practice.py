import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core.accessor import register_index_accessor

df = pd.read_excel('項目特性実験データ.xlsx')
data_1 = list(df["名前"][:30])
data_goukei = list(df["合計"][:30])

data_A = list(df["問題A"][:30])
data_B = list(df["問題B"][:30])
data_C = list(df["問題C"][:30])
data_D = list(df["問題D"][:30])
data_E = list(df["問題E"][:30])
data_F = list(df["問題F"][:30])
data_G = list(df["問題G"][:30])
data_H = list(df["問題H"][:30])
cut = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(30):
    data_i = list(df.loc[i])
    if data_i[1] == 1:
        cut[i] += 1
    if data_i[2] == 3:
        cut[i] += 1
    if data_i[3] == 4:
        cut[i] += 1
    if data_i[4] == 4:
        cut[i] += 1
    if data_i[5] == 4:
        cut[i] += 1
    if data_i[6] == 3:
        cut[i] += 1
    if data_i[7] == 2:
        cut[i] += 1
    if data_i[8] == 4:
        cut[i] += 1
print(cut)

# zipで一つの変数"zip_lists"にまとめる
# ソートの基準としたいリスト(ここではscores)を一番左においてzip
zip_lists = zip(cut,data_1,data_A,data_B,data_C,data_D,data_E,data_F,data_G,data_H)
# 昇順でソート
zip_sort = sorted(zip_lists)
#zipを解除
cut,data_1,data_A,data_B,data_C,data_D,data_E,data_F,data_G,data_H= zip(*zip_sort)


print(data_1)
