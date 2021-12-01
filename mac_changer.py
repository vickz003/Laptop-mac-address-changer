import subprocess
import optparse

a = optparse.OptionParser()

a.add_option("-i","--interface",dest="interface",help="use to interface")
a.add_option("-m","--mac",dest="mac",help="use to mac_address")

(x , y) = a.parse_args()

interface  = x.interface
mac_address = x.mac

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + mac_address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

print("changing " +interface+ " to " + mac_address)

