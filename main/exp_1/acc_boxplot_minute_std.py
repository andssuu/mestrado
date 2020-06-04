import math
import statistics
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

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
        threshold_min, threshold_max = threshold, threshold + 60000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max]
        time_std = range(0, 600, 100)
        values_x, values_y, values_z, values_resultant = [], [], [], []
        _data = []
        # for j in time_std:
        #     _x = np.array([ax[i] for i in index[j:j+100]])
        #     _y = np.array([ay[i] for i in index[j:j+100]])
        #     _z = np.array([az[i] for i in index[j:j+100]])
        #     _x_mean = np.mean(_x)
        #     _y_mean = np.mean(_y)
        #     _z_mean = np.mean(_z)
        #     _x_std = np.std(_x)
        #     _y_std = np.std(_y)
        #     _z_std = np.std(_z)
        #     labels = ['Acc X', 'Acc Y', 'Acc Z']
            # x_pos = np.arange(len(labels))
            # CTEs = [_x_mean, _y_mean, _z_mean]
            # error = [_x_std, _y_std, _z_std]
            # fig, graph = plt.subplots()
            # graph.bar(x_pos, CTEs , yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
            # graph.set_ylabel('Standard Deviation (g)')
            # graph.set_xticks(x_pos)
            # graph.set_xticklabels(labels)
            # graph.set_title('08/08/19 {}m {}s {}s'.format(n, int(j/10), int(j/10)+10))
            # graph.yaxis.grid(True)
            # # Save the figure and show
            # plt.tight_layout()
            # plt.show()
        #     fig, graph = plt.subplots()
        #     labels = ['Acc X', 'Acc Y', 'Acc Z']
        #     graph.set_xticklabels(labels)
        #     graph.set_title('08/08/19 {}m {}s {}s'.format(n, int(j/10), int(j/10)+10))
        #     bp = graph.boxplot([_x, _y, _z])
        #     plt.ylabel('Acc (g)')
        #     plt.show()
        _x = np.array([ax[i] for i in index])
        _y = np.array([ay[i] for i in index])
        _z = np.array([az[i] for i in index])
        fig, graph = plt.subplots()
        labels = ['Acc X', 'Acc Y', 'Acc Z']
        graph.set_xticklabels(labels)
        graph.set_title('08/08/19 {}h {}m:{}m'.format(hour, n, n+1))
        bp = graph.boxplot([_x, _y, _z])
        plt.ylabel('Acc (g)')
        #plt.savefig('mestrado/figures/exp1/accelerometer/{}h/boxplot/exp1_acc_bp_{}-{}.png'.format(hour, n, n+1))
        #plt.close()
        plt.show()
