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

#----------問題の答え-------------
data_A_ans = 1
data_B_ans = 1
data_C_ans = 1
data_D_ans = 1
data_E_ans = 1
data_F_ans = 1
data_G_ans = 1
data_H_ans = 1
data_I_ans = 1
data_J_ans = 1
data_K_ans = 1
data_L_ans = 1
data_M_ans = 1
data_N_ans = 1
data_O_ans = 1
#--------------合計点によって郡に分ける------------------
n = 5
data1 = cut[:n+107]
data2 = cut[n+107:n+213]
data3 = cut[n+213:n+320]
data4 = cut[n+320:n+427]
data5 = cut[n+427:n+534]
#--------------郡ごとの問題に対する答え------------------
#(A)
data_A_1 = data_A[:n+107]
data_A_2 = data_A[n+107:n+213]
data_A_3 = data_A[n+213:n+320]
data_A_4 = data_A[n+320:n+427]
data_A_5 = data_A[n+427:n+534]
#(B)
data_B_1 = data_B[:n+107]
data_B_2 = data_B[n+107:n+213]
data_B_3 = data_B[n+213:n+320]
data_B_4 = data_B[n+320:n+427]
data_B_5 = data_B[n+427:n+534]
#(C)
data_C_1 = data_C[:n+107]
data_C_2 = data_C[n+107:n+213]
data_C_3 = data_C[n+213:n+320]
data_C_4 = data_C[n+320:n+427]
data_C_5 = data_C[n+427:n+534]
#(D)
data_D_1 = data_D[:n+107]
data_D_2 = data_D[n+107:n+213]
data_D_3 = data_D[n+213:n+320]
data_D_4 = data_D[n+320:n+427]
data_D_5 = data_D[n+427:n+534]
#(E)
data_E_1 = data_E[:n+107]
data_E_2 = data_E[n+107:n+213]
data_E_3 = data_E[n+213:n+320]
data_E_4 = data_E[n+320:n+427]
data_E_5 = data_E[n+427:n+534]
#(F)
data_F_1 = data_F[:n+107]
data_F_2 = data_F[n+107:n+213]
data_F_3 = data_F[n+213:n+320]
data_F_4 = data_F[n+320:n+427]
data_F_5 = data_F[n+427:n+534]
#(G)
data_G_1 = data_G[:n+107]
data_G_2 = data_G[n+107:n+213]
data_G_3 = data_G[n+213:n+320]
data_G_4 = data_G[n+320:n+427]
data_G_5 = data_G[n+427:n+534]
#(H)
data_H_1 = data_H[:n+107]
data_H_2 = data_H[n+107:n+213]
data_H_3 = data_H[n+213:n+320]
data_H_4 = data_H[n+320:n+427]
data_H_5 = data_H[n+427:n+534]
#(I)
data_I_1 = data_I[:n+107]
data_I_2 = data_I[n+107:n+213]
data_I_3 = data_I[n+213:n+320]
data_I_4 = data_I[n+320:n+427]
data_I_5 = data_I[n+427:n+534]
#(J)
data_J_1 = data_J[:n+107]
data_J_2 = data_J[n+107:n+213]
data_J_3 = data_J[n+213:n+320]
data_J_4 = data_J[n+320:n+427]
data_J_5 = data_J[n+427:n+534]
#(K)
data_K_1 = data_K[:n+107]
data_K_2 = data_K[n+107:n+213]
data_K_3 = data_K[n+213:n+320]
data_K_4 = data_K[n+320:n+427]
data_K_5 = data_K[n+427:n+534]
#(L)
data_L_1 = data_L[:n+107]
data_L_2 = data_L[n+107:n+213]
data_L_3 = data_L[n+213:n+320]
data_L_4 = data_L[n+320:n+427]
data_L_5 = data_L[n+427:n+534]
#(M)
data_M_1 = data_M[:n+107]
data_M_2 = data_M[n+107:n+213]
data_M_3 = data_M[n+213:n+320]
data_M_4 = data_M[n+320:n+427]
data_M_5 = data_M[n+427:n+534]
#(N)
data_N_1 = data_N[:n+107]
data_N_2 = data_N[n+107:n+213]
data_N_3 = data_N[n+213:n+320]
data_N_4 = data_N[n+320:n+427]
data_N_5 = data_N[n+427:n+534]
#(O)
data_O_1 = data_O[:n+107]
data_O_2 = data_O[n+107:n+213]
data_O_3 = data_O[n+213:n+320]
data_O_4 = data_O[n+320:n+427]
data_O_5 = data_O[n+427:n+534]
#--------------問題に対して正しい選択肢を選んだ確率------------------
#(A)
#(a)
#data_A = [[data_A_i] for i in range(4)]
data_A_1_theta_1 = int(format(data_A_1.count(1))) / len(data_A_1)
data_A_2_theta_1 = int(format(data_A_2.count(1))) / len(data_A_2)
data_A_3_theta_1 = int(format(data_A_3.count(1))) / len(data_A_3)
data_A_4_theta_1 = int(format(data_A_4.count(1))) / len(data_A_4)
data_A_5_theta_1 = int(format(data_A_5.count(1))) / len(data_A_5)
#(b)
data_A_1_theta_2 = int(format(data_A_1.count(0))) / len(data_A_1)
data_A_2_theta_2 = int(format(data_A_2.count(0))) / len(data_A_2)
data_A_3_theta_2 = int(format(data_A_3.count(0))) / len(data_A_3)
data_A_4_theta_2 = int(format(data_A_4.count(0))) / len(data_A_4)
data_A_5_theta_2 = int(format(data_A_5.count(0))) / len(data_A_5)


