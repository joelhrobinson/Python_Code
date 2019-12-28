# format two floating numbers


print ("Enter two floating point values X and Y on two separate lines")
x = float (input() ) 
y = float (input() ) 
print ("You entered X and Y ", x, y)


print ('floating point format 9.3 ={r:9.3f}' .format (r=x))    # use "f" to prevent going exponential
print ('floating point format 9.3 ={r:9.3f}' .format (r=y))

print(f'{x:9.4f}')
print (f'printf Unformatted   = {x}')
print (f'printf Formatted 6.3 = {y:6.3}')

numbers = [123.23, 0.123456, 1, 1234567.891, 9887.2]

for number in numbers:
    print(f'{number:9.4f}')