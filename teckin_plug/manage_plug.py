import pytuya

import config


def running_state():
    d = pytuya.OutletDevice(config.PLUG_CONFIG['id'], config.PLUG_CONFIG['host'], config.PLUG_CONFIG['key'])
    data = d.status()
    return data['dps']['1']


def switch_status(status):
    state = {'on': True, 'off': False}
    d = pytuya.OutletDevice(config.PLUG_CONFIG['id'], config.PLUG_CONFIG['host'], config.PLUG_CONFIG['key'])
    d.set_status(state[status])  # This requires a valid key
