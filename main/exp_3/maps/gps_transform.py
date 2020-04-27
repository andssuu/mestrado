import json

if __name__ == "__main__":
    cow = []
    file = open('mestrado/data/exp_3/20191021104433-gps.txt', 'r')
    for line in file.readlines():
        ts, lat, lng = line.strip().split(';')
        obj = {}
        obj['ts'], obj['lat'], obj['lng'] = ts, lat, lng
        cow.append(obj)
    with open('mestrado/data/exp_3/chuviscada.json', 'w') as f: f.write('chuviscada = ')
    with open('mestrado/data/exp_3/chuviscada.json', 'a') as f: json.dump(cow, f, indent=2)
    f.close()
