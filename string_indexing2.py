
# string indexing
hw = 'Hello World'
print( hw[8])                   # print 'r'
print( 'Hello World'[8])        # print 'r'

print( 'tinker'[1:4])           # print 'ink'
##################################################
# strings are immutable >> cannot be changed
sname = "Samuel"
pname = "Pamela"
newname = pname[0] + sname[1:3]
print (sname, pname, newname)   # print 'Pam"
print ('z' * 10)    # prints zzzzzzzzzz
print ('2' + '3')       # prints '23'
x = "Hello Boise"
print (x.upper() )      # convert to upper case
print (x.split() )       # splits by white space
print (x.split('l')   )     # splits by letter 'l'

