import math
from datetime import datetime

import matplotlib.pyplot as plt

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
    #1565233200000 -> day 8/8/19 - 0h - UTC-3
    threshold = 1565233200000
    fig, graph = plt.subplots(nrows=8, ncols=3)
    for n in range(24):
        graphics = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2),
            (3, 0), (3, 1), (3, 2),
            (4, 0), (4, 1), (4, 2),
            (5, 0), (5, 1), (5, 2),
            (6, 0), (6, 1), (6, 2),
            (7, 0), (7, 1), (7, 2)
        ]
        i_graphic, j_graphic = graphics[n]
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        graph[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [ax[i] for i in index], label='X')
        graph[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [ay[i] for i in index], label='Y')
        graph[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [az[i] for i in index], label='Z')
        graph[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [resultant[i] for i in index], label='R')
        graph[i_graphic, j_graphic].set_ylim([-2, 2])
        graph[i_graphic, j_graphic].set_title('08/08/19 {}h:{}h'.format(n, n+1))
    #plt.legend(loc="best")
    plt.show()
