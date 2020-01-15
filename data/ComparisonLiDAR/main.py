import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# 配色リスト[青，赤，緑，黄，紫，水色]
color_list = ["#296fbc","#cb360d", "#3d9435", "#e1aa13", "#a54675", "#138bae"]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

file_name = "LiDAR.csv"
p2_L = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
x_L = p2_L[0:, 0]
y_L = p2_L[0:, 1]

file_name = "RADAR.csv"
p2_R = np.genfromtxt(file_name, delimiter=',', filling_values = 0)
x_R = p2_R[0:, 0]
y_R = p2_R[0:, 1]

#2016-06-02 00:00:00から1日毎のdatetimeを生成(6個生成)
ts = [0]*len(x_L)
for i in range(len(x_L)):
    ts[i] = datetime.fromtimestamp(x_L[i] + 9 * 60 * 60)


# ts = datetime.fromtimestamp(x_L[0] + 9*60*60)
# x = pd.date_range(ts, periods=6, freq='2H')
# print(ts)
# print(x)

ax.plot(ts, y_L, color = color_list[0], linewidth=0.5, label='LiDAR')
ax.plot(ts, y_R, color = color_list[1], linewidth=0.5, label='RADAR')

# 日付ラベルフォーマットを修正
ax.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0, 24, 3), tz=None))
ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=range(0, 24, 1), tz=None))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d\n%H:%M:%S"))

# 次の2行は軸ラベルを回転させるために使用
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, fontsize=10)

# グラフタイトル
# plt.title('')

# グラフ範囲
plt.xlim(datetime.fromtimestamp(x_L[0] + 9*60*60), datetime.fromtimestamp(x_L[len(x_L)-1] + 9*60*60))
# plt.ylim(0.0, 0.7)

# グラフの軸
plt.xlabel("Date and time")
plt.ylabel('')

#グラフの凡例
plt.legend()

plt.show()