from netmiko import ConnectHandler
## import your lib


## open file of commands
with open('commands_file') as f:
    commands = f.read().splitlines()

# list your dictionary ( devices) 
ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '10.10.251.101',
    'username': 'admin',
    'password': 'cisco'
}

all_devices = [ios_devices]

## create a loop to connect to devices
for devices in all_devices:
    ## Use connect hanndler to connect to the switch
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands)
    ## Print output
    print (output)