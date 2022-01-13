import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd

#------------データの読み込み----------------------
df = pd.read_csv('データ1013[162].csv')
data_A = list(df["1"][:539])
data_B = list(df["2"][:539])
data_C = list(df["3"][:539])
data_D = list(df["4"][:539])
data_E = list(df["5"][:539])
data_F = list(df["6"][:539])
data_G = list(df["7"][:539])
data_H = list(df["8"][:539])
data_I = list(df["9"][:539])
data_J = list(df["10"][:539])
data_K = list(df["11"][:539])
data_L = list(df["12"][:539])
data_M = list(df["13"][:539])
data_N = list(df["14"][:539])
data_O = list(df["15"][:539])

#----------------------合計を算出してリスト化-----------------
cut = [0 for i in range(539)]
for i in range(539):
    data_i = list(df.loc[i])
    if data_i[1] == 1:
        cut[i] += 1
    if data_i[2] == 1:
        cut[i] += 1
    if data_i[3] == 1:
        cut[i] += 1
    if data_i[4] == 1:
        cut[i] += 1
    if data_i[5] == 1:
        cut[i] += 1
    if data_i[6] == 1:
        cut[i] += 1
    if data_i[7] == 1:
        cut[i] += 1
    if data_i[8] == 1:
        cut[i] += 1
    if data_i[9] == 1:
        cut[i] += 1
    if data_i[10] == 1:
        cut[i] += 1
    if data_i[11] == 1:
        cut[i] += 1
    if data_i[12] == 1:
        cut[i] += 1
    if data_i[13] == 1:
        cut[i] += 1
    if data_i[14] == 1:
        cut[i] += 1
    if data_i[15] == 1:
        cut[i] += 1
#-----------合計をもとに得点順に並び替える------------------
# zipで一つの変数"zip_lists"にまとめる
# ソートの基準としたいリスト(ここではcut)を一番左においてzip
zip_lists = zip(cut,data_A,data_B,data_C,data_D,data_E,data_F,data_G,data_H,data_I,data_J,data_J,data_L,data_M,data_N,data_O)
# 昇順でソート
zip_sort = sorted(zip_lists)
# zipを解除
cut,data_A,data_B,data_C,data_D,data_E,data_F,data_G,data_H,data_I,data_J,data_J,data_L,data_M,data_N,data_O= zip(*zip_sort)

print(int(data_M))
