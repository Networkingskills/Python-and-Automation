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

iosv_l2_4 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.251.105',
    'username': 'admin',
    'password': 'cisco'
}

all_devices = [iosv_l2_2, iosv_l2_3, iosv_l2_4 ]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('show ip int brief')
    print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (2,21):
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output) 