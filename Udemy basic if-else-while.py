# Udemy Numbers.py
import os
a=9
b=0
while b <= a:   # WHILE COUNT execution
    b=b+1
    print ('b=',b)
c=1
if c <= a:      # one time IF execution
    c = c+1
    print ("IF TRUE c=",c)
##################
c=99
if c <= a:      # one time ELSE execution
    c = c+1
    print ("IF TRUE c=",c)
else: 
    print ('ELSE FALSE c=', c)
#####################
active = True
while active:   # WHILE TRUE one time execution
    print ('While True.False loop:', active)
    active = False

print ('##################')
c=-1
if c > 0:      # one time ELSE execution
    print ("IF positive c=",c)
elif c==0: 
    print ('ELIF c==zero c=', c)
elif c < 0:
    print ('ELIF c negative c=',c)