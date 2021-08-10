import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd
#------------データの読み込み----------------------
df = pd.read_excel('Book30.xlsx')
data_1 = list(df["名前"][:30])
data_A = list(df["問題A"][:30])
data_B = list(df["問題B"][:30])
data_C = list(df["問題C"][:30])
data_D = list(df["問題D"][:30])
data_E = list(df["問題E"][:30])
data_F = list(df["問題F"][:30])
data_G = list(df["問題G"][:30])
data_H = list(df["問題H"][:30])
#----------------------合計を算出してリスト化-----------------
cut = [0 for i in range(30)]
for i in range(30):
    data_i = list(df.loc[i])
    if data_i[1] == 1:
        cut[i] += 1
    if data_i[2] == 4:
        cut[i] += 1
    if data_i[3] == 3:
        cut[i] += 1
    if data_i[4] == 3:
        cut[i] += 1
    if data_i[5] == 3:
        cut[i] += 1
    if data_i[6] == 1:
        cut[i] += 1
    if data_i[7] == 2:
        cut[i] += 1
    if data_i[8] == 4:
        cut[i] += 1
#-----------合計をもとに得点順に並び替える------------------
# zipで一つの変数"zip_lists"にまとめる
# ソートの基準としたいリスト(ここではcut)を一番左においてzip
zip_lists = zip(cut,data_1,data_A,data_B,data_C,data_D,data_E,data_F,data_G,data_H)
# 昇順でソート
zip_sort = sorted(zip_lists)
# zipを解除
cut,data_1,data_A,data_B,data_C,data_D,data_E,data_F,data_G,data_H= zip(*zip_sort)

#----------問題の答え-------------
data_A_ans = 1
data_B_ans = 4
data_C_ans = 3
data_D_ans = 3
data_E_ans = 3
data_F_ans = 1
data_G_ans = 2
data_H_ans = 4
#--------------合計点によって郡に分ける------------------
n = 5
data1 = cut[:n+1]
data2 = cut[n+1:n+7]
data3 = cut[n+7:n+13]
data4 = cut[n+13:n+19]
data5 = cut[n+19:n+25]
#--------------郡ごとの問題に対する答え------------------
#(A)
data_A_1 = data_A[:n+1]
data_A_2 = data_A[n+1:n+7]
data_A_3 = data_A[n+7:n+13]
data_A_4 = data_A[n+13:n+19]
data_A_5 = data_A[n+19:n+25]
#(B)
data_B_1 = data_B[:n+1]
data_B_2 = data_B[n+1:n+7]
data_B_3 = data_B[n+7:n+13]
data_B_4 = data_B[n+13:n+19]
data_B_5 = data_B[n+19:n+25]
#(C)
data_C_1 = data_C[:n+1]
data_C_2 = data_C[n+1:n+7]
data_C_3 = data_C[n+7:n+13]
data_C_4 = data_C[n+13:n+19]
data_C_5 = data_C[n+19:n+25]
#(D)
data_D_1 = data_D[:n+1]
data_D_2 = data_D[n+1:n+7]
data_D_3 = data_D[n+7:n+13]
data_D_4 = data_D[n+13:n+19]
data_D_5 = data_D[n+19:n+25]
#(E)
data_E_1 = data_E[:n+1]
data_E_2 = data_E[n+1:n+7]
data_E_3 = data_E[n+7:n+13]
data_E_4 = data_E[n+13:n+19]
data_E_5 = data_E[n+19:n+25]
#(F)
data_F_1 = data_F[:n+1]
data_F_2 = data_F[n+1:n+7]
data_F_3 = data_F[n+7:n+13]
data_F_4 = data_F[n+13:n+19]
data_F_5 = data_F[n+19:n+25]
#(G)
data_G_1 = data_G[:n+1]
data_G_2 = data_G[n+1:n+7]
data_G_3 = data_G[n+7:n+13]
data_G_4 = data_G[n+13:n+19]
data_G_5 = data_G[n+19:n+25]
#(H)
data_H_1 = data_H[:n+1]
data_H_2 = data_H[n+1:n+7]
data_H_3 = data_H[n+7:n+13]
data_H_4 = data_H[n+13:n+19]
data_H_5 = data_H[n+19:n+25]
#--------------問題に対して正しい選択肢を選んだ確率------------------
#(A)
#(a)
data_A = [[data_A_i] for i in range(4)]
data_A_1_theta_1 = int(format(data_A_1.count(1))) / len(data_A_1)
data_A_2_theta_1 = int(format(data_A_2.count(1))) / len(data_A_2)
data_A_3_theta_1 = int(format(data_A_3.count(1))) / len(data_A_3)
data_A_4_theta_1 = int(format(data_A_4.count(1))) / len(data_A_4)
data_A_5_theta_1 = int(format(data_A_5.count(1))) / len(data_A_5)
#(b)
data_A_1_theta_2 = int(format(data_A_1.count(2))) / len(data_A_1)
data_A_2_theta_2 = int(format(data_A_2.count(2))) / len(data_A_2)
data_A_3_theta_2 = int(format(data_A_3.count(2))) / len(data_A_3)
data_A_4_theta_2 = int(format(data_A_4.count(2))) / len(data_A_4)
data_A_5_theta_2 = int(format(data_A_5.count(2))) / len(data_A_5)
#(c)
data_A_1_theta_3 = int(format(data_A_1.count(3))) / len(data_A_1)
data_A_2_theta_3 = int(format(data_A_2.count(3))) / len(data_A_2)
data_A_3_theta_3 = int(format(data_A_3.count(3))) / len(data_A_3)
data_A_4_theta_3 = int(format(data_A_4.count(3))) / len(data_A_4)
data_A_5_theta_3 = int(format(data_A_5.count(3))) / len(data_A_5)
#(d)
data_A_1_theta_4 = int(format(data_A_1.count(4))) / len(data_A_1)
data_A_2_theta_4 = int(format(data_A_2.count(4))) / len(data_A_2)
data_A_3_theta_4 = int(format(data_A_3.count(4))) / len(data_A_3)
data_A_4_theta_4 = int(format(data_A_4.count(4))) / len(data_A_4)
data_A_5_theta_4 = int(format(data_A_5.count(4))) / len(data_A_5)

