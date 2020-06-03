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
    for n in range(24):
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [ax[i] for i in index], label='X')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [ay[i] for i in index], label='Y')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [az[i] for i in index], label='Z')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [resultant[i] for i in index], label='R')
        plt.title('08/08/19 {}h:{}h'.format(n, n+1))
        plt.ylim(-2, 2)
        plt.xticks(range(0, 61, 5))
        plt.legend()
        #plt.savefig('mestrado/figures/exp1/accelerometer/exp1_acc_{}-{}.png'.format(n, n+1))
        #plt.close()
        plt.show()
