from napalm import get_network_driver
import json

bgplist = ['10.10.251.100',
            '10.10.251.110'
            ]

for ip_address in bgplist:
    print (" Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    ios_router = driver(ip_address, 'admin', 'cisco')
    ios_router.open()
    ## bgp_nei is just a name of the task - the action is .get_bgp_nei 
    bgp_neighbor = ios_router.get_bgp_neighbors()
    print (json.dumps(bgp_neighbor, indent =4))
    ios_router.close()
