import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from statistics import mean, median,variance,stdev

# 配色リスト[青，赤，緑，黄，紫，水色]
color_list = ["#000000","#cb360d", "#3d9435", "#e1aa13", "#a54675", "#138bae"]

plt.rcParams['xtick.direction'] = 'in'  # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'  # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1.0 # x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0 # y軸主目盛り線の線幅
plt.rcParams['font.size'] = 9           # フォントの大きさ
plt.rcParams['axes.linewidth'] = 0.7    # 軸の線幅edge linewidth。囲みの太さ

fig = plt.figure(figsize=(18/2.54, 12/2.54))
ax = fig.add_subplot(1, 1, 1)

# データの読み込み
file_name = "acc.csv"
p2 = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
x = p2[:, 0]
y = p2[:, 1]

file_name = "result.csv"
p2 = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
r_x = p2[:, 0]
r_y = p2[:, 1]

detection_times = []
for i in range(len(r_x)):
    if r_y[i] == 1:
        detection_times.append(r_x[i])

print(x)
print(detection_times)

# グラフにデータを追加
ax.plot(x, y, color = color_list[0], linewidth=1, label='acceleration')


for data in detection_times:
    ax.vlines([data], min(y), max(y), color_list[0], linestyles='dotted')

ax.vlines([detection_times[0]], min(y), max(y), color_list[0], linestyles='dotted', label='detection point')

# 目盛のスタイル
plt.setp(ax.get_xticklabels(), fontsize=8)
plt.setp(ax.get_yticklabels(), fontsize=8)
# ax.grid(ls="--")

# グラフタイトル
# plt.title('')

# グラフ範囲
# plt.xlim()
# plt.ylim(0.0, 0.7)

# 余白設定
plt.subplots_adjust(bottom=0.22)

# グラフの軸
plt.xlabel("time[s]", fontsize=9)
plt.ylabel("acceleration[m/s$^2$]", fontsize=9)

#グラフの凡例
plt.legend()

# 表示
plt.show()
