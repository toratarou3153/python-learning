data_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
data_goukei = [10,17,19,23,31,41,43,47,53,57,59,61,65,66,67,69,70,73,74,77,78,80,81,83,85,87,88,89,92,93]
a=1
b=2
c=3
d=4
data_A = [a,b,c,d,a,a,a,c,d,b,b,b,c,b,d,d,d,a,b,c,a,d,b,c,d,c,d,a,b,c]
data_B = [c,b,d,d,d,c,b,c,a,b,c,d,c,d,c,b,c,b,c,b,a,a,a,d,c,d,c,b,c,b]
data_C = [a,b,c,d,a,a,a,c,d,b,b,b,c,b,d,d,d,a,b,c,a,d,b,c,d,c,d,a,b,c]
data_D = [a,b,c,d,a,a,a,c,d,b,b,b,c,b,d,d,d,a,b,c,a,d,b,c,d,c,d,a,b,c]
data_E = [a,b,c,d,a,a,a,c,d,b,b,b,c,b,d,d,d,a,b,c,a,d,b,c,d,c,d,a,b,c]
data_F = [a,b,c,d,a,a,a,c,d,b,b,b,c,b,d,d,d,a,b,c,a,d,b,c,d,c,d,a,b,c]
data_G = [a,b,c,d,a,a,a,c,d,b,b,b,c,b,d,d,d,a,b,c,a,d,b,c,d,c,d,a,b,c]
data_H = [a,b,c,d,a,a,a,c,d,b,b,b,c,b,d,d,d,a,b,c,a,d,b,c,d,c,d,a,b,c]

data_A_ans = 3
data_B_ans = 2
data_C_ans = 3
data_D_ans = 1
data_E_ans = 2
data_F_ans = 2
data_G_ans = 1
data_H_ans = 1


n = 5
data1 = data_goukei[:n+1]
data2 = data_goukei[n+1:n+7]
data3 = data_goukei[n+7:n+13]
data4 = data_goukei[n+13:n+19]
data5 = data_goukei[n+19:n+25]

data_A_1 = data_A[:n+1]
data_A_2 = data_A[n+1:n+7]
data_A_3 = data_A[n+7:n+13]
data_A_4 = data_A[n+13:n+19]
data_A_5 = data_A[n+19:n+25]

ans_A = 0
print(data_A_1)
