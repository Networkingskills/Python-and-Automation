from napalm import get_network_driver
import json

driver = get_network_driver('ios')
iosvl2 = driver('10.10.251.105', 'admin', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_users()
print (json.dumps(ios_output, indent =4))

ios_output = iosvl2.get_interfaces_ip()
print (json.dumps(ios_output, indent =4))

ios_output = iosvl2.get_arp_table()
print (json.dumps(ios_output, indent =4))

ios_output = iosvl2.ping('8.8.8.8')
print (json.dumps(ios_output, indent =4))