#(B)
#(a)
data_B_1_theta_1 = int(format(data_B_1.count(1))) / len(data_A_1)
data_B_2_theta_1 = int(format(data_B_2.count(1))) / len(data_A_2)
data_B_3_theta_1 = int(format(data_B_3.count(1))) / len(data_A_3)
data_B_4_theta_1 = int(format(data_B_4.count(1))) / len(data_A_4)
data_B_5_theta_1 = int(format(data_B_5.count(1))) / len(data_A_5)
#(b)
data_B_1_theta_2 = int(format(data_B_1.count(2))) / len(data_A_1)
data_B_2_theta_2 = int(format(data_B_2.count(2))) / len(data_A_2)
data_B_3_theta_2 = int(format(data_B_3.count(2))) / len(data_A_3)
data_B_4_theta_2 = int(format(data_B_4.count(2))) / len(data_A_4)
data_B_5_theta_2 = int(format(data_B_5.count(2))) / len(data_A_5)
#(c)
data_B_1_theta_3 = int(format(data_B_1.count(3))) / len(data_A_1)
data_B_2_theta_3 = int(format(data_B_2.count(3))) / len(data_A_2)
data_B_3_theta_3 = int(format(data_B_3.count(3))) / len(data_A_3)
data_B_4_theta_3 = int(format(data_B_4.count(3))) / len(data_A_4)
data_B_5_theta_3 = int(format(data_B_5.count(3))) / len(data_A_5)
#(d)
data_B_1_theta_4 = int(format(data_B_1.count(4))) / len(data_A_1)
data_B_2_theta_4 = int(format(data_B_2.count(4))) / len(data_A_2)
data_B_3_theta_4 = int(format(data_B_3.count(4))) / len(data_A_3)
data_B_4_theta_4 = int(format(data_B_4.count(4))) / len(data_A_4)
data_B_5_theta_4 = int(format(data_B_5.count(4))) / len(data_A_5)
#(C)
#(a)
data_C_1_theta_1 = int(format(data_C_1.count(1))) / len(data_A_1)
data_C_2_theta_1 = int(format(data_C_2.count(1))) / len(data_A_2)
data_C_3_theta_1 = int(format(data_C_3.count(1))) / len(data_A_3)
data_C_4_theta_1 = int(format(data_C_4.count(1))) / len(data_A_4)
data_C_5_theta_1 = int(format(data_C_5.count(1))) / len(data_A_5)
#(b)
data_C_1_theta_2 = int(format(data_C_1.count(2))) / len(data_A_1)
data_C_2_theta_2 = int(format(data_C_2.count(2))) / len(data_A_2)
data_C_3_theta_2 = int(format(data_C_3.count(2))) / len(data_A_3)
data_C_4_theta_2 = int(format(data_C_4.count(2))) / len(data_A_4)
data_C_5_theta_2 = int(format(data_C_5.count(2))) / len(data_A_5)
#(c)
data_C_1_theta_3 = int(format(data_C_1.count(3))) / len(data_A_1)
data_C_2_theta_3 = int(format(data_C_2.count(3))) / len(data_A_2)
data_C_3_theta_3 = int(format(data_C_3.count(3))) / len(data_A_3)
data_C_4_theta_3 = int(format(data_C_4.count(3))) / len(data_A_4)
data_C_5_theta_3 = int(format(data_C_5.count(3))) / len(data_A_5)
#(d)
data_C_1_theta_4 = int(format(data_C_1.count(4))) / len(data_A_1)
data_C_2_theta_4 = int(format(data_C_2.count(4))) / len(data_A_2)
data_C_3_theta_4 = int(format(data_C_3.count(4))) / len(data_A_3)
data_C_4_theta_4 = int(format(data_C_4.count(4))) / len(data_A_4)
data_C_5_theta_4 = int(format(data_C_5.count(4))) / len(data_A_5)
#(D)
#(a)
data_D_1_theta_1 = int(format(data_D_1.count(1))) / len(data_A_1)
data_D_2_theta_1 = int(format(data_D_2.count(1))) / len(data_A_2)
data_D_3_theta_1 = int(format(data_D_3.count(1))) / len(data_A_3)
data_D_4_theta_1 = int(format(data_D_4.count(1))) / len(data_A_4)
data_D_5_theta_1 = int(format(data_D_5.count(1))) / len(data_A_5)
#(b)
data_D_1_theta_2 = int(format(data_D_1.count(2))) / len(data_A_1)
data_D_2_theta_2 = int(format(data_D_2.count(2))) / len(data_A_2)
data_D_3_theta_2 = int(format(data_D_3.count(2))) / len(data_A_3)
data_D_4_theta_2 = int(format(data_D_4.count(2))) / len(data_A_4)
data_D_5_theta_2 = int(format(data_D_5.count(2))) / len(data_A_5)
#(c)
data_D_1_theta_3 = int(format(data_D_1.count(3))) / len(data_A_1)
data_D_2_theta_3 = int(format(data_D_2.count(3))) / len(data_A_2)
data_D_3_theta_3 = int(format(data_D_3.count(3))) / len(data_A_3)
data_D_4_theta_3 = int(format(data_D_4.count(3))) / len(data_A_4)
data_D_5_theta_3 = int(format(data_D_5.count(3))) / len(data_A_5)
#(d)
data_D_1_theta_4 = int(format(data_D_1.count(4))) / len(data_A_1)
data_D_2_theta_4 = int(format(data_D_2.count(4))) / len(data_A_2)
data_D_3_theta_4 = int(format(data_D_3.count(4))) / len(data_A_3)
data_D_4_theta_4 = int(format(data_D_4.count(4))) / len(data_A_4)
data_D_5_theta_4 = int(format(data_D_5.count(4))) / len(data_A_5)
#(E)
#(a)
data_E_1_theta_1 = int(format(data_E_1.count(1))) / len(data_A_1)
data_E_2_theta_1 = int(format(data_E_2.count(1))) / len(data_A_2)
data_E_3_theta_1 = int(format(data_E_3.count(1))) / len(data_A_3)
data_E_4_theta_1 = int(format(data_E_4.count(1))) / len(data_A_4)
data_E_5_theta_1 = int(format(data_E_5.count(1))) / len(data_A_5)
#(b)
data_E_1_theta_2 = int(format(data_E_1.count(2))) / len(data_A_1)
data_E_2_theta_2 = int(format(data_E_2.count(2))) / len(data_A_2)
data_E_3_theta_2 = int(format(data_E_3.count(2))) / len(data_A_3)
data_E_4_theta_2 = int(format(data_E_4.count(2))) / len(data_A_4)
data_E_5_theta_2 = int(format(data_E_5.count(2))) / len(data_A_5)
#(c)
data_E_1_theta_3 = int(format(data_E_1.count(3))) / len(data_A_1)
data_E_2_theta_3 = int(format(data_E_2.count(3))) / len(data_A_2)
data_E_3_theta_3 = int(format(data_E_3.count(3))) / len(data_A_3)
data_E_4_theta_3 = int(format(data_E_4.count(3))) / len(data_A_4)
data_E_5_theta_3 = int(format(data_E_5.count(3))) / len(data_A_5)
#(d)
data_E_1_theta_4 = int(format(data_E_1.count(4))) / len(data_A_1)
data_E_2_theta_4 = int(format(data_E_2.count(4))) / len(data_A_2)
data_E_3_theta_4 = int(format(data_E_3.count(4))) / len(data_A_3)
data_E_4_theta_4 = int(format(data_E_4.count(4))) / len(data_A_4)
data_E_5_theta_4 = int(format(data_E_5.count(4))) / len(data_A_5)
#(F)
#(a)
data_F_1_theta_1 = int(format(data_F_1.count(1))) / len(data_A_1)
data_F_2_theta_1 = int(format(data_F_2.count(1))) / len(data_A_2)
data_F_3_theta_1 = int(format(data_F_3.count(1))) / len(data_A_3)
data_F_4_theta_1 = int(format(data_F_4.count(1))) / len(data_A_4)
data_F_5_theta_1 = int(format(data_F_5.count(1))) / len(data_A_5)
#(b)
data_F_1_theta_2 = int(format(data_F_1.count(2))) / len(data_A_1)
data_F_2_theta_2 = int(format(data_F_2.count(2))) / len(data_A_2)
data_F_3_theta_2 = int(format(data_F_3.count(2))) / len(data_A_3)
data_F_4_theta_2 = int(format(data_F_4.count(2))) / len(data_A_4)
data_F_5_theta_2 = int(format(data_F_5.count(2))) / len(data_A_5)
#(c)
data_F_1_theta_3 = int(format(data_F_1.count(3))) / len(data_A_1)
data_F_2_theta_3 = int(format(data_F_2.count(3))) / len(data_A_2)
data_F_3_theta_3 = int(format(data_F_3.count(3))) / len(data_A_3)
data_F_4_theta_3 = int(format(data_F_4.count(3))) / len(data_A_4)
data_F_5_theta_3 = int(format(data_F_5.count(3))) / len(data_A_5)
#(d)
data_F_1_theta_4 = int(format(data_F_1.count(4))) / len(data_A_1)
data_F_2_theta_4 = int(format(data_F_2.count(4))) / len(data_A_2)
data_F_3_theta_4 = int(format(data_F_3.count(4))) / len(data_A_3)
data_F_4_theta_4 = int(format(data_F_4.count(4))) / len(data_A_4)
data_F_5_theta_4 = int(format(data_F_5.count(4))) / len(data_A_5)
#(G)
#(a)
data_G_1_theta_1 = int(format(data_G_1.count(1))) / len(data_A_1)
data_G_2_theta_1 = int(format(data_G_2.count(1))) / len(data_A_2)
data_G_3_theta_1 = int(format(data_G_3.count(1))) / len(data_A_3)
data_G_4_theta_1 = int(format(data_G_4.count(1))) / len(data_A_4)
data_G_5_theta_1 = int(format(data_G_5.count(1))) / len(data_A_5)
#(b)
data_G_1_theta_2 = int(format(data_G_1.count(2))) / len(data_A_1)
data_G_2_theta_2 = int(format(data_G_2.count(2))) / len(data_A_2)
data_G_3_theta_2 = int(format(data_G_3.count(2))) / len(data_A_3)
data_G_4_theta_2 = int(format(data_G_4.count(2))) / len(data_A_4)
data_G_5_theta_2 = int(format(data_G_5.count(2))) / len(data_A_5)
#(c)
data_G_1_theta_3 = int(format(data_G_1.count(3))) / len(data_A_1)
data_G_2_theta_3 = int(format(data_G_2.count(3))) / len(data_A_2)
data_G_3_theta_3 = int(format(data_G_3.count(3))) / len(data_A_3)
data_G_4_theta_3 = int(format(data_G_4.count(3))) / len(data_A_4)
data_G_5_theta_3 = int(format(data_G_5.count(3))) / len(data_A_5)
#(d)
data_G_1_theta_4 = int(format(data_G_1.count(4))) / len(data_A_1)
data_G_2_theta_4 = int(format(data_G_2.count(4))) / len(data_A_2)
data_G_3_theta_4 = int(format(data_G_3.count(4))) / len(data_A_3)
data_G_4_theta_4 = int(format(data_G_4.count(4))) / len(data_A_4)
data_G_5_theta_4 = int(format(data_G_5.count(4))) / len(data_A_5)
#(H)
#(a)
data_H_1_theta_1 = int(format(data_H_1.count(1))) / len(data_A_1)
data_H_2_theta_1 = int(format(data_H_2.count(1))) / len(data_A_2)
data_H_3_theta_1 = int(format(data_H_3.count(1))) / len(data_A_3)
data_H_4_theta_1 = int(format(data_H_4.count(1))) / len(data_A_4)
data_H_5_theta_1 = int(format(data_H_5.count(1))) / len(data_A_5)
#(b)
data_H_1_theta_2 = int(format(data_H_1.count(2))) / len(data_A_1)
data_H_2_theta_2 = int(format(data_H_2.count(2))) / len(data_A_2)
data_H_3_theta_2 = int(format(data_H_3.count(2))) / len(data_A_3)
data_H_4_theta_2 = int(format(data_H_4.count(2))) / len(data_A_4)
data_H_5_theta_2 = int(format(data_H_5.count(2))) / len(data_A_5)
#(c)
data_H_1_theta_3 = int(format(data_H_1.count(3))) / len(data_A_1)
data_H_2_theta_3 = int(format(data_H_2.count(3))) / len(data_A_2)
data_H_3_theta_3 = int(format(data_H_3.count(3))) / len(data_A_3)
data_H_4_theta_3 = int(format(data_H_4.count(3))) / len(data_A_4)
data_H_5_theta_3 = int(format(data_H_5.count(3))) / len(data_A_5)
#(d)
data_H_1_theta_4 = int(format(data_H_1.count(4))) / len(data_A_1)
data_H_2_theta_4 = int(format(data_H_2.count(4))) / len(data_A_2)
data_H_3_theta_4 = int(format(data_H_3.count(4))) / len(data_A_3)
data_H_4_theta_4 = int(format(data_H_4.count(4))) / len(data_A_4)
data_H_5_theta_4 = int(format(data_H_5.count(4))) / len(data_A_5)
#----------------------------グラフの値の生成---------------------
#(A)
#(a)
y_A_1 = np.array([data_A_1_theta_1,data_A_2_theta_1,data_A_3_theta_1,data_A_4_theta_1,data_A_5_theta_1])
#(b)
y_A_2 = np.array([data_A_1_theta_2,data_A_2_theta_2,data_A_3_theta_2,data_A_4_theta_2,data_A_5_theta_2])
#(c)
y_A_3 = np.array([data_A_1_theta_3,data_A_2_theta_3,data_A_3_theta_3,data_A_4_theta_3,data_A_5_theta_3])
#(d)
y_A_4 = np.array([data_A_1_theta_4,data_A_2_theta_4,data_A_3_theta_4,data_A_4_theta_4,data_A_5_theta_4])

