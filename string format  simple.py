# simplest styles to most complex
myname = 'Bob'
myerror = 50159747054
print (myerror)
print (format (myname, ">11s"))     # s=string  right justify if field of 11 char
print (f'{myerror:.11g}')           # g=general print 11 digits in decimal 
print ('{}'      .format (myerror)) # integer is default
print ('{:.11g} integer' .format (myerror)) # integer
print ('{0:b} binary' .format (myerror))   # binary
print ('{0:x} hex' .format (myerror))   # hex
print ('{0:o} octal' .format (myerror))   # octal
print ('{0:.3f} float' .format (myerror))   # floating point 3 decimal digits
print ('{:,} commas'    .format (myerror)) # add commas
print (f'{myerror:,} commas'    )
print ('No formatting       | Hello ', myname, myerror)        # no formatting method
print ('Old formatting      | Hello %s %x' % (myname, myerror))
print(f'New f interpolation | Hello {myname} {myerror}')       # new string interpolation method
print ('New .format         | Hello {} {}'.format( myname, myerror))     # new .format method

print ('Hey %(name)s, there is a 0x%(errno)x error!' % {
"name": myname, "errno": myerror })
