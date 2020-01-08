### Open File TRY EXCEPT
import os           ## import os operating sytem library
os.chdir ("L:/SOFTWARE/PYTHON/TEMP")
os.getcwd()

############################################################################
# open file to write   
try:
    f = open("unicorn.json","w") 
    print ("Found file=unicorn.json for read")
except IOError:        
    print('file unicorn.json open to write error: ', IOError ) 
f.close()
############################################################################
# open file to read
try:
    f = open("unicorn.json","r")    # "w" for write "r" for read
    print ("Found file=unicorn.json for write")
except IOError:        
    print('file unicorn.json open to read error: ', IOError ) 
f.close()
############################################################################
# open file to write again:
try:
    i = 1
    f = open("unicorn.json","w")
    while i < 10:
        f.write("Hello world %d \n" % (i))
        i = i+1       
except IOError:        
    print('file unicorn.json open to write error: ', IOError ) 
f.close()
 
