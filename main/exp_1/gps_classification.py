from datetime import datetime
from math import sin, cos, sqrt, atan2, radians

import matplotlib.pyplot as plt

def get_distance(lat_1, lng1, lat2, lng2):
    radius = 6371.0
    lat_1, lng_1 = radians(lat_1), radians(lng1)
    lat_2, lng_2 = radians(lat2), radians(lng2)
    d_lat, d_lng = (lat_2 - lat_1), (lng_2 - lng_1)
    a = sin(d_lat / 2)**2 + cos(lat_1) * cos(lat_2) * sin(d_lng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return radius * c

if __name__ == "__main__":
    ts, lat, lng = [], [], []
    file = open('mestrado/data/exp_1/20190807124800-gps.txt', 'r')
    for line in file.readlines():
        raw_ts, raw_lat, raw_lng = line.strip().split(';')
        ts.append(float(raw_ts))
        lat.append(float(raw_lat))
        lng.append(float(raw_lng))
    #1565233200000 -> day 8/8/19 - 0h - UTC-3
    threshold = 1565233200000
    min_lat, max_lat = min(lat), max(lat)
    min_lng, max_lng = min(lng), max(lng)
    for n in range(24):
        #fig, axs = plt.subplots(nrows=2, ncols=1)
        threshold_min, threshold_max = threshold, threshold+3600000
        threshold = threshold_max
        index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
        d_total=0
        for i in range(len(index)-1):
            distance = get_distance(lat[index[i]], lng[index[i]], lat[index[i+1]], lng[index[i+1]])*1000
            d_total += distance
            if distance > 3: print('{}h-{}m-{}m: andou {:.2f} metros'.format(n, i , i+1, distance))
            else: print('{}h-{}m-{}m: ócio'.format(n, i , i+1))
        print('Distância Total ({}-{}): {:.2f} metros'.format(n, n+1, d_total))
    # 10 minutes
    # for n in range(24):
    #     #fig, axs = plt.subplots(nrows=2, ncols=1)
    #     threshold_min, threshold_max = threshold, threshold+3600000
    #     threshold = threshold_max
    #     index = [i for i, x in enumerate(ts) if x >= threshold_min and x < threshold_max ]
    #     d_total=0
    #     for i in range(0, len(index), 10):
    #         distance = get_distance(lat[index[i]], lng[index[i]], lat[index[i+1]], lng[index[i+1]])*1000
    #         d_total += distance
    #         if distance > 3: print('{}h-{}m-{}m: andou {:.2f} metros'.format(n, i , i+1, distance))
    #         else: print('{}h-{}m-{}m: ócio'.format(n, i , i+10))
    #     print('Distância Total ({}-{}): {:.2f} metros'.format(n, n+1, d_total))
