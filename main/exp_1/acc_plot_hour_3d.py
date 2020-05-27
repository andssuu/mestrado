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
    #1565233200000 -> day 8/8/19 - 0h - UTC-3
    threshold = 1565233200000
    for n in range(24):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        ax.scatter([Ax[i] for i in index], [Ay[i] for i in index], [Az[i] for i in index], c='r', marker='o', s=1)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.title('{}h:{}h'.format(n, n+1))
        plt.ylim(-2, 2)
        plt.show()
