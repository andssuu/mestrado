from  math import sqrt, log
from statistics import mean, stdev
from datetime import datetime
import itertools

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats.stats import pearsonr

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
        _x = [ax[i]*10000 for i in index[t:t+100]]
        _y = [ay[i]*10000 for i in index[t:t+100]]
        _z = [az[i]*10000 for i in index[t:t+100]]
        _r = [resultant[i]*10000 for i in index[t:t+100]]
        _x_mean.append(log(abs(10000 + mean(_x))))
        _x_std.append(log(abs(stdev(_x))))
        _y_mean.append(log(abs(10000 + mean(_y))))
        _y_std.append(log(abs(stdev(_y))))
        _z_mean.append(log(abs(10000 + mean(_z))))
        _z_std.append(log(abs(stdev(_z))))
        _r_mean.append(log(abs(10000 + mean(_r))))
        _r_std.append(log(abs(stdev(_r))))
    print('''Acc's Pearson\n
        X Y  -> {}\n
        X Z  -> {}\n
        X R  -> {}\n
        Y Z  -> {}\n
        Y R  -> {}\n
        Z R  -> {}\n
    '''.format(pearsonr(_x, _y), pearsonr(_x, _z), pearsonr(_x, _r),
                pearsonr(_y, _z), pearsonr(_y, _r), pearsonr(_z, _r)))
    print('''Mean's Pearson\n
        X Y  -> {}\n
        X Z  -> {}\n
        X R  -> {}\n
        Y Z  -> {}\n
        Y R  -> {}\n
        Z R  -> {}\n
    '''.format(pearsonr(_x_mean, _y_mean), pearsonr(_x_mean, _z_mean),
                pearsonr(_x_mean, _r_mean), pearsonr(_y_mean, _z_mean),
                pearsonr(_y_mean, _r_mean), pearsonr(_z_mean, _r_mean)))
    print('''STD's Pearson\n
        X Y  -> {}\n
        X Z  -> {}\n
        X R  -> {}\n
        Y Z  -> {}\n
        Y R  -> {}\n
        Z R  -> {}\n
   '''.format(pearsonr(_x_std, _y_std), pearsonr(_x_std, _z_std),
                pearsonr(_x_std, _r_std), pearsonr(_y_std, _z_std),
                pearsonr(_y_std, _r_std), pearsonr(_z_std, _r_std)))
