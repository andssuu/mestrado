from  math import sqrt, log
from statistics import mean, stdev
from datetime import datetime
import itertools

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans

if __name__ == "__main__":
    ts, ax, ay, az, resultant = [], [], [], [], []
    file = open('mestrado/data/exp_1/20190807124800-acc.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_ax, raw_ay, raw_az, *_  = line.strip().split(';')
        ts.append(int(raw_ts))
        ax.append((2*float(raw_ax))/ 32768.)
        ay.append((2*float(raw_ay))/ 32768.)
        az.append((2*float(raw_az))/ 32768.)
        resultant.append(sqrt(pow(ax[-1], 2) + pow(ay[-1], 2) + pow(az[-1], 2)))
    #1565233200000 -> day 8/8/19
    #hour = 0
    threshold_min = 1565233200000
    threshold_max = 1565233200000 + (3600000 * 24)
    index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
    _x_mean, _y_mean, _z_mean, _r_mean = [], [], [], []
    _x_std, _y_std, _z_std, _r_std = [], [], [], []
    for t in range(0, len(index), 100):
        _x = [ax[i] for i in index[t:t+100]]
        _y = [ay[i] for i in index[t:t+100]]
        _z = [az[i] for i in index[t:t+100]]
        _r = [resultant[i] for i in index[t:t+100]]
        _x_mean.append(log(2 + mean(_x)))
        _x_std.append(log(stdev(_x)))
        _y_mean.append(log(2 + mean(_y)))
        _y_std.append(log(stdev(_y)))
        _z_mean.append(log(2 + mean(_z)))
        _z_std.append(log(stdev(_z)))
        _r_mean.append(log(2 + mean(_r)))
        _r_std.append(log(stdev(_r)))
    _data = list(zip(_x_std, _y_std, _z_std))
    kmeans = KMeans(n_clusters=3, random_state=0).fit(_data)
    std_clustered = kmeans.fit_predict(_data)
    _data = list(zip(_x_mean, _y_mean, _z_mean))
    kmeans = KMeans(n_clusters=2, random_state=0).fit(_data)
    mean_clustered = kmeans.fit_predict(_data)
    hour, minute, second = 0, 0, 0
    for m, s in zip(mean_clustered, std_clustered) :
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if s == 2: behavior = "ÓCIO"
        elif s == 1: behavior = "RUMINANDO"
        else:
            if m == 1: behavior = "PASTANDO"
            else: behavior = "OUTRO"
        print('{}h {}m {}s:{} -> {}'.format(hour, minute, second, second+10, behavior))
        second +=10
