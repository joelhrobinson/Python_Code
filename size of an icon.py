import sys


def byte_size(string):
    return(len(string.encode('utf-8')))

x = byte_size('😀') 
y = byte_size('Hello World') 
print ('😀') 
print ('Hello World') 
print ( byte_size('😀')  )              # 4
print ( byte_size('Hello World') )      # 11    
print(" icon size is:",sys.getsizeof(x) )
print(" string size is:",sys.getsizeof(y) )

print ("done")
