from pyBusPirateLite.I2Chigh import *
import struct 

EEPROM_SIZE = 1024
OUTPUT_FILE = "eeprom_dump.bin"

i2c = I2Chigh("COM13", 115200, 5)
i2c.BBmode()
i2c.enter_I2C()
i2c.cfg_pins(I2CPins.POWER | I2CPins.PULLUPS)

#reset current address
i2c.send_start_bit()
i2c.bulk_trans(2, [0xa0, 0x00])
i2c.send_start_bit()
i2c.bulk_trans(1, [0xa1])
r = i2c.read_byte() #value at addr 0x0
r = ord(r)
i2c.send_stop_bit()
print "%X%X: %X"%(0xa1,0x0,r)
dump = [r]

# read the rest
for i in range(EEPROM_SIZE-1):
   addr = (i>>8)&0b11
   devSelect = 0xa1 | (addr<<1)
   addr = i & 0xff
   i2c.send_start_bit()
   i2c.bulk_trans(1, [devSelect])   
   r = i2c.read_byte()
   r = ord(r)
   i2c.send_stop_bit()
   print "%X%X: %X"%(devSelect,addr,r)
   dump.append(r)

#write to fie
print "Writing to file: %s"%OUTPUT_FILE
f = open(OUTPUT_FILE,"wb")
struct_fmt = "%dB"%len(dump)
f.write(struct.pack(struct_fmt, *dump))
f.close()