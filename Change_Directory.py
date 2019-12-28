# python file created from new
import datetime
import time
import os
mypath = 'L:/SOFTWARE/PYTHON/Python_Scripting'
os.chdir(mypath)
print ('Hello world  1')
x = 2
time.sleep (1)
print ('Hello world ', x, end='\n')
time.sleep (1)
msg = 'Hello world  3'
print (msg)
os.getcwd()
os.chdir ("L:/SOFTWARE/PYTHON/TEMP")
os.getcwd()
f = open("joel-hello-world.txt","w+")
f.write("Hello world  4 %d\r\n" )