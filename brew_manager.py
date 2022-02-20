import sys
import time

from teckin_plug import manage_plug as plug
from temperature import checker as temp
import requests
import config

low_temp = 21.00
high_temp = 22.00


def main(log_file):
    current_time = time.asctime(time.localtime(time.time()))
    current_temp = temp.read_temp()
    api_url = 'http://' + config.HOMEASSISTS_CONFIG['host'] + ':' + config.HOMEASSISTS_CONFIG['port'] + config.HOMEASSISTS_CONFIG['slug'] + config.HOMEASSISTS_CONFIG['sensor']
    data = {'state': current_temp}
    headers = {'Authorization': 'Bearer ' + config.HOMEASSISTS_CONFIG['token'], 'Content-Type': 'application/json'}
    requests.post(api_url, json=data, headers=headers)
    # requests.post(api_url, data=data, headers=headers).json())
    # print(current_temp)
    # plug_is_on = plug.running_state()
    #
    # if float(current_temp) < low_temp:
    #     print("Brrr ... it's cold, is the plug currently Running? ", plug_is_on)
    #     if not plug_is_on:
    #         plug.switch_status("on")
    #         print("Turned the plug on")
    # elif float(current_temp) > high_temp:
    #     print("Ouch, its getting warm, is the plug on? ", plug_is_on)
    #     if plug_is_on:
    #         plug.switch_status("off")
    #         print("Turned the plug off")
    # print("Plug status: ", plug_is_on, "Current_temp: ", current_temp)
    # data_line = "Temp at time " + current_time + " is: " + str(current_temp) + "\n"
    #
    # if log_file:
    #     with open(log_file, 'a') as f:
    #         f.write(data_line)
    # else:
    #     print(data_line)


if __name__ == "__main__":
    main(sys.argv[1])
