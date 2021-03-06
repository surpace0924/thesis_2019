import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from statistics import mean, median,variance,stdev

# 配色リスト[青，赤，緑，黄，紫，水色]
color_list = ["#296fbc","#cb360d", "#3d9435", "#e1aa13", "#a54675", "#138bae"]

plt.rcParams['xtick.direction'] = 'in'  # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'  # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1.0 # x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0 # y軸主目盛り線の線幅
plt.rcParams['font.size'] = 9           # フォントの大きさ
plt.rcParams['axes.linewidth'] = 0.7    # 軸の線幅edge linewidth。囲みの太さ

# プロットエリアの設定
fig = plt.figure(figsize=(18/2.54, 12/2.54))
ax = fig.add_subplot(1, 1, 1)

num = 60
b = np.ones(num) / num

# データの読み込み
file_name = "LiDAR.csv"
p2_L = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
x_L = p2_L[0:, 0]
y = p2_L[0:, 1]

# 移動平均フィルタ
y_L = np.convolve(y, b, mode='same')
for i in range(int(num / 2)):
    if i == 0:
        y_L[0] = y[int(num / 2) + 1]
    # elif i == int(num / 2) - 1:
        # y_L[len(y_L) - i - 1] = y[len(y)-2]
    else:
        y_L[i] = sum(y[0:i])/len(y[0:i]+1)
        y_L[len(y_L) - i] = sum(y[len(y) - int(num / 2):len(y) - i]) / len(y[len(y) - int(num / 2):len(y) - i])

y_L = p2_L[0:, 1]

file_name = "RADAR.csv"
p2_R = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
x_R = p2_R[0:, 0]
y = p2_R[0:, 1]
y_R = np.convolve(y, b, mode='same')
for i in range(int(num / 2)):
    if i == 0:
        y_R[0] = y[int(num / 2) + 1]
    # elif i == int(num / 2) - 1:
        # y_R[len(y_R) - i - 1] = y[len(y)-2]
    else:
        y_R[i] = sum(y[0:i])/len(y[0:i]+1)
        y_R[len(y_R) - i] = sum(y[len(y) - int(num / 2):len(y) - i]) / len(y[len(y) - int(num / 2):len(y) - i])

y_R = p2_R[0:, 1]

# この日の日没と日の出の日時
JST = 9*60*60
# JST = 0
sunset_time = datetime.fromtimestamp(1578814380 + JST)
sunrise_time = datetime.fromtimestamp(1578866040 + JST)
sunset_line = [[sunset_time, sunset_time], [0.58, 0.61]]
sunrise_line = [[sunrise_time, sunrise_time], [0.58, 0.61]]

# タイムスタンプのリストを作成
ts = [0]*len(x_L)
for i in range(len(x_L)):
    ts[i] = datetime.fromtimestamp(x_L[i] + JST)

# グラフにデータを追加
ax.plot(ts, y_L, color = color_list[0], linewidth=1, label='LiDAR')
ax.plot(ts, y_R, color = color_list[1], linewidth=1, label='RADAR')
# ax.plot(sunset_line[0], sunset_line[1], color = color_list[2], linewidth=2, label='sunset_line')
# ax.plot(sunrise_line[0], sunrise_line[1], color = color_list[3], linewidth=2, label='sunrise_line')

# 日付ラベルフォーマットを修正
ax.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0, 24, 3), tz=None))
ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=range(0, 24, 1), tz=None))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d\n%H:%M:%S"))

ax.grid(ls="--")

# 目盛のスタイル
plt.setp(ax.get_xticklabels(), fontsize=8, rotation=45)
plt.setp(ax.get_yticklabels(), fontsize=8)

# グラフタイトル
# plt.title('')

# グラフ範囲
# plt.xlim()
# plt.ylim(0.0, 0.7)

# 余白設定
plt.subplots_adjust(bottom=0.22)

# グラフの軸
plt.xlabel("Date and time", fontsize=9)
plt.ylabel("Distance[m]", fontsize=9)

#グラフの凡例
plt.legend()

# 表示
plt.show()

data = y_L
m = mean(data)
median = median(data)
variance = variance(data)
stdev = stdev(data)
print('平均: {0:.8f}'.format(m))
print('中央値: {0:.8f}'.format(median))
print('分散: {0:.8f}'.format(variance))
print('標準偏差: {0:.8f}'.format(stdev))

