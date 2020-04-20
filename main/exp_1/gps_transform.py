import json

cows = {'1': 'branquinha', '2':'mimosa', '3':'pretinha', '4': 'chuviscada'}
if __name__ == "__main__":
    for n in cows.keys():
        cow = []
        file = open('mestrado/data/dados-jua-ams/experimento-01/unified-gps-0{}.txt'.format(n), 'r')
        for line in file.readlines():
            ts, lat, lng= line.strip().split(';')
            obj = {}
            obj['ts'], obj['lat'], obj['lng'] = ts, lat, lng
            cow.append(obj)
        with open('mestrado/data/exp_1/cow_{}.json'.format(n), 'w') as f: f.write('cow_{} = '.format(n))
        with open('mestrado/data/exp_1/cow_{}.json'.format(n), 'a') as f: json.dump(cow, f, indent=2)
        f.close()
