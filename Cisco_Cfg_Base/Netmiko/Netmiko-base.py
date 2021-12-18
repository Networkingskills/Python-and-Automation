## import your lib
from netmiko import ConnectHandler

# list your dictionary ( devices) 
iosv_l2_2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.251.101',
    'username': 'admin',
    'password': 'cisco'
}

## Use connect hanndler to connect to the switch
net_connect = ConnectHandler(**iosv_l2_2)

## run a command 
output = net_connect.send_command('show ip int brief')

## Print output
print (output)