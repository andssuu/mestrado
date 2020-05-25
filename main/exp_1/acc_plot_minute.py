from datetime import datetime

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ts, Ax, Ay, Az = [], [], [], []
    file = open('mestrado/data/exp_1/20190807124800-acc.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_Ax, raw_Ay, raw_Az, *_  = line.strip().split(';')
        ts.append(int(raw_ts))
        Ax.append((2 * float(raw_Ax))/ 32768.)
        Ay.append((2 * float(raw_Ay))/ 32768.)
        Az.append((2 * float(raw_Az))/ 32768.)
    #1565233200000 -> day 8/8/19
    hour = 0
    threshold = 1565233200000+((3600000)*hour)
    for n in range(60):
        threshold_min, threshold_max = threshold, threshold+60000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        plt.plot([(ts[i]-threshold_min)/1000 for i in index], [Ax[i] for i in index], label='Ax')
        plt.plot([(ts[i]-threshold_min)/1000 for i in index], [Ay[i] for i in index], label='Ay')
        plt.plot([(ts[i]-threshold_min)/1000 for i in index], [Az[i] for i in index], label='Az')
        plt.title('08/08/19 {}h:{}m:{}m'.format(hour, n, n+1))
        plt.ylim(-2, 2)
        plt.legend()
        plt.show()
