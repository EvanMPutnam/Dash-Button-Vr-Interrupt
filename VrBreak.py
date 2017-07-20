"""
Author: Evan Putnam
Description: Implements a key press of the f1 key that interrupts the htc vive, when pressing an amazon dash button.
Pre-Reqs: scapy-python3, pyautogui

#pip install scapy-python3
#pip install pyautogui
"""
from scapy.all import *
import pyautogui

def knockKnock():
    pyautogui.press('f1')

def arpCallback(pkt):
    if ARP in pkt and pkt[ARP].op == 1:
        #Need to hard code the mac address below
        if pkt[ARP].hwsrc == '':
            print("starting")
            knockKnock()
            return pkt.sprintf("Button Pressed!")


def main():
    sniff(prn=arpCallback, filter="arp", store=0, count=0)

if __name__ == '__main__':
    main()
