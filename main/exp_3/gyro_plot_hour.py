from datetime import datetime

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ts, Gx, Gy, Gz = [], [], [], []
    file = open('mestrado/data/exp_3/20191021104433.txt', 'r')
    for line in file.readlines():
        raw_ts, _, _, _, _, raw_Gx, raw_Gy, raw_Gz  = line.strip().split(';')
        ts.append(int(raw_ts))
        Gx.append(float(raw_Gx))
        Gy.append(float(raw_Gy))
        Gz.append(float(raw_Gz))
    #1571666400000 -> day 21/10/19 11h 00m 00s
    #1571713200000 -> day 22/10/19
    #1571666400000 11h #1571670000000 12h #1571673600000 13h #1571677200000 14h  
    #1571680800000 15h #1571684400000 16h #1571688000000 17h #1571691600000 18h
    #1571695200000 19h #1571698800000 20h #1571702400000 21h #1571706000000 22h
    #1571709600000 23h
    #1571713200000 24h
    thresholds = [0,0,0,0,0,0,0,0,0,0,0,1571666400000, 1571670000000, 1571673600000, 1571677200000, 1571680800000,
    1571684400000, 1571688000000, 1571691600000, 1571695200000, 1571698800000, 1571702400000, 1571706000000,
    1571709600000, 1571713200000]
    for n in range(11, 24, 1):
        threshold_min, threshold_max = thresholds[n], thresholds[n+1]
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gx[i] for i in index], label='Gx')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gy[i] for i in index], label='Gy')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gz[i] for i in index], label='Gz')
        plt.title('{}h:{}h'.format(n, n+1))
        plt.legend()
        plt.show()
