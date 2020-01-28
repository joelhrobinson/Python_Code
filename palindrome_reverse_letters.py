def palindrome(a):
    return a == a[::-1]

print (palindrome('MoM')   ) # True
print (palindrome('mom 2 mom')   ) # True
print (palindrome('was it a rat i saw')   ) # True
print (palindrome('wasitaratisaw')   ) # True

aaaa = 'joel'
b=aaaa.capitalize()
print (b)