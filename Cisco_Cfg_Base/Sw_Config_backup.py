import getpass
import telnetlib


user = input("Enter your Username: ")
password = getpass.getpass()

f = open ('switches_vars')

for IP in f:
    IP=IP.strip()
    ## Remove any spaces##
    print ("Configuring Switch " + (IP))
    ## Print a msg showing Task that is running with switch/Name##
    HOST = IP
    ### Host should equal the value in the loop that open a file and find IPs#
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")

    print ("Configuring Vlans ")
    tn.write(b"config t\n")
    for n in range (2,11):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_ " + str(n).encode('ascii') + b"\n")
        
    tn.write(b"end\n")
    
    print ("Get Running Config from Devices  " + (IP))
    ## Print a msg showing task that is running with switch/Name##
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")

    print ("Save Config from Devices to files")
    readoutput = tn.read_all()
    saveoutout = open("switch_" + HOST, "w")
    ### open a file and name it switch + IP ##
    saveoutout.write(readoutput.decode('ascii'))
    ### write the output ##
    saveoutout.write("\n")
    saveoutout.close

    print(tn.read_all().decode('ascii'))
