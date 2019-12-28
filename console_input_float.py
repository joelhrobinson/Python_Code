# simple function call with parameters
# calculate fourth power of variable passed to function

############################################################
# DEFINE FUNCTION BEFORE USING IT
def fourthpower(f):     #parameter is an integer
    g = f * f * f * f
    print ( "Fourth power of  value of ", f, " is ", g)
#############################################################

print ("Enter two floating point values ")
x = float (input() ) 
y = float (input() )
print ("You entered ", x,y )

fourthpower(x)       # invoke the function
fourthpower(y)       # invoke with floating point value
print ("the end")