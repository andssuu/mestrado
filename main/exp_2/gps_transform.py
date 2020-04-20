import json

if __name__ == "__main__":
    file = open('mestrado/data/dados-jua-ams/experimento-02/mimosa/20190914174500-gps.txt', 'r')
    cow = []
    for line in file.readlines():
        ts, lat, lng= line.strip().split(';')
        obj = {}
        obj['ts'], obj['lat'], obj['lng'] = ts, lat, lng
        cow.append(obj)
    with open('mestrado/data/exp_2/cow_{}.json'.format(2), 'w') as f: f.write('cow_{} = '.format(2))
    with open('mestrado/data/exp_2/cow_{}.json'.format(2), 'a') as f: json.dump(cow, f, indent=2)
    f.close()
