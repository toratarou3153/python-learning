import matplotlib.pyplot as plt
import numpy as np

# データ生成
y = np.array([50,60,100,80,75])
x = np.array([1,2,3,4,5])
y1 = np.array([100,70,50,40,35])
x1 = np.array([1,2,3,4,5])
# プロット領域(Figure, Axes)の初期化
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(421)
ax2 = fig.add_subplot(422)
ax3 = fig.add_subplot(423)
ax4 = fig.add_subplot(424)
ax5 = fig.add_subplot(425)
ax6 = fig.add_subplot(426)
ax7 = fig.add_subplot(427)
ax8 = fig.add_subplot(428)

# 棒グラフの作成
ax1.plot(x,y, marker="$a$", linewidth= 2, linestyle = "dashed")
ax1.set_title("title1")
ax2.plot(x,y, color ="red", linewidth= 2, linestyle = "dashed")
ax2.set_title("title2")
ax3.plot(x,y, marker="$a$", linewidth= 2, linestyle = "dashed")
ax3.plot(x1,y1, marker="$b$",color = "red", linewidth= 2, linestyle = "dashed")
ax3.set_title("title3")
ax4.plot(x,y, marker="$a$", linewidth= 2, linestyle = "dashed")
ax4.set_title("title4")
ax5.plot(x,y, marker="$a$", linewidth= 2, linestyle = "dashed")
ax5.set_title("title5")
ax6.plot(x,y, marker="$a$", linewidth= 2, linestyle = "dashed")
ax6.set_title("title6")
ax7.plot(x,y, marker="$a$", linewidth= 2, linestyle = "dashed")
ax7.set_title("title7")
ax8.plot(x,y, marker="$a$", linewidth= 2, linestyle = "dashed")
ax8.set_title("title8")

plt.xticks([ 1,2,3,4,5 ])
plt.tight_layout()
plt.show()
