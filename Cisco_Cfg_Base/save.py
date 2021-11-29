import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open ('switches_vars')

for IP in f:
    IP=IP.strip()
    ## Below remove any spaces##
    print ("Configuring Switch " + (IP))
    ## Print a msg showing switch IP of the switch being configured ##
    HOST = IP
    ### Host should equal the value in the loop that open a file and find IPs#
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")

    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
