#!/usr/bin/env python3

import subprocess

# subprocess.call("ifconfig wlan0 down", shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True)
# subprocess.call("ifconfig wlan0 up", shell=True)
print("Welcome to SpoofGoof - MAC address changer\n")
adapter = input("Please enter the adapter(such as eth0 or wlan0): \n")
changedMAC = input("Please enter the MAC address you which to spoof: \n")

# kill adapter
subprocess.call("ifconfig " + adapter + " down", shell=True)

# set hardware MAC address to be spoofed
subprocess.call("ifconfig " + adapter + " hw ether " + changedMAC, shell=True)

# wake adapter
subprocess.call("ifconfig " + adapter + " up", shell=True)

# print verification
print("Your MAC address on adapter " + adapter + " has been changed, and is now " + changedMAC)