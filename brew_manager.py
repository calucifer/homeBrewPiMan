import sys
import time

from teckin_plug import manage_plug as plug
from temperature import checker as temp

low_temp = 21.00
high_temp = 23.00


def main(log_file):
    current_time = time.asctime(time.localtime(time.time()))
    current_temp = temp.read_temp()
    plug_is_on = plug.running_state()

    if float(current_temp) < low_temp:
        print("Brrr ... it's cold, is the plug currently Running? ", plug_is_on)
        if not plug_is_on:
            plug.switch_status("on")
            print("Turned the plug on")
    elif float(current_temp) > high_temp:
        print("Ouch, its getting warm, is the plug on? ", plug_is_on)
        if plug_is_on:
            plug.switch_status("off")
            print("Turned the plug off")
    print("Plug status: ", plug_is_on, "Current_temp: ", current_temp)
    data_line = "Temp at time " + current_time + " is: " + str(current_temp) + "\n"

    if log_file:
        with open(log_file, 'a') as f:
            f.write(data_line)
    else:
        print(data_line)


if __name__ == "__main__":
    main(sys.argv[1])
