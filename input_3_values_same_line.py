#######################################################
#######################################################
# input three values on SAME LINES
print ("Enter THREE floating point values X and Y on SAME LINE")


user_input = input("Enter three numbers separated by commas: ")
input_list = user_input.split(',')
myinputs = [float(i.strip()) for i in input_list]

print (*myinputs)           # printing the list using * operator separated  
print ("You entered", myinputs[0], myinputs[1], myinputs[2])

# printing the list using loop 
for x in range(len(myinputs)): 
    print ("loop:", myinputs[x])
print ('the end')