#(B)
#(a)
y_B_1 = np.array([data_B_1_theta_1,data_B_2_theta_1,data_B_3_theta_1,data_B_4_theta_1,data_B_5_theta_1])
#(b)
y_B_2 = np.array([data_B_1_theta_2,data_B_2_theta_2,data_B_3_theta_2,data_B_4_theta_2,data_B_5_theta_2])
#(c)
y_B_3 = np.array([data_B_1_theta_3,data_B_2_theta_3,data_B_3_theta_3,data_B_4_theta_3,data_B_5_theta_3])
#(d)
y_B_4 = np.array([data_B_1_theta_4,data_B_2_theta_4,data_B_3_theta_4,data_B_4_theta_4,data_B_5_theta_4])
#(C)
#(a)
y_C_1 = np.array([data_C_1_theta_1,data_C_2_theta_1,data_C_3_theta_1,data_C_4_theta_1,data_C_5_theta_1])
#(b)
y_C_2 = np.array([data_C_1_theta_2,data_C_2_theta_2,data_C_3_theta_2,data_C_4_theta_2,data_C_5_theta_2])
#(c)
y_C_3 = np.array([data_C_1_theta_3,data_C_2_theta_3,data_C_3_theta_3,data_C_4_theta_3,data_C_5_theta_3])
#(d)
y_C_4 = np.array([data_C_1_theta_4,data_C_2_theta_4,data_C_3_theta_4,data_C_4_theta_4,data_C_5_theta_4])
#(D)
#(a)
y_D_1 = np.array([data_D_1_theta_1,data_D_2_theta_1,data_D_3_theta_1,data_D_4_theta_1,data_D_5_theta_1])
#(b)
y_D_2 = np.array([data_D_1_theta_2,data_D_2_theta_2,data_D_3_theta_2,data_D_4_theta_2,data_D_5_theta_2])
#(c)
y_D_3 = np.array([data_D_1_theta_3,data_D_2_theta_3,data_D_3_theta_3,data_D_4_theta_3,data_D_5_theta_3])
#(d)
y_D_4 = np.array([data_D_1_theta_4,data_D_2_theta_4,data_D_3_theta_4,data_D_4_theta_4,data_D_5_theta_4])
#(E)
#(a)
y_E_1 = np.array([data_E_1_theta_1,data_E_2_theta_1,data_E_3_theta_1,data_E_4_theta_1,data_E_5_theta_1])
#(b)
y_E_2 = np.array([data_E_1_theta_2,data_E_2_theta_2,data_E_3_theta_2,data_E_4_theta_2,data_E_5_theta_2])
#(c)
y_E_3 = np.array([data_E_1_theta_3,data_E_2_theta_3,data_E_3_theta_3,data_E_4_theta_3,data_E_5_theta_3])
#(d)
y_E_4 = np.array([data_E_1_theta_4,data_E_2_theta_4,data_E_3_theta_4,data_E_4_theta_4,data_E_5_theta_4])
#(F)
#(a)
y_F_1 = np.array([data_F_1_theta_1,data_F_2_theta_1,data_F_3_theta_1,data_F_4_theta_1,data_F_5_theta_1])
#(b)
y_F_2 = np.array([data_F_1_theta_2,data_F_2_theta_2,data_F_3_theta_2,data_F_4_theta_2,data_F_5_theta_2])
#(c)
y_F_3 = np.array([data_F_1_theta_3,data_F_2_theta_3,data_F_3_theta_3,data_F_4_theta_3,data_F_5_theta_3])
#(d)
y_F_4 = np.array([data_F_1_theta_4,data_F_2_theta_4,data_F_3_theta_4,data_F_4_theta_4,data_F_5_theta_4])
#(G)
#(a)
y_G_1 = np.array([data_G_1_theta_1,data_G_2_theta_1,data_G_3_theta_1,data_G_4_theta_1,data_G_5_theta_1])
#(b)
y_G_2 = np.array([data_G_1_theta_2,data_G_2_theta_2,data_G_3_theta_2,data_G_4_theta_2,data_G_5_theta_2])
#(c)
y_G_3 = np.array([data_G_1_theta_3,data_G_2_theta_3,data_G_3_theta_3,data_G_4_theta_3,data_G_5_theta_3])
#(d)
y_G_4 = np.array([data_G_1_theta_4,data_G_2_theta_4,data_G_3_theta_4,data_G_4_theta_4,data_G_5_theta_4])
#(H)
#(a)
y_H_1 = np.array([data_H_1_theta_1,data_H_2_theta_1,data_H_3_theta_1,data_H_4_theta_1,data_H_5_theta_1])
#(b)
y_H_2 = np.array([data_H_1_theta_2,data_H_2_theta_2,data_H_3_theta_2,data_H_4_theta_2,data_H_5_theta_2])
#(c)
y_H_3 = np.array([data_H_1_theta_3,data_H_2_theta_3,data_H_3_theta_3,data_H_4_theta_3,data_H_5_theta_3])
#(d)
y_H_4 = np.array([data_H_1_theta_4,data_H_2_theta_4,data_H_3_theta_4,data_H_4_theta_4,data_H_5_theta_4])
x = np.array([1,2,3,4,5])
#-------------グラフの位置の設定-----------------
#(A)
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(421)
ax1.plot(x,y_A_1, marker="$a$", linewidth= 2, linestyle = "solid")
ax1.plot(x,y_A_2, marker="$b$", linewidth= 2, linestyle = "dashed")
ax1.plot(x,y_A_3, marker="$c$", linewidth= 2, linestyle = "dashed")
ax1.plot(x,y_A_4, marker="$d$", linewidth= 2, linestyle = "dashed")
ax1.set_title("教育史(a)")
#(B)
ax2 = fig.add_subplot(422)
ax2.plot(x,y_B_1, marker="$a$", linewidth= 2, linestyle = "dashed")
ax2.plot(x,y_B_2, marker="$b$", linewidth= 2, linestyle = "dashed")
ax2.plot(x,y_B_3, marker="$c$", linewidth= 2, linestyle = "dashed")
ax2.plot(x,y_B_4, marker="$d$", linewidth= 2, linestyle = "solid")
ax2.set_title("教育史(b)")
#(C)
ax3 = fig.add_subplot(423)
ax3.plot(x,y_C_1, marker="$a$", linewidth= 2, linestyle = "dashed")
ax3.plot(x,y_C_2, marker="$b$", linewidth= 2, linestyle = "dashed")
ax3.plot(x,y_C_3, marker="$c$", linewidth= 2, linestyle = "solid")
ax3.plot(x,y_C_4, marker="$d$", linewidth= 2, linestyle = "dashed")
ax3.set_title("教育原理")
#(D)
ax4 = fig.add_subplot(424)
ax4.plot(x,y_D_1, marker="$a$", linewidth= 2, linestyle = "dashed")
ax4.plot(x,y_D_2, marker="$b$", linewidth= 2, linestyle = "dashed")
ax4.plot(x,y_D_3, marker="$c$", linewidth= 2, linestyle = "solid")
ax4.plot(x,y_D_4, marker="$d$", linewidth= 2, linestyle = "dashed")
ax4.set_title("教育法規[1]")
#(E)
ax5 = fig.add_subplot(425)
ax5.plot(x,y_E_1, marker="$a$", linewidth= 2, linestyle = "dashed")
ax5.plot(x,y_E_2, marker="$b$", linewidth= 2, linestyle = "dashed")
ax5.plot(x,y_E_3, marker="$c$", linewidth= 2, linestyle = "solid")
ax5.plot(x,y_E_4, marker="$d$", linewidth= 2, linestyle = "dashed")
ax5.set_title("教育法規[2]")
#(F)
ax6 = fig.add_subplot(426)
ax6.plot(x,y_F_1, marker="$a$", linewidth= 2, linestyle = "solid")
ax6.plot(x,y_F_2, marker="$b$", linewidth= 2, linestyle = "dashed")
ax6.plot(x,y_F_3, marker="$c$", linewidth= 2, linestyle = "dashed")
ax6.plot(x,y_F_4, marker="$d$", linewidth= 2, linestyle = "dashed")
ax6.set_title("教育心理(a)")
#(G)
ax7 = fig.add_subplot(427)
ax7.plot(x,y_G_1, marker="$a$", linewidth= 2, linestyle = "dashed")
ax7.plot(x,y_G_2, marker="$b$", linewidth= 2, linestyle = "solid")
ax7.plot(x,y_G_3, marker="$c$", linewidth= 2, linestyle = "dashed")
ax7.plot(x,y_G_4, marker="$d$", linewidth= 2, linestyle = "dashed")
ax7.set_title("教育心理(b)")
#(H)
ax8 = fig.add_subplot(428)
ax8.plot(x,y_H_1, marker="$a$", linewidth= 2, linestyle = "dashed")
ax8.plot(x,y_H_2, marker="$b$", linewidth= 2, linestyle = "dashed")
ax8.plot(x,y_H_3, marker="$c$", linewidth= 2, linestyle = "dashed")
ax8.plot(x,y_H_4, marker="$d$", linewidth= 2, linestyle = "solid")
ax8.set_title("教育心理(c)")
#----------グラフの生成----------
plt.xticks([ 1,2,3,4,5 ])
plt.tight_layout()
plt.show()
