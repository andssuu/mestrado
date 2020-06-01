import math
import statistics
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt

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
        time_std = range(0, 60, 5)
        values_std_x, values_std_y, values_std_z, values_std_resultant = [], [], [], []
        for j in time_std:
            values_std_x.append(statistics.stdev([ax[i] for i in index[(j*10):(j*10+50)]]))
            values_std_y.append(statistics.stdev([ay[i] for i in index[(j*10):(j*10+50)]]))
            values_std_z.append(statistics.stdev([az[i] for i in index[(j*10):(j*10+50)]]))
        barWidth = 0.3
        # Definindo a posição das barras
        r1 = np.arange(len(values_std_x))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        plt.bar(r1, values_std_x, width=barWidth, label='X')
        plt.bar(r2, values_std_y, width=barWidth, label='Y')
        plt.bar(r3, values_std_z, width=barWidth, label='Z')
        plt.title('08/08/19 {}h:{}m:{}m'.format(hour, n, n+1))
        plt.xlabel('Intervalos')
        plt.xticks([r + barWidth for r in range(len(values_std_x))], ['{}'.format(x_) for x_ in range(0, 60, 5)])
        plt.ylim(0, 0.35)
        plt.legend()
        #plt.savefig('mestrado/figures/exp1/accelerometer/{}h/std/exp1_acc_std_{}-{}.png'.format(hour, n, n+1))
        #plt.close()
        plt.show()
