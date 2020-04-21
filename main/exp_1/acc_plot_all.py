from datetime import datetime

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ts, Ax, Ay, Az = [],[],[],[]
    file = open('mestrado/data/exp_1/20190807124800-acc.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_Ax, raw_Ay, raw_Az, *_  = line.strip().split(';')
        ts.append(int(raw_ts))
        Ax.append((2 * float(raw_Ax))/ 32768.)
        Ay.append((2 * float(raw_Ay))/ 32768.)
        Az.append((2 * float(raw_Az))/ 32768.)
    #1565233200000 -> day 8/8/19
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
        axs[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [Ax[i] for i in index], label='Ax')
        axs[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [Ay[i] for i in index], label='Ay')
        axs[i_graphic, j_graphic].plot([(ts[i]-threshold_min)/60000 for i in index], [Az[i] for i in index], label='Az')
        axs[i_graphic, j_graphic].set_ylim([-2, 2])
        axs[i_graphic, j_graphic].set_title('{}h:{}h'.format(n, n+1))
    #plt.legend(loc="best")
    plt.show()