#(B)
#(a)
data_B_1_theta_1 = int(format(data_B_1.count(1))) / len(data_A_1)
data_B_2_theta_1 = int(format(data_B_2.count(1))) / len(data_A_2)
data_B_3_theta_1 = int(format(data_B_3.count(1))) / len(data_A_3)
data_B_4_theta_1 = int(format(data_B_4.count(1))) / len(data_A_4)
data_B_5_theta_1 = int(format(data_B_5.count(1))) / len(data_A_5)
#(b)
data_B_1_theta_2 = int(format(data_B_1.count(0))) / len(data_A_1)
data_B_2_theta_2 = int(format(data_B_2.count(0))) / len(data_A_2)
data_B_3_theta_2 = int(format(data_B_3.count(0))) / len(data_A_3)
data_B_4_theta_2 = int(format(data_B_4.count(0))) / len(data_A_4)
data_B_5_theta_2 = int(format(data_B_5.count(0))) / len(data_A_5)

#(C)
#(a)
data_C_1_theta_1 = int(format(data_C_1.count(1))) / len(data_A_1)
data_C_2_theta_1 = int(format(data_C_2.count(1))) / len(data_A_2)
data_C_3_theta_1 = int(format(data_C_3.count(1))) / len(data_A_3)
data_C_4_theta_1 = int(format(data_C_4.count(1))) / len(data_A_4)
data_C_5_theta_1 = int(format(data_C_5.count(1))) / len(data_A_5)
#(b)
data_C_1_theta_2 = int(format(data_C_1.count(0))) / len(data_A_1)
data_C_2_theta_2 = int(format(data_C_2.count(0))) / len(data_A_2)
data_C_3_theta_2 = int(format(data_C_3.count(0))) / len(data_A_3)
data_C_4_theta_2 = int(format(data_C_4.count(0))) / len(data_A_4)
data_C_5_theta_2 = int(format(data_C_5.count(0))) / len(data_A_5)

