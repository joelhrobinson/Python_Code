print ('enter multiple values on one line')

###############################################################
# taking two inputs at a time and convert to floating point
x, y = input("Enter # pounds # ounces in decimal no comma please: ").split() 
print("Number of pounds: ", float(x)) 
print("Number of ounces: ", float(y), '\'') 

###############################################################
# taking two inputs at a time convert to integer
x, y = input("Enter # boys #girls in integer no comma please: ").split() 
print("Number of boys: ", int(x)) 
print("Number of girls: ", int(y), '\'')  

###############################################################3
# taking two inputs at a time and formatting them
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 

#################################################################
# taking unknown # inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter any # of integers3 3: ").split())) 
print("List of students: ", x) 
