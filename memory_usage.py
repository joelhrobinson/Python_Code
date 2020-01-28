import sys


ii = -1
jj = +4
print (ii,jj)
print ( abs(ii+jj) )
print ( abs(ii) + abs(jj)  )
print(" variable size is:",sys.getsizeof(ii) )

singlequote = 'this is a single quote string'
doublequote = "this is a double quote string"
print(" single quote size is:",sys.getsizeof(singlequote) )
print(" double quote size is:",sys.getsizeof(doublequote) )

print ("done")
