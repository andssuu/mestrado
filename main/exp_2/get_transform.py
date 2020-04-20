from datetime import datetime

if __name__ == "__main__":
    date = '20190914174500'
    path_file = 'mestrado/data/dados-jua-ams/experimento-02/mimosa/{}-acc.txt'.format(date)
    file = open(path_file, 'r')
    dt_obj = datetime.strptime('{}.{}.{} {}:{}:{},00'.format(date[6:8], date[4:6], date[0:4], date[8:10], date[10:12], date[12:14]), '%d.%m.%Y %H:%M:%S,%f')
    time_stamp = int(dt_obj.timestamp() * 1000)
    with open('mestrado/data/exp_2/{}.txt'.format(date), 'w') as f:
        for line in file.readlines():
            t, a_x, a_y, a_z, temp, g_x, g_y, g_z = line.strip().split(';')
            f.write('{};{};{};{};{};{};{};{}\n'.format(time_stamp,a_x, a_y, a_z, temp, g_x, g_y, g_z))
            time_stamp+=100
        f.close()
