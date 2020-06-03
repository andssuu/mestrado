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
    #1565233200000 -> day 8/8/19 - 0h - UTC-3
    threshold = 1565233200000
    fig = plt.figure()
    graph = fig.add_subplot(111, projection='3d')
    for n in range(24):
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        graph.scatter([ax[i] for i in index], [ay[i] for i in index], [az[i] for i in index], c='r', marker='o', s=1)
        graph.set_xlabel('X')
        graph.set_ylabel('Y')
        graph.set_zlabel('Z')
        plt.ylim(-2, 2)
    plt.title('08/08/19')
    #plt.savefig('mestrado/figures/exp1/accelerometer/3D/exp1_acc_all_3d.png')
    #plt.close()
    plt.show()
