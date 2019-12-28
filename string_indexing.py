
# string indexing
mystring = "HelloWorld"
print ('pos index +0=H ', mystring[0])      # indexing starts at zero
print ('neg index -1=d ', mystring[-1])     # negative indexing starts at end with -1
###############################################################
# string slicing (indexed starting at zero)
print (mystring[0:5])           # slice index 0-5 up to but NOT including index '5'
print (mystring[2:])            # slice everything after AND including index '2'
print (mystring[:2])            # slice everything up to but NOT including index '2'
print (mystring[3:5])           # slice everything up to but NOT including index '2'
print( 'tinker'[1:4])
###############################################################
# step size
print (mystring[::2])           # step size slice every other character
print (mystring[::-1])          # reverse the letters
print ('Reverse This String'[::-1])  # reverse the letters
namex='Fred'
print (f'my name is {namex!r}') # use r! to print single quotes around name