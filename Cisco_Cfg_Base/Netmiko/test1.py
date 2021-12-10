from netmiko import ConnectHandler

iosv_l2_2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.251.102',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_3 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.251.103',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_5 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.251.105',
    'username': 'admin',
    'password': 'cisco'
}



with open('L2_Default_Script') as f:
    lines = f.read().splitlines()
    print (lines)

all_devices = [iosv_l2_5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

with open('All_switches') as f:
    lines = f.read().splitlines()
    print (lines)

all_devices = [iosv_l2_2, iosv_l2_3, iosv_l2_5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)