import json

if __name__ == "__main__":
    file = open('mestrado/data/dados-jua-ams/experimento-03/Chuviscada_3/20191021104433-gps.txt', 'r')
    cow = []
    for line in file.readlines():
        ts, lat, lng= line.strip().split(';')
        obj = {}
        obj['ts'], obj['lat'], obj['lng'] = ts, lat, lng
        cow.append(obj)
    with open('mestrado/data/exp_3/cow_{}.json'.format(4), 'w') as f: f.write('cow_{} = '.format(4))
    with open('mestrado/data/exp_3/cow_{}.json'.format(4), 'a') as f: json.dump(cow, f, indent=2)
    f.close()
