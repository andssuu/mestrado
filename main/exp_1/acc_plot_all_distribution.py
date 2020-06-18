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
    fig, graph = plt.subplots(nrows=2, ncols=1)
    bins = int(len(_x_mean)/10)
    graph[0].hist(_x_mean, bins=bins, label="Mean X")
    graph[0].hist(_y_mean, bins=bins, label="Mean Y")
    graph[0].hist(_z_mean, bins=bins, label="Mean Z")
    graph[0].hist(_r_mean, bins=bins, label="Mean R")
    graph[1].hist(_x_std, bins=bins, label="Std X")
    graph[1].hist(_y_std, bins=bins, label="Std Y")
    graph[1].hist(_z_std, bins=bins, label="Std Z")
    graph[1].hist(_r_std, bins=bins, label="Std R")
    #graph[1].set_xticks(range(0, 10, 1))
    plt.legend()
    plt.show()

    # fig, graph = plt.subplots(nrows=2, ncols=1)
    # graph[0].plot(range(0, len(_z_std)), _z_std, marker='x', linestyle = 'None', label="Mean X")
    # graph[1].plot(range(0, len(_z_mean)), _z_mean, marker='x', linestyle = 'None', label="Mean X")
    # plt.show()

    _data = list(zip(_x_std, _y_std, _z_std))
    #_data = list(zip(_y_std))
    kmeans = KMeans(n_clusters=3, random_state=0).fit(_data)
    X_clustered = kmeans.fit_predict(_data)
    LABEL_COLOR_MAP = {0 : 'red', 1 : 'blue', 2: 'green'}
    label_color = [LABEL_COLOR_MAP[l] for l in X_clustered]
    fig = plt.figure()
    graph = fig.add_subplot(111, projection='3d')
    graph.scatter(_x_std, _y_std, _z_std, c=label_color, marker='o', s=1)
    #graph.scatter(_y_std, _y_std, _y_std, c=label_color, marker='o', s=1)
    plt.show()

    #_data = list(zip(_x_mean, _y_mean, _z_mean))
    # _data = list(zip(_y_mean))
    # kmeans = KMeans(n_clusters=2, random_state=0).fit(_data)
    # X_clustered = kmeans.fit_predict(_data)
    # LABEL_COLOR_MAP = {0 : 'red', 1 : 'blue'}
    # label_color = [LABEL_COLOR_MAP[l] for l in X_clustered]
    # fig = plt.figure()
    # graph = fig.add_subplot(111, projection='3d')
    # graph.scatter(_y_mean, _y_mean, _y_mean, c=label_color, marker='o', s=1)
    # plt.show()
