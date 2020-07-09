from serial import Serial

if __name__ == "__main__":
    port_name = "ttyUSB1"
    serial_port = Serial(port="/dev/"+port_name , baudrate=115200, bytesize=8, timeout=1)
    while(True):
        if(serial_port.in_waiting > 0):
            line = serial_port.readline()
            with open('mestrado/tics_4/data/mcu_{}.txt'.format(port_name),'ab') as f: f.write(line)
            print(line)
