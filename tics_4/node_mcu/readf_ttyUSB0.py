if __name__ == "__main__":
    with open('mestrado/tics4/data/mcu_ttyUSB0.txt','r') as f: lines = f.readlines()
    for l in lines: print(l)
