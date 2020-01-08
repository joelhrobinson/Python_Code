### READ JSON FILE
import os           ## import os operating sytem library
import json
os.chdir ("L:/SOFTWARE/PYTHON/TEMP")
os.getcwd()

############################################################################
# open file to write   
try:
    f = open("mylanguages.txt","r") 
    print ("Found file=mylanguages.txt for read")
except IOError:        
    print('file mylanguages.txtn open error: ', IOError ) 
f.close()
############################################################################
f = open("mylanguages.txt","r") 
line = f.read(5)     # read this many characters 
print ('read characters from file:', line)
f.close()

f = open("mylanguages.txt","r") 
line = f.readlines(2)     # read this many characters
line = [x.strip() for x in line]  
print ('read lines from file:', line)

f.close()
