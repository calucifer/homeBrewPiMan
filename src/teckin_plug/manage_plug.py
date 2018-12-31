import pytuya
import config

def running_state():
    d = pytuya.OutletDevice(config.PLUG_CONFIG['id'], config.PLUG_CONFIG['host'], config.PLUG_CONFIG['key'])
    data = d.status()
    return data['dps']['1']

def switch_status(status):
    state = {'on': True, 'off': False}

    d = pytuya.OutletDevice('46011085807d3a6fc88f', '192.168.9.15', '5ff9298cf4ba8f45')
    d.set_status(state[status])  # This requires a valid key


# d = pytuya.OutletDevice('46011085807d3a6fc88f', '192.168.9.15', '5ff9298cf4ba8f45')
# data = d.status()  # NOTE this does NOT require a valid key
# print('Dictionary %r' % data)
# print('state (bool, true is ON) %r' % data['dps']['1'])  # Show status of first controlled switch on device
#
# # Toggle switch state
# switch_state = data['dps']['1']
# data = d.set_status(not switch_state)  # This requires a valid key
# if data:
#     print('set_status() result %r' % data)
#
# # on a switch that has 4 controllable ports, turn the fourth OFF (1 is the first)
# data = d.set_status(False, 4)
# if data:
#     print('set_status() result %r' % data)
#     print('set_status() extrat %r' % data[20:-8])
