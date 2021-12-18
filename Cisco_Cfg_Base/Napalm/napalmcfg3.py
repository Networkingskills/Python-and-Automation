## script to load_merge_candidate - from a differnet files ##
from napalm import get_network_driver
import json


Device_list = ['10.10.251.100',
            '10.10.251.110'
            ]

for ip_address in Device_list:
    print (" Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    ios_router = driver(ip_address, 'admin', 'cisco')
    ios_router.open()

    ## load_merge_candidate - the action is add config from ACL1
    ios_router.load_merge_candidate(filename='ACL1.cfg')

    diffs = ios_router.compare_config()
    if len(diffs) > 0:
        print(diffs)
        print(" Updating configuration to standard")
        ios_router.commit_config()
    else:
        print(" No change Required.")
        ios_router.discard_config()

    ## load_merge_candidate - the action is add config from ACL1
    ios_router.load_merge_candidate(filename='loopback.cfg')

    diffs = ios_router.compare_config()
    if len(diffs) > 0:
        print(diffs)
        print(" Updating configuration to standard")
        ios_router.commit_config()
    else:
        print(" No change Required.")
        ios_router.discard_config()

ios_router.close()
