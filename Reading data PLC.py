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

#Read byte from DB8000, from byte 0 for 1 byte
db = plc.db_read(8000,0,1)

print (db)


#Read int from DB8000, from byte 2 for 2 byte
db = plc.db_read(8000,2,2)
cat = struct.unpack('>H',db)

print (cat)


#Read DINT from DB8000, from byte 4 for 4 byte
db = plc.db_read(8000,4,4)
cat = struct.unpack('>l',db)

print (cat)


#Read REAL from DB8000, from byte 8 for 4 byte
db = plc.db_read(8000,8,4)
cat = struct.unpack('>f',db)

print (cat)



print("Close communication PLC")

plc.disconnect()
