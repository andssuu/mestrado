from datetime import datetime

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ts, Ax, Ay, Az = [], [] , [], []
    file = open('mestrado/data/exp_3/20191021104433-acc.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_Ax, raw_Ay, raw_Az, *_  = line.strip().split(';')
        ts.append(int(raw_ts))
        Ax.append((2 * float(raw_Ax))/ 32768.)
        Ay.append((2 * float(raw_Ay))/ 32768.)
        Az.append((2 * float(raw_Az))/ 32768.)
    #1571666400000 -> day 21/10/19 11h 00m 00s
    threshold = 1571666400000
    for n in range(11, 24, 1):
        threshold_min, threshold_max = threshold, threshold+3600000
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Ax[i] for i in index], label='Ax')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Ay[i] for i in index], label='Ay')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Az[i] for i in index], label='Az')
        plt.title('{}h:{}h'.format(n, n+1))
        plt.ylim(-2, 2)
        plt.legend()
        #plt.savefig('mestrado/figures/exp3/accelerometer/exp3_acc_{}-{}.png'.format(n, n+1))
        plt.show()
