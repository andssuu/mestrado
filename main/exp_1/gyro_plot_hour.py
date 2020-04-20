from datetime import datetime

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ts, Gx, Gy, Gz = [],[],[],[]
    file = open('mestrado/data/exp_1/20190807124800.txt', 'r')
    for line in file.readlines():
        raw_ts, _, _, _, _, raw_Gx, raw_Gy, raw_Gz  = line.strip().split(';')
        ts.append(int(raw_ts))
        Gx.append(float(raw_Gx))
        Gy.append(float(raw_Gy))
        Gz.append(float(raw_Gz))
    #1565233200000 -> day 8/8/19
    #1565319600000 -> day 9/9/19
    #1565233200000 0h  #1565236800000 1h  #1565240400000  2h   #1565244000000 3h  #1565247600000 4h  #1565251200000 5h 
    #1565254800000 6h  #1565258400000 7h  #1565262000000  8h   #1565265600000 9h  #1565269200000 10h #1565272800000 11h 
    #1565276400000 12h #1565280000000 13h #1565283600000  14h  #1565287200000 15h #1565290800000 16h #1565294400000 17h
    #1565298000000 18h #1565301600000 19h #1565305200000  20h  #1565308800000 21h #1565312400000 22h #1565316000000 23h
    #1565319600000 24h
    thresholds = [1565233200000, 1565236800000, 1565240400000, 1565244000000, 1565247600000, 1565251200000,
     1565254800000, 1565258400000 ,1565262000000  ,1565265600000 ,1565269200000 ,1565272800000,
     1565276400000 ,1565280000000 ,1565283600000  ,1565287200000 ,1565290800000 ,1565294400000,
     1565298000000 ,1565301600000 ,1565305200000  ,1565308800000 ,1565312400000 ,1565316000000, 1565319600000]
    for n in range(24):
        threshold_min, threshold_max = thresholds[n], thresholds[n+1]
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gx[i] for i in index], label='Gx')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gy[i] for i in index], label='Gy')
        plt.plot([(ts[i]-threshold_min)/60000 for i in index], [Gz[i] for i in index], label='Gz')
        plt.title('{}h:{}h'.format(n, n+1))
        plt.legend()
        plt.show()