#(D)
#(a)
data_D_1_theta_1 = int(format(data_D_1.count(1))) / len(data_A_1)
data_D_2_theta_1 = int(format(data_D_2.count(1))) / len(data_A_2)
data_D_3_theta_1 = int(format(data_D_3.count(1))) / len(data_A_3)
data_D_4_theta_1 = int(format(data_D_4.count(1))) / len(data_A_4)
data_D_5_theta_1 = int(format(data_D_5.count(1))) / len(data_A_5)
#(b)
data_D_1_theta_2 = int(format(data_D_1.count(0))) / len(data_A_1)
data_D_2_theta_2 = int(format(data_D_2.count(0))) / len(data_A_2)
data_D_3_theta_2 = int(format(data_D_3.count(0))) / len(data_A_3)
data_D_4_theta_2 = int(format(data_D_4.count(0))) / len(data_A_4)
data_D_5_theta_2 = int(format(data_D_5.count(0))) / len(data_A_5)

#(E)
#(a)
data_E_1_theta_1 = int(format(data_E_1.count(1))) / len(data_A_1)
data_E_2_theta_1 = int(format(data_E_2.count(1))) / len(data_A_2)
data_E_3_theta_1 = int(format(data_E_3.count(1))) / len(data_A_3)
data_E_4_theta_1 = int(format(data_E_4.count(1))) / len(data_A_4)
data_E_5_theta_1 = int(format(data_E_5.count(1))) / len(data_A_5)
#(b)
data_E_1_theta_2 = int(format(data_E_1.count(0))) / len(data_A_1)
data_E_2_theta_2 = int(format(data_E_2.count(0))) / len(data_A_2)
data_E_3_theta_2 = int(format(data_E_3.count(0))) / len(data_A_3)
data_E_4_theta_2 = int(format(data_E_4.count(0))) / len(data_A_4)
data_E_5_theta_2 = int(format(data_E_5.count(0))) / len(data_A_5)

#(F)
#(a)
data_F_1_theta_1 = int(format(data_F_1.count(1))) / len(data_A_1)
data_F_2_theta_1 = int(format(data_F_2.count(1))) / len(data_A_2)
data_F_3_theta_1 = int(format(data_F_3.count(1))) / len(data_A_3)
data_F_4_theta_1 = int(format(data_F_4.count(1))) / len(data_A_4)
data_F_5_theta_1 = int(format(data_F_5.count(1))) / len(data_A_5)
#(b)
data_F_1_theta_2 = int(format(data_F_1.count(0))) / len(data_A_1)
data_F_2_theta_2 = int(format(data_F_2.count(0))) / len(data_A_2)
data_F_3_theta_2 = int(format(data_F_3.count(0))) / len(data_A_3)
data_F_4_theta_2 = int(format(data_F_4.count(0))) / len(data_A_4)
data_F_5_theta_2 = int(format(data_F_5.count(0))) / len(data_A_5)

#(G)
#(a)
data_G_1_theta_1 = int(format(data_G_1.count(1))) / len(data_A_1)
data_G_2_theta_1 = int(format(data_G_2.count(1))) / len(data_A_2)
data_G_3_theta_1 = int(format(data_G_3.count(1))) / len(data_A_3)
data_G_4_theta_1 = int(format(data_G_4.count(1))) / len(data_A_4)
data_G_5_theta_1 = int(format(data_G_5.count(1))) / len(data_A_5)
#(b)
data_G_1_theta_2 = int(format(data_G_1.count(0))) / len(data_A_1)
data_G_2_theta_2 = int(format(data_G_2.count(0))) / len(data_A_2)
data_G_3_theta_2 = int(format(data_G_3.count(0))) / len(data_A_3)
data_G_4_theta_2 = int(format(data_G_4.count(0))) / len(data_A_4)
data_G_5_theta_2 = int(format(data_G_5.count(0))) / len(data_A_5)

