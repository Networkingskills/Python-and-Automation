from napalm import get_network_driver
import json

driver = get_network_driver('ios')
iosvl2 = driver('10.10.251.105', 'admin', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output, indent =4))
