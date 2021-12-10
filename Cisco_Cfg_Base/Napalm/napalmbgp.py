from napalm import get_network_driver
import json

driver = get_network_driver('ios')
iosvl2 = driver('10.10.251.100', 'admin', 'cisco')
iosvl2.open()

## bgp_nei is just a name - the action is .get_bgp_nei 
bgp_neighbor = iosvl2.get_bgp_neighbors()
print (json.dumps(bgp_neighbor, indent =4))

iosvl2.close()
