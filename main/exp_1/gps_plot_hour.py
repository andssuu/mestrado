from datetime import datetime

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ts, lat, lng = [], [], []
    file = open('mestrado/data/exp_1/20190807124800-gps.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_lat, raw_lng = line.strip().split(';')
        ts.append(float(raw_ts))
        lat.append(float(raw_lat))
        lng.append(float(raw_lng))
    #1565233200000 -> day 8/8/19
    threshold = 1565233200000
    for n in range(24):
        fig, axs = plt.subplots(nrows=2, ncols=1)
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        axs[0].plot([(ts[i]-threshold_min)/60000 for i in index], [lat[i] for i in index], label='Lat')
        axs[0].set_title('{}h:{}h'.format(n, n+1))
        axs[0].legend()
        axs[1].plot([(ts[i]-threshold_min)/60000 for i in index], [lng[i] for i in index], label='Lng', color='red')
        #axs[1].set_title('LNG - {}h:{}h'.format(n, n+1))
        axs[1].legend()
        #plt.savefig('mestrado/figures/exp1/gps/exp1_gps_{}-{}.png'.format(n, n+1))
        plt.show()