#(H)
#(a)
data_H_1_theta_1 = int(format(data_H_1.count(1))) / len(data_A_1)
data_H_2_theta_1 = int(format(data_H_2.count(1))) / len(data_A_2)
data_H_3_theta_1 = int(format(data_H_3.count(1))) / len(data_A_3)
data_H_4_theta_1 = int(format(data_H_4.count(1))) / len(data_A_4)
data_H_5_theta_1 = int(format(data_H_5.count(1))) / len(data_A_5)
#(b)
data_H_1_theta_2 = int(format(data_H_1.count(0))) / len(data_A_1)
data_H_2_theta_2 = int(format(data_H_2.count(0))) / len(data_A_2)
data_H_3_theta_2 = int(format(data_H_3.count(0))) / len(data_A_3)
data_H_4_theta_2 = int(format(data_H_4.count(0))) / len(data_A_4)
data_H_5_theta_2 = int(format(data_H_5.count(0))) / len(data_A_5)

#(I)
#(a)
data_I_1_theta_1 = int(format(data_I_1.count(1))) / len(data_A_1)
data_I_2_theta_1 = int(format(data_I_2.count(1))) / len(data_A_2)
data_I_3_theta_1 = int(format(data_I_3.count(1))) / len(data_A_3)
data_I_4_theta_1 = int(format(data_I_4.count(1))) / len(data_A_4)
data_I_5_theta_1 = int(format(data_I_5.count(1))) / len(data_A_5)
#(b)
data_I_1_theta_2 = int(format(data_I_1.count(0))) / len(data_A_1)
data_I_2_theta_2 = int(format(data_I_2.count(0))) / len(data_A_2)
data_I_3_theta_2 = int(format(data_I_3.count(0))) / len(data_A_3)
data_I_4_theta_2 = int(format(data_I_4.count(0))) / len(data_A_4)
data_I_5_theta_2 = int(format(data_I_5.count(0))) / len(data_A_5)

#(J)
#(a)
data_J_1_theta_1 = int(format(data_J_1.count(1))) / len(data_A_1)
data_J_2_theta_1 = int(format(data_J_2.count(1))) / len(data_A_2)
data_J_3_theta_1 = int(format(data_J_3.count(1))) / len(data_A_3)
data_J_4_theta_1 = int(format(data_J_4.count(1))) / len(data_A_4)
data_J_5_theta_1 = int(format(data_J_5.count(1))) / len(data_A_5)
#(b)
data_J_1_theta_2 = int(format(data_J_1.count(0))) / len(data_A_1)
data_J_2_theta_2 = int(format(data_J_2.count(0))) / len(data_A_2)
data_J_3_theta_2 = int(format(data_J_3.count(0))) / len(data_A_3)
data_J_4_theta_2 = int(format(data_J_4.count(0))) / len(data_A_4)
data_J_5_theta_2 = int(format(data_J_5.count(0))) / len(data_A_5)

