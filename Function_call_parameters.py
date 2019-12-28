# simple function call with parameters
# calculate fourth power of variable passed to function

############################################################
# DEFINE FUNCTION BEFORE USING IT
def fourthpower(f):     #parameter is an integer
    g = f * f * f * f
    print ( "Fourth power of  value of ", f, " is ", g)
#############################################################

print ("Enter two values ")
string1 = input()       # get first input string
x = int(string1)        # convert to integer
y = int(input())        # get second input string and convert all in one line
print ("Original values are ",x, y )

fourthpower(x+y)        # invoke the function
fourthpower(1.53)       # invoke with floating point value
print ("the end")


fourthpower(x+y)       # invoke the function
print ("the end")