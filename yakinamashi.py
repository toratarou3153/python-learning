import random
import math
import numpy as np
import copy
import matplotlib.pyplot as plt

#点の数
n = 47
print("　都市の数：" + str(n))
#クラスタリング・スケジュール(温度関数)の定数
c = 30
#クラスタリング・スケジュール(温度関数)の上界
end = 10000
#摂動回数の設定
k = 400


#クラスタリング・スケジュール(温度関数)の設定---------------------------------------------------------------------------------
def T(temper):
    return c/(math.sqrt(temper)+1)

#初めにめぐる点の順番--------------------------------------------------------------------------------------------------------
city = [i for i in range(n)]
random.shuffle(city)

#点の位置-------------------------------------------------------------------------------------------------------------------
x = [(2.5-1)*math.cos(0.27*theta) + 0.8*math.cos((2.5-1)/1*0.27*theta) for theta in range(n)]
y = [(2.5-1)*math.sin(0.27*theta) - 0.8*math.sin((2.5-1)/1*0.27*theta) for theta in range(n)]


x_y = {}
for i,j,r in zip(range(n),x,y):
    x_y[i] = [j, r]

#距離を求める関数の生成-------------------------------------------------------------------------------------------------------
def d(toshi):
    kyori = 0
    for i in range(n):
        if toshi[i] != toshi[n-1]:
            kyori += math.sqrt((x_y[toshi[i+1]][0]-x_y[toshi[i]][0])**2+(x_y[toshi[i+1]][1]-x_y[toshi[i]][1])**2)
        else:
            kyori += math.sqrt((x_y[toshi[0]][0]-x_y[toshi[i]][0])**2+(x_y[toshi[0]][1]-x_y[toshi[i]][1])**2)
    return kyori
print("初期の距離：" + str(d(city)))

print("理想的な距離：",d([i for i in range(n)]))
x = [x_y[i][0] for i in range(n)]
y = [x_y[j][1] for j in range(n)]
x.append(x_y[0][0])
y.append(x_y[0][1])
plt.plot(x, y, marker="o")
plt.show()

x = [x_y[i][0] for i in city]
y = [x_y[j][1] for j in city]
x.append(x_y[city[0]][0])
y.append(x_y[city[0]][1])
plt.plot(x, y, marker="o")
plt.show()

#大域的最小値の生成-----------------------------------------------------------------------------------------------------------
for t in range(end):
    for i in range(k):
        #摂動の生成--------------------------------------------------------------------------------------------------
        a = random.randint(1,n-1)
        b = random.randint(a+1,n)
        city_near = copy.copy(city)
        city_near[a:b] = reversed(city_near[a:b])
        #遷移--------------------------------------------------------------------------------------------------------
        if d(city) >= d(city_near):
            city = city_near
        else:
            P = (math.e)**(-(d(city_near)-d(city))/T(t))
            m = np.random.choice([0,1],p = [1-P,P])
            if m == 1:
                city = city_near
    
print("　　最小値：" + str(d(city)))
print("　　　順番：" + str(city))

x = [x_y[i][0] for i in city]
y = [x_y[j][1] for j in city]
x.append(x_y[city[0]][0])
y.append(x_y[city[0]][1])
plt.plot(x, y, marker="o")
plt.show()