#(K)
#(a)
data_K_1_theta_1 = int(format(data_K_1.count(1))) / len(data_A_1)
data_K_2_theta_1 = int(format(data_K_2.count(1))) / len(data_A_2)
data_K_3_theta_1 = int(format(data_K_3.count(1))) / len(data_A_3)
data_K_4_theta_1 = int(format(data_K_4.count(1))) / len(data_A_4)
data_K_5_theta_1 = int(format(data_K_5.count(1))) / len(data_A_5)
#(b)
data_K_1_theta_2 = int(format(data_K_1.count(0))) / len(data_A_1)
data_K_2_theta_2 = int(format(data_K_2.count(0))) / len(data_A_2)
data_K_3_theta_2 = int(format(data_K_3.count(0))) / len(data_A_3)
data_K_4_theta_2 = int(format(data_K_4.count(0))) / len(data_A_4)
data_K_5_theta_2 = int(format(data_K_5.count(0))) / len(data_A_5)
#(L)
#(a)
data_L_1_theta_1 = int(format(data_L_1.count(1))) / len(data_A_1)
data_L_2_theta_1 = int(format(data_L_2.count(1))) / len(data_A_2)
data_L_3_theta_1 = int(format(data_L_3.count(1))) / len(data_A_3)
data_L_4_theta_1 = int(format(data_L_4.count(1))) / len(data_A_4)
data_L_5_theta_1 = int(format(data_L_5.count(1))) / len(data_A_5)
#(b)
data_L_1_theta_2 = int(format(data_L_1.count(0))) / len(data_A_1)
data_L_2_theta_2 = int(format(data_L_2.count(0))) / len(data_A_2)
data_L_3_theta_2 = int(format(data_L_3.count(0))) / len(data_A_3)
data_L_4_theta_2 = int(format(data_L_4.count(0))) / len(data_A_4)
data_L_5_theta_2 = int(format(data_L_5.count(0))) / len(data_A_5)
#(M)
#(a)
data_M_1_theta_1 = int(format(data_M_1.count(1))) / len(data_A_1)
data_M_2_theta_1 = int(format(data_M_2.count(1))) / len(data_A_2)
data_M_3_theta_1 = int(format(data_M_3.count(1))) / len(data_A_3)
data_M_4_theta_1 = int(format(data_M_4.count(1))) / len(data_A_4)
data_M_5_theta_1 = int(format(data_M_5.count(1))) / len(data_A_5)
#(b)
data_M_1_theta_2 = int(format(data_M_1.count(0))) / len(data_A_1)
data_M_2_theta_2 = int(format(data_M_2.count(0))) / len(data_A_2)
data_M_3_theta_2 = int(format(data_M_3.count(0))) / len(data_A_3)
data_M_4_theta_2 = int(format(data_M_4.count(0))) / len(data_A_4)
data_M_5_theta_2 = int(format(data_M_5.count(0))) / len(data_A_5)
#(N)
#(a)
data_N_1_theta_1 = int(format(data_N_1.count(1))) / len(data_A_1)
data_N_2_theta_1 = int(format(data_N_2.count(1))) / len(data_A_2)
data_N_3_theta_1 = int(format(data_N_3.count(1))) / len(data_A_3)
data_N_4_theta_1 = int(format(data_N_4.count(1))) / len(data_A_4)
data_N_5_theta_1 = int(format(data_N_5.count(1))) / len(data_A_5)
#(b)
data_N_1_theta_2 = int(format(data_N_1.count(0))) / len(data_A_1)
data_N_2_theta_2 = int(format(data_N_2.count(0))) / len(data_A_2)
data_N_3_theta_2 = int(format(data_N_3.count(0))) / len(data_A_3)
data_N_4_theta_2 = int(format(data_N_4.count(0))) / len(data_A_4)
data_N_5_theta_2 = int(format(data_N_5.count(0))) / len(data_A_5)
#(O)
#(a)
data_O_1_theta_1 = int(format(data_O_1.count(1))) / len(data_A_1)
data_O_2_theta_1 = int(format(data_O_2.count(1))) / len(data_A_2)
data_O_3_theta_1 = int(format(data_O_3.count(1))) / len(data_A_3)
data_O_4_theta_1 = int(format(data_O_4.count(1))) / len(data_A_4)
data_O_5_theta_1 = int(format(data_O_5.count(1))) / len(data_A_5)
#(b)
data_O_1_theta_2 = int(format(data_O_1.count(0))) / len(data_A_1)
data_O_2_theta_2 = int(format(data_O_2.count(0))) / len(data_A_2)
data_O_3_theta_2 = int(format(data_O_3.count(0))) / len(data_A_3)
data_O_4_theta_2 = int(format(data_O_4.count(0))) / len(data_A_4)
data_O_5_theta_2 = int(format(data_O_5.count(0))) / len(data_A_5)
#----------------------------グラフの値の生成---------------------
#(A)
#(a)
y_A_1 = np.array([data_A_1_theta_1,data_A_2_theta_1,data_A_3_theta_1,data_A_4_theta_1,data_A_5_theta_1])
#(b)
y_A_2 = np.array([data_A_1_theta_2,data_A_2_theta_2,data_A_3_theta_2,data_A_4_theta_2,data_A_5_theta_2])

