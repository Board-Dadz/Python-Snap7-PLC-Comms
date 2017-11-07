#This is a basic working model of a PLC connection
#Currently this uses Snap7 to speak to PLC 161 Gappex PLC UPS
#With IP address: 192.168.0.241
#Siemens PLC 319F

import snap7
from snap7.util import *
import struct

print("Start communication to PLC")

#Connect to PLC as a client
plc = snap7.client.Client()
plc.connect ("192.168.0.241",0,2)

#Read data fro, DB120, from byte 0 for 1 byte
db = plc.db_read(120,0,1)
print(db)

print("Close communication PLC")

plc.disconnect()
