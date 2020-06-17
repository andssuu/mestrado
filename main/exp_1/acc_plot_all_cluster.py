import statistics
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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
    threshold = 1565233200000
    fig = plt.figure()
    graph = fig.add_subplot(111, projection='3d')
    for n in range(24):
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        X = list(zip([ax[i] for i in index], [ay[i] for i in index], [az[i] for i in index]))
        kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
        X_clustered = kmeans.fit_predict(X)
        LABEL_COLOR_MAP = {0 : 'red', 1 : 'blue', 2: 'green', 3: 'yellow'}
        label_color = [LABEL_COLOR_MAP[l] for l in X_clustered]
        graph.scatter([ax[i] for i in index], [ay[i] for i in index], [az[i] for i in index], c=label_color, marker='o', s=1)
        graph.set_xlim([-2, 2])
        graph.set_ylim([-2, 2])
        graph.set_zlim([-2, 2])
        graph.set_xlabel('X')
        graph.set_ylabel('Y')
        graph.set_zlabel('Z')
        graph.set_title('08/08/19')
    plt.show()
