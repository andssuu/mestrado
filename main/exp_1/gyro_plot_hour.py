from datetime import datetime

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ts, Gx, Gy, Gz = [],[],[],[]
    file = open('mestrado/data/exp_1/20190807124800-acc.txt', 'r')
    for line in file.readlines():
        raw_ts, _, _, _, _, raw_Gx, raw_Gy, raw_Gz  = line.strip().split(';')
        ts.append(int(raw_ts))
        Gx.append(float(raw_Gx))
        Gy.append(float(raw_Gy))
        Gz.append(float(raw_Gz))
    #1565233200000 -> day 8/8/19 - 0h - UTC-3
    threshold = 1565233200000
    for n in range(24):
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gx[i] for i in index], label='Gx')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gy[i] for i in index], label='Gy')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gz[i] for i in index], label='Gz')
        plt.title('{}h:{}h'.format(n, n+1))
        plt.legend()
        #plt.savefig('mestrado/figures/exp1/gyroscope/exp1_gyro_{}-{}.png'.format(n, n+1))
        plt.show()
