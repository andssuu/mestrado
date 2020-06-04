from __future__ import division
import statistics
from datetime import datetime
import itertools

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal

if __name__ == "__main__":
    ts, ax, ay, az = [], [], [], []
    file = open('mestrado/data/exp_1/20190807124800-acc.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_ax, raw_ay, raw_az, *_  = line.strip().split(';')
        ts.append(int(raw_ts))
        ax.append((2*float(raw_ax))/ 32768.)
        ay.append((2*float(raw_ay))/ 32768.)
        az.append((2*float(raw_az))/ 32768.)
    #1565233200000 -> day 8/8/19
    hour = 0
    threshold = 1565233200000 + (3600000 * hour)
    for n in range(60):
        threshold_min, threshold_max = threshold, threshold+60000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max]
        _ts = np.array([(ts[i]-threshold_min)/1000 for i in index])
        _x = np.array([ax[i] for i in index])
        _y = np.array([ay[i] for i in index])
        _z = np.array([az[i] for i in index])
        freqs_x, psd_x = signal.welch(_x)
        freqs_y, psd_y = signal.welch(_y)
        freqs_z, psd_z = signal.welch(_z)
        plt.figure(figsize=(5, 4))
        plt.semilogx(freqs_x, psd_x)
        plt.semilogx(freqs_y, psd_y)
        plt.semilogx(freqs_z, psd_z)
        plt.title('PSD 08/08/19 {}h:{}m:{}m'.format(hour, n, n+1))
        plt.xlabel('Frequency')
        plt.ylabel('Power')
        plt.tight_layout()
        #plt.savefig('mestrado/figures/exp1/accelerometer/{}h/power/exp1_acc_fft_{}-{}.png'.format(hour, n, n+1))
        #plt.close()
        plt.show()
