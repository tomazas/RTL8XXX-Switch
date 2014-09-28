import sys

if len(sys.argv)<2:
   print "python read_dump.py <dump binary>"

f = open(sys.argv[1],"rb").read()
b = (ord(f[1])<<8)|ord(f[0])
print "First 2 bytes 0x%X"%b
read_until = b&0xFFF
print "Read until 0x%04X"%read_until
i = 2
reg = None
count = 0
while i < len(f):
   if i == read_until: break
   b1 = ord(f[i])
   b2 = ord(f[i+1])
   b = (b2<<8)|b1
   if reg is None: reg = b
   else: 
      print "%04X 0x%04X: 0x%04X"%(i,reg,b)
      reg = None
      count = count + 1
   i = i + 2

print "Register count: %d (0x%X)"%(count,count)