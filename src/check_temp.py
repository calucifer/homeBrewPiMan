import os
import sys
import glob
import time
from teckin_plug import manage_plug as plug

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

low_temp = 21.00
high_temp = 23.00

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return "{:.2f}".format(temp_c)


def main(log_file):
    current_time = time.asctime( time.localtime(time.time()))

    current_temp = read_temp()
    plug_is_on = plug.running_state()
    if float(current_temp) < low_temp:
        print("Brrr ... it's cold, is the plug currently Running? ",plug_is_on)
        if not plug_is_on:
            plug.switch_status("on")
            print("Turned the plug on")
    elif float(current_temp) > high_temp:
        print("Ouch, its getting warm, is the plug on? ",plug_is_on)
        if plug_is_on:
            plug.switch_status("off")
            print("Turned the plug off")
    print("Plug status: ", plug_is_on, "Current_temp: ", current_temp)
    data_line = "Temp at time " + current_time + " is: " + str(read_temp()) + "\n"

    if log_file:
        with open(log_file, 'a') as f:
            f.write(data_line)
    else:
        print(data_line)


if __name__ == "__main__":
    main(sys.argv[1])
