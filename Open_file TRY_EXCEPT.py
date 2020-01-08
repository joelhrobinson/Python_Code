### Open File TRY EXCEPT
import os           ## import os operating sytem library
os.chdir ("L:/SOFTWARE/PYTHON/TEMP")
os.getcwd()
############################################################################
try:
    f = open("unicorn","r")    # "w" for write "r" for read
    f.close()
    print ("Found file=unicorn")

except IOError:       # print(os.error) will <class 'OSError'> 
    print('file unicorn does not exist: ', IOError ) 
f = open("unicorn","w")  
    ############################################################################
try:
    f = open("joel01.txt","r")    # "w" for write "r" for read
    for i in range(10):
        f.write("Hello world %d \n" % (i+1))        # this will generate an error if "r"
    f.close()
    print ("Write to file=joel01.txt")

except IOError:   
    # print(os.error) will <class 'OSError'> 
    print('file joel01.txt is read only: ', IOError )
