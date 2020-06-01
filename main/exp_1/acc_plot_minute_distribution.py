import math
import statistics
from datetime import datetime
import itertools

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

if __name__ == "__main__":
    ts, ax, ay, az, resultant = [], [], [], [], []
    file = open('mestrado/data/exp_1/20190807124800-acc.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_ax, raw_ay, raw_az, *_  = line.strip().split(';')
        ts.append(int(raw_ts))
        ax.append((2*float(raw_ax))/ 32768.)
        ay.append((2*float(raw_ay))/ 32768.)
        az.append((2*float(raw_az))/ 32768.)
        resultant.append(math.sqrt(pow(ax[-1], 2) + pow(ay[-1], 2) + pow(az[-1], 2)))
    #1565233200000 -> day 8/8/19
    hour = 16
    threshold = 1565233200000 + (3600000 * hour)
    for n in range(60):
        threshold_min, threshold_max = threshold, threshold+60000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        fig, graph = plt.subplots(nrows=2, ncols=3)
        for t in range(6):
            mls = 100
            interval = t * mls
            _index = index[interval:interval+mls]
            _x = np.array([ax[i] for i in _index])
            _y = np.array([ay[i] for i in _index])
            _z = np.array([az[i] for i in _index])
            _r = np.array([resultant[i] for i in _index])
            x_counter, y_counter, z_counter, r_counter = [], [], [], []
            for i in np.arange(-2, 2, 0.05):
                _frequence = len([m for m in _x if m >i and m <=i+0.05])/100.
                x_counter.append(_frequence) if _frequence > 0 else x_counter.append(np.nan)
                _frequence = len([m for m in _y if m >i and m <=i+0.05])/100.
                y_counter.append(_frequence) if _frequence > 0 else y_counter.append(np.nan)
                _frequence = len([m for m in _z if m >i and m <=i+0.05])/100.
                z_counter.append(_frequence) if _frequence > 0 else z_counter.append(np.nan)
                _frequence = len([m for m in _r if m >i and m <=i+0.05])/100.
                r_counter.append(_frequence) if _frequence > 0 else r_counter.append(np.nan)
            graphics = [
                (0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
            ]
            i_graphic, j_graphic = graphics[t]
            graph[i_graphic, j_graphic].plot(np.arange(-2, 2, 0.05), x_counter, marker='*', label="X")
            graph[i_graphic, j_graphic].plot(np.arange(-2, 2, 0.05), y_counter, marker='v', label="Y")
            graph[i_graphic, j_graphic].plot(np.arange(-2, 2, 0.05), z_counter, marker='x', label="Z")
            graph[i_graphic, j_graphic].plot(np.arange(-2, 2, 0.05), r_counter, marker='P', label="R")
            ticks = np.arange(-2, 2.1, 0.5)
            graph[i_graphic, j_graphic].set_xticks(ticks)
            graph[i_graphic, j_graphic].set_title('{}h {}m {}s:{}s'.format(hour, n, t*10, t*10+10))
        plt.legend(loc="best")
        plt.show()
