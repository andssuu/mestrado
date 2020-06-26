import matplotlib.pyplot as plt

if __name__ == "__main__":
    vedba, scay, activity = [], [], []
    file = open('mestrado/data/others/diosdado.txt', 'r')
    # 1 min [1:2020]
    # 5 min [2021:2424]
    # 10 min [2425, 2626]
    size = 10
    windows = {1:[1, 2020], 5: [2021, 2424], 10: [2425, 2626]}
    for line in file.readlines()[windows[size][0]:windows[size][1]]:
        raw_vedba, raw_scay, raw_activity = line.strip().split()
        vedba.append(float(raw_vedba))
        scay.append(float(raw_scay))
        activity.append(raw_activity)
    colors = {'Feeding':'r', 'Drinking':'b', 'Standing':'g', 'Lying':'y'}
    label_color = [colors[l] for l in activity]
    label_color = [colors[l] for l in activity]
    for p1, p2, c in zip(vedba, scay, label_color):
       plt.plot(p1, p2, '*{}'.format(c))
    plt.xlabel('vedba', fontsize=12)
    plt.ylabel('scay', fontsize=12)
    plt.title('Base Diosdado {} min'.format(size))
    plt.show()
