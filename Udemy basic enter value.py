# Udemy enter value.py

### STRING INPUT
sss = input("Enter your name: ")
print ('you entered string = ',sss)
print ('type of input=', type(sss),'\n')

#### INTEGER INPUT
age = input("Enter age as integer: ")
print ('you entered string = ',age)
iii = int(age)              # convert string to integer
print ('your age as intger=', iii,'\n')

#### FLOATING POINT INPUT
age = float (input("Enter age as decimal: "))  # convert string to float
print ('you entered string = ',age)
vvv = age
print ('your age as float=', vvv,'\n')

lst = []
howmanygkids = int(input('enter # kids'))   # get # inputs to follow
for i in range (0,howmanygkids):
    gk = int(input('enter age'))
    lst.append(gk)
print (lst)