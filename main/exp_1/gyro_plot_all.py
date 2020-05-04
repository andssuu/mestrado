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
    fig, axs = plt.subplots(nrows=8, ncols=3)
    for n in range(24):
        graphics = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2),
            (3, 0), (3, 1), (3, 2),
            (4, 0), (4, 1), (4, 2),
            (5, 0), (5, 1), (5, 2),
            (6, 0), (6, 1), (6, 2),
            (7, 0), (7, 1), (7, 2)
        ]
        i_graphic, j_graphic = graphics[n]
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]      
        axs[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [Gx[i] for i in index], label='Gx')
        axs[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [Gy[i] for i in index], label='Gy')
        axs[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [Gz[i] for i in index], label='Gz')
        axs[i_graphic, j_graphic].set_title('{}h:{}h'.format(n, n+1))
    #plt.legend(loc="best")
    plt.show()
