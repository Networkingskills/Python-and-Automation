from netmiko import ConnectHandler

iosv_l2_2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.251.105',
    'username': 'admin',
    'password': 'cisco'
}

with open('L2_Default_Script') as f:
    lines = f.read().splitlines()
    print (lines)

all_devices = [iosv_l2_2, ]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('show ip int brief')
    print (output)

config_commands = ['int loop 0', 'ip address 2.2.2.2 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (20,23):
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output) 