from temperature import checker as temp
import requests
import config

low_temp = 21.00
high_temp = 22.00


def main():
    current_temp = temp.read_temp()
    api_url = 'http://' + config.HOMEASSISTS_CONFIG['host'] + ':' + config.HOMEASSISTS_CONFIG['port'] + config.HOMEASSISTS_CONFIG['slug'] + config.HOMEASSISTS_CONFIG['sensor']
    data = {'state': current_temp}
    headers = {'Authorization': 'Bearer ' + config.HOMEASSISTS_CONFIG['token'], 'Content-Type': 'application/json'}
    requests.post(api_url, json=data, headers=headers)

if __name__ == "__main__":
    main()
