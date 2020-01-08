# simplest styles to most complex
myname = 'Bob'
strNew = input("prompt: Enter value: ")

floatNew    = float(strNew)
intNew      = int(strNew)
print (strNew, myname, intNew, floatNew)
print ('floating point: %1.5f' % (floatNew))

print ('Use No formatting   | Hello',strNew, myname, intNew,floatNew)
print ('Use hex formatting  | Hello %s %x' % (myname, intNew)  )
print(f'Use f interpolation | Hello {myname} {intNew}')       # new string interpolation method
print ('Use .format         | Hello {} {}'.format( myname, intNew))     # new .format method
