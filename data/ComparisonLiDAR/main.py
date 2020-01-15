import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# 配色リスト[青，赤，緑，黄，紫，水色]
color_list = ["#296fbc","#cb360d", "#3d9435", "#e1aa13", "#a54675", "#138bae"]

# 目盛の設定
plt.rcParams['xtick.direction'] = 'in'  # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'  # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1.0 # x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0 # y軸主目盛り線の線幅
plt.rcParams['axes.linewidth'] = 0.7    # 軸の線幅edge linewidth。囲みの太さ

# プロットエリアの設定
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# データの読み込み
file_name = "LiDAR.csv"
p2_L = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
x_L = p2_L[0:, 0]
y_L = p2_L[0:, 1]

file_name = "RADAR.csv"
p2_R = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
x_R = p2_R[0:, 0]
y_R = p2_R[0:, 1]

# この日の日没と日の出の日時
sunset_time = datetime.fromtimestamp(1578814380 + 9*60*60)
sunrise_time = datetime.fromtimestamp(1578866040 + 9*60*60)
sunset_line = [[sunset_time, sunset_time], [0.58, 0.61]]
sunrise_line = [[sunrise_time, sunrise_time], [0.58, 0.61]]

# タイムスタンプのリストを作成
ts = [0]*len(x_L)
for i in range(len(x_L)):
    ts[i] = datetime.fromtimestamp(x_L[i] + 9*60*60)
    # ts[i] = datetime.fromtimestamp(x_L[i])

# グラフにデータを追加
ax.plot(ts, y_L, color = color_list[0], linewidth=0.5, label='LiDAR')
ax.plot(ts, y_R, color = color_list[1], linewidth=0.5, label='RADAR')
ax.plot(sunset_line[0], sunset_line[1], color = color_list[2], linewidth=2, label='sunset_line')
ax.plot(sunrise_line[0], sunrise_line[1], color = color_list[3], linewidth=2, label='sunrise_line')

# 日付ラベルフォーマットを修正
ax.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0, 24, 3), tz=None))
ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=range(0, 24, 1), tz=None))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d\n%H:%M:%S"))

# 軸ラベルを回転
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, fontsize=10)

# グラフタイトル
# plt.title('')

# グラフ範囲
# plt.xlim()
# plt.ylim(0.0, 0.7)

# 余白設定
plt.subplots_adjust(bottom=0.25)

# グラフの軸
plt.xlabel("Date and time")
plt.ylabel("Distance[m]")

#グラフの凡例
plt.legend()

# 表示
plt.show()