#(B)
#(a)
y_B_1 = np.array([data_B_1_theta_1,data_B_2_theta_1,data_B_3_theta_1,data_B_4_theta_1,data_B_5_theta_1])
#(b)
y_B_2 = np.array([data_B_1_theta_2,data_B_2_theta_2,data_B_3_theta_2,data_B_4_theta_2,data_B_5_theta_2])

#(C)
#(a)
y_C_1 = np.array([data_C_1_theta_1,data_C_2_theta_1,data_C_3_theta_1,data_C_4_theta_1,data_C_5_theta_1])
#(b)
y_C_2 = np.array([data_C_1_theta_2,data_C_2_theta_2,data_C_3_theta_2,data_C_4_theta_2,data_C_5_theta_2])

#(D)
#(a)
y_D_1 = np.array([data_D_1_theta_1,data_D_2_theta_1,data_D_3_theta_1,data_D_4_theta_1,data_D_5_theta_1])
#(b)
y_D_2 = np.array([data_D_1_theta_2,data_D_2_theta_2,data_D_3_theta_2,data_D_4_theta_2,data_D_5_theta_2])

#(E)
#(a)
y_E_1 = np.array([data_E_1_theta_1,data_E_2_theta_1,data_E_3_theta_1,data_E_4_theta_1,data_E_5_theta_1])
#(b)
y_E_2 = np.array([data_E_1_theta_2,data_E_2_theta_2,data_E_3_theta_2,data_E_4_theta_2,data_E_5_theta_2])

#(F)
#(a)
y_F_1 = np.array([data_F_1_theta_1,data_F_2_theta_1,data_F_3_theta_1,data_F_4_theta_1,data_F_5_theta_1])
#(b)
y_F_2 = np.array([data_F_1_theta_2,data_F_2_theta_2,data_F_3_theta_2,data_F_4_theta_2,data_F_5_theta_2])

#(G)
#(a)
y_G_1 = np.array([data_G_1_theta_1,data_G_2_theta_1,data_G_3_theta_1,data_G_4_theta_1,data_G_5_theta_1])
#(b)
y_G_2 = np.array([data_G_1_theta_2,data_G_2_theta_2,data_G_3_theta_2,data_G_4_theta_2,data_G_5_theta_2])

#(H)
#(a)
y_H_1 = np.array([data_H_1_theta_1,data_H_2_theta_1,data_H_3_theta_1,data_H_4_theta_1,data_H_5_theta_1])
#(b)
y_H_2 = np.array([data_H_1_theta_2,data_H_2_theta_2,data_H_3_theta_2,data_H_4_theta_2,data_H_5_theta_2])

#(I)
#(a)
y_I_1 = np.array([data_I_1_theta_1,data_I_2_theta_1,data_I_3_theta_1,data_I_4_theta_1,data_I_5_theta_1])
#(b)
y_I_2 = np.array([data_I_1_theta_2,data_I_2_theta_2,data_I_3_theta_2,data_I_4_theta_2,data_I_5_theta_2])

#(J)
#(a)
y_J_1 = np.array([data_J_1_theta_1,data_J_2_theta_1,data_J_3_theta_1,data_J_4_theta_1,data_J_5_theta_1])
#(b)
y_J_2 = np.array([data_J_1_theta_2,data_J_2_theta_2,data_J_3_theta_2,data_J_4_theta_2,data_J_5_theta_2])

#(K)
#(a)
y_K_1 = np.array([data_K_1_theta_1,data_K_2_theta_1,data_K_3_theta_1,data_K_4_theta_1,data_K_5_theta_1])
#(b)
y_K_2 = np.array([data_K_1_theta_2,data_K_2_theta_2,data_K_3_theta_2,data_K_4_theta_2,data_K_5_theta_2])

#(L)
#(a)
y_L_1 = np.array([data_L_1_theta_1,data_L_2_theta_1,data_L_3_theta_1,data_L_4_theta_1,data_L_5_theta_1])
#(b)
y_L_2 = np.array([data_L_1_theta_2,data_L_2_theta_2,data_L_3_theta_2,data_L_4_theta_2,data_L_5_theta_2])

