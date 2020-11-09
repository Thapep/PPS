#import matplotlib.py as pl
import re
serial = open('../serial/rgol.out','r')
lines = serial.readlines()
print(lines)
tserial={}
#re.find(r'[+-]?\d+(?:\.\d+)?', lines[i]))
for i in range(len(lines)):
    tserial[] = 

print(tserial)