#(M)
#(a)
y_M_1 = np.array([data_M_1_theta_1,data_M_2_theta_1,data_M_3_theta_1,data_M_4_theta_1,data_M_5_theta_1])
#(b)
y_M_2 = np.array([data_M_1_theta_2,data_M_2_theta_2,data_M_3_theta_2,data_M_4_theta_2,data_M_5_theta_2])

#(N)
#(a)
y_N_1 = np.array([data_N_1_theta_1,data_N_2_theta_1,data_N_3_theta_1,data_N_4_theta_1,data_N_5_theta_1])
#(b)
y_N_2 = np.array([data_N_1_theta_2,data_N_2_theta_2,data_N_3_theta_2,data_N_4_theta_2,data_N_5_theta_2])

#(O)
#(a)
y_O_1 = np.array([data_O_1_theta_1,data_O_2_theta_1,data_O_3_theta_1,data_O_4_theta_1,data_O_5_theta_1])
#(b)
y_O_2 = np.array([data_O_1_theta_2,data_O_2_theta_2,data_O_3_theta_2,data_O_4_theta_2,data_O_5_theta_2])

x = np.array([1,2,3,4,5])
#-------------グラフの位置の設定-----------------
#(A)
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(5,3,1)
ax1.plot(x,y_A_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax1.plot(x,y_A_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax1.set_title("No.1")
#(B)
ax2 = fig.add_subplot(5,3,2)
ax2.plot(x,y_B_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax2.plot(x,y_B_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax2.set_title("No.2")
#(C)
ax3 = fig.add_subplot(5,3,3)
ax3.plot(x,y_C_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax3.plot(x,y_C_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax3.set_title("No.3")
#(D)
ax4 = fig.add_subplot(5,3,4)
ax4.plot(x,y_D_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax4.plot(x,y_D_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax4.set_title("No.4")
#(E)
ax5 = fig.add_subplot(5,3,5)
ax5.plot(x,y_E_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax5.plot(x,y_E_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax5.set_title("No.5")
#(F)
ax6 = fig.add_subplot(5,3,6)
ax6.plot(x,y_F_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax6.plot(x,y_F_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax6.set_title("No.6")
#(G)
ax7 = fig.add_subplot(5,3,7)
ax7.plot(x,y_G_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax7.plot(x,y_G_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax7.set_title("No.7")
#(H)
ax8 = fig.add_subplot(5,3,8)
ax8.plot(x,y_H_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax8.plot(x,y_H_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax8.set_title("No.8")
#(I)
ax9 = fig.add_subplot(5,3,9)
ax9.plot(x,y_I_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax9.plot(x,y_I_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax9.set_title("No.9")
#(J)
ax10 = fig.add_subplot(5,3,10)
ax10.plot(x,y_J_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax10.plot(x,y_J_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax10.set_title("No.10")
#(K)
ax11 = fig.add_subplot(5,3,11)
ax11.plot(x,y_K_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax11.plot(x,y_K_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax11.set_title("No.11")
#(L)
ax12 = fig.add_subplot(5,3,12)
ax12.plot(x,y_L_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax12.plot(x,y_L_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax12.set_title("No.12")
#(M)
ax13 = fig.add_subplot(5,3,13)
ax13.plot(x,y_M_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax13.plot(x,y_M_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax13.set_title("No.13")
#(N)
ax14 = fig.add_subplot(5,3,14)
ax14.plot(x,y_N_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax14.plot(x,y_N_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax14.set_title("No.14")
#(O)
ax15 = fig.add_subplot(5,3,15)
ax15.plot(x,y_O_1, marker="$1$", linewidth= 2, linestyle = "solid")
ax15.plot(x,y_O_2, marker="$0$", linewidth= 2, linestyle = "dashed")
ax15.set_title("No.15")
#----------グラフの生成----------
plt.xticks([ 1,2,3,4,5 ])
plt.tight_layout()
plt